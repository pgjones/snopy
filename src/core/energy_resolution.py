#!/usr/bin/env python
#
# energy_resolution.py
#
# Base class for applying energy resolution to raw data and an implementation that represents the 
# current best knowledge of the SNO+ detector.
#
# Author P G Jones - 23/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import spectrum_util
import math
import os
import ROOT

class EnergyResolution(object):
    """ Base class for energy resolution application."""
    def __init__(self):
        """ Initialise the energy resolution."""
        pass
    def apply(self, raw_data):
        """ Apply the energy resolution to the raw_data."""
        pass
    ################################################################################################
    def get_resolution(self, energy, radius):
        """ Return the resolution (FWHM)."""
        return self.get_sigma(energy, radius) * 2.0 * math.sqrt(2.0 * math.Log(2.0))
    def get_sigma(self, energy, radius):
        """ Return the sigma given the energy and radius."""
        pass

# Load the function
ROOT.gROOT.ProcessLine(".L " + os.path.dirname(__file__) + "/GaussianXConvolve.cc+");

class GaussianResolution(EnergyResolution):
    """ A Gaussian shaped energy resolution)."""
    def __init__(self):
        """ Initialise the base class."""
        super(GaussianResolution, self).__init__() 
    def apply(self, raw_data):
        """ Apply the Gaussian energy resolution to the raw_data."""
        sigma_data = spectrum_util.default_raw(raw_data.GetName())
        for bin_radius in range(1, raw_data.GetNbinsY() + 1):
            for bin_energy in range(1, raw_data.GetNbinsX() + 1):
                sigma_data.SetBinContent(bin_energy, bin_radius, 
                                         self.get_sigma(raw_data.GetXaxis().GetBinCenter(bin_energy), # In MeV
                                                        raw_data.GetYaxis().GetBinCenter(bin_radius)))
        result = spectrum_util.default_raw(raw_data.GetName())
        ROOT.GaussianXConvolve(result, raw_data, sigma_data)
        return result

class NhitResolution(GaussianResolution):
    """ A fixed nhit based resolution energy resolution class."""
    def __init__(self, nhit_per_MeV):
        """ Initialise with the fixed nhit per MeV."""
        super(NhitResolution, self).__init__()
        self._nhit_per_MeV = nhit_per_MeV
    def get_sigma(self, energy, radius):
        """ Return the sigma given the energy and radius."""
        # Find MeV resolution at this energy
        num_hits = self._nhit_per_MeV * energy
        # Sigma in NHits is sqrt(num_hits) in energy it is times energy / num_hits or 1 / nhit_per_MeV
        return math.sqrt(num_hits) / num_hits * energy
        
        
