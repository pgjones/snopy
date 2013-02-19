#!/usr/bin/env python
#
# signal_rejection.py
#
# Base class for applying signal rejection to raw data. General radial rejection is taken care of
# by the FiducialRejection class.
#
# Author P G Jones - 23/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import spectrum_util

class SignalRejection(object):
    """ Base class for signal rejection application."""
    def __init__(self):
        """ Initialise the energy resolution."""
        pass
    def apply(self, raw_data):
        """ Apply the signal rejection to the raw_data."""
        result = spectrum_util.default_raw(raw_data.GetName())
        for bin_radius in range(1, raw_data.GetNbinsY() + 1):
            for bin_energy in range(1, raw_data.GetNbinsX() + 1):
                net_count = raw_data.GetBinContent(bin_energy, bin_radius)
                survival_factor = self.get_survival_factor(raw_data.GetName(),
                                                           raw_data.GetXaxis().GetBinCenter(bin_energy),
                                                           raw_data.GetYaxis().GetBinCenter(bin_radius))
                result.SetBinContent(bin_energy, bin_radius, net_count * survival_factor)
        return result
    ################################################################################################
    def get_survival_factor(self, name, energy, radius):
        """ Return the survival factor."""
        pass

class NoRejection(SignalRejection):
    def get_survival_factor(self, name, energy, radius):
        return 1.0
