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
    def generate(self):
        """ Calculate pileup, apply the rejection, energy resolution, and return the detected 
        data set."""
        detected_data_set = data_set.DetectedDataSet("Simulated")
        if self._pileup:
            self.calculate_pileup() # Adds to the raw data set
        for data in self._raw_data.iter_backgrounds():
            print data.GetName()
            detected_data_set.add_background(self._apply_processes(data))
        detected_data_set.set_signal(self._apply_processes(self._raw_data.get_signal()),
                                     self._raw_data.get_signal().GetSumOfWeights())
        return detected_data_set
    def set_energy_resolution(self, energy_resolution):
        """ Set the energy resolution type."""
        self._energy_resolution = energy_resolution
    def set_pileup(self, calc_pileup):
        """ Set pileup calculation on/off."""
        self._pileup = calc_pileup
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
