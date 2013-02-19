#!/usr/bin/env python
#
# fiducial_rejection.py
#
# Base class for applying fiducial rejection to raw data. General signal rejection is taken care of
# by the SignalRejection class.
#
# Author P G Jones - 23/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import spectrum_util

class FiducialRejection(object):
    """ Base class for fiducial rejection application."""
    def __init__(self):
        """ Initialise the energy resolution."""
        pass
    def apply(self, raw_data):
        """ Apply the fiducial rejection to the raw_data."""
        result = spectrum_util.default_raw(raw_data.GetName())
        for bin_radius in range(1, raw_data.GetNbinsY() + 1):
            for bin_energy in range(1, raw_data.GetNbinsX() + 1):
                net_count = raw_data.GetBinContent(bin_energy, bin_radius)
                survival_factor = self.get_survival_factor(raw_data.GetXaxis().GetBinCenter(bin_energy),
                                                           raw_data.GetYaxis().GetBinCenter(bin_radius))
                result.SetBinContent(bin_energy, bin_radius, net_count * survival_factor)
        return result
    ################################################################################################
    def get_survival_factor(self, energy, radius):
        """ Return the survival factor."""
        pass

class RadialFixedRejection(FiducialRejection):
    """ Apply a fixed radial rejection."""
    def __init__(self, radial_cut):
        """ Initialise with the maximum radius that isn't cut."""
        super(RadialFixedRejection, self).__init__()
        self._radial_cut = radial_cut
    def get_survival_factor(self, energy, radius):
        """ Return the survival factor."""
        if radius < self._radial_cut:
            return 1.0
        else:
            return 0.0
