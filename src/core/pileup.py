#!/usr/bin/env python
#
# pileup.py
#
# Functions to calculate the pileup spectra.
#
# Author P G Jones - 21/02/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import constants
import math_util
import spectrum_util
import os
import ROOT

def _new_spectra(old_spectra):
    """ Produce a new normalised spectra."""
    new_spectra = old_spectra.Clone(old_spectra.GetName())
    new_spectra.SetDirectory(0)
    new_spectra.Scale(1.0 / new_spectra.GetSumOfWeights())
    return new_spectra

# Load the function
ROOT.gROOT.ProcessLine(".L " + os.path.dirname(__file__) + "/GaussianXConvolve.cc+");

def _convolve_reject(spectra1, spectra2, rejection):
    """ Return a convolution of the two spectra with rejection applied."""
    convolved = _new_spectra(spectra1)
    ROOT.ConvolveReject(convolved, spectra1, spectra2)
    # (c)(b1) = sum(b2) h1(b2) * h2( b1 - b2 )
    for b1 in range(1, convolved.GetNbinsX() + 1):
        h = 0.0
        for b2 in range(1, convolved.GetNbinsX() + 1):
            diff = b1 - b2
            if diff >= 1 and diff <= convolved.GetNbinsX():
                survivalFactor = 1.0#rejection. ??
                h = h + spectra1.GetBinContent(b2) * spectra2.GetBinContent(diff) * survivalFactor
        convolved.SetBinContent(b1, h)
    return convolved

def activity(bg1, bg2, bg3, pileup_window):
    """ Calculate the pileup activity of 1 + 2 + [3] in the window specified."""
    if bg3 is None:
        activity_in_sec = bg2.GetSumOfWeights() / constants.year_in_sec
        return bg1.GetSumOfWeights() * math_util.poisson(activity_in_sec * pileup_window * constants.ns, 1)
    elif bg2.GetName() == bg3.GetName(): 
        activity_in_sec = bg2.GetSumOfWeights() / constants.year_in_sec
        return bg1.GetSumOfWeights() * math_util.poisson(activity_in_sec * pileup_window * constants.ns, 2)
    else:
        activity2_in_sec = bg2.GetSumOfWeights() / constants.year_in_sec
        activity3_in_sec = bg2.GetSumOfWeights() / constants.year_in_sec
        return bg1.GetSumOfWeights() * math_util.poisson(activity2_in_sec * pileup_window * constants.ns, 1) \
            * math_util.poisson(activity3_in_sec * pileup_window * constants.ns, 1)

def spectra(bg1, bg2, bg3, activity, rejection):
    """ Return the pileup spectra of 1 + 2 + [3] with the activity specified given the rejection."""
    name = bg1.GetName() + "+" + bg2.GetName()
    spectra1 = spectrum_util.flattern(_new_spectra(bg1))
    spectra2 = spectrum_util.flattern(_new_spectra(bg2))
    convolved = _convolve_reject(spectra1, spectra2, rejection)
    if bg3 is not None:
        spectra3 = spectrum_util.flattern(_new_spectra(bg3))
        convolved = _convolve_reject(convolved, spectra3, rejection)
        name = name + "+" + bg3.GetName()
    convolved.Scale(activity / convolved.GetSumOfWeights())
    result = spectrum_util.apply_radial_spectrum(convolved, spectrum_util.internal(6000.0)) #Need to think about radial dependence
    result.SetName(name)
    return result
