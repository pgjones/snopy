#!/usr/bin/env python
#
# Simulation
#
# Simulation class, turns raw data sets into detected data sets using the applied energy resolution
# pileup generation with rejection and data rejection.
#
# Author P G Jones - 22/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import data_set
import spectrum_util
import pileup

class Simulation(object):
    """ Contains a raw data spectra."""
    def __init__(self, name, raw_data_set):
        """ Initialise the raw data with a name and the full spectrum, the full spectrum should be
        a TH2D."""
        self._raw_data = raw_data_set
        self._energy_resolution = None
        self._fiducial = None
        self._rejection = None
        self._pileup = False
        self._pileup_window = 400.0 # in ns
    def generate(self):
        """ Calculate pileup, apply the rejection, energy resolution, and return the detected 
        data set."""
        detected_data_set = data_set.DetectedDataSet("Simulated")
        if self._pileup:
            detected_data_set.add_backgrounds(self._calculate_pileup())
        for data in self._raw_data.iter_backgrounds():
            print data.GetName()
            detected_data_set.add_background(self._apply_processes(data))
        detected_data_set.set_signal(self._apply_processes(self._raw_data.get_signal()),
                                     self._raw_data.get_signal().GetSumOfWeights())
        return detected_data_set
    def set_energy_resolution(self, energy_resolution):
        """ Set the energy resolution type."""
        self._energy_resolution = energy_resolution
    def set_pileup(self, calc_pileup, pileup_window=400.0):
        """ Set pileup calculation on/off."""
        self._pileup = calc_pileup
        self._pileup_window = pileup_window
    def set_fiducial_rejection(self, fiducial_rejection):
        """ Set the fiducial rejection type."""
        self._fiducial = fiducial_rejection
    def set_rejection(self, rejection):
        """ Set the rejection type."""
        self._rejection = rejection
    ################################################################################################
    def _apply_processes(self, data):
        """ Apply the rejection, energy resolution, and return the detected data set."""
        fiducial_data = self._fiducial.apply(data)
        rejected_data = self._rejection.apply(fiducial_data)
        energy_res_data = self._energy_resolution.apply(rejected_data)
        return spectrum_util.flattern(energy_res_data)
    def _calculate_pileup(self):
        """ Calculate the pileup backgrounds, then apply fiducial and energy resolution, 
        then flattern."""
        pileup_backgrounds = []
        for data1 in self._raw_data.iter_backgrounds():
            print data1.GetName()
            for data2 in self._raw_data.iter_backgrounds():
                print "\t", data2.GetName()
                activity = pileup.activity(data1, data2, None, self._pileup_window)
                if activity > 1:
                    pileup_backgrounds.append(pileup.spectra(data1, data2, None, activity, self._rejection))
                for data3 in self._raw_data.iter_backgrounds():
                    print "\t\t", data3.GetName()
                    activity = pileup.activity(data1, data2, data3, self._pileup_window)
                    if activity > 1:
                        pileup_backgrounds.append(pileup.spectra(data1, data2, data3, activity, self._rejection))
        pileup_backgrounds = set(pileup_backgrounds)
        detected_pileup = []
        for data in pileup_backgrounds:
            fiducial_data = self._fiducial.apply(data)
            energy_res_data = self._energy_resolution.apply(fiducial_data)
            detected_pileup.append(spectrum_util.flattern(energy_res_data))
        return detected_pileup
