#!/usr/bin/env python
#
# RawData
#
# RawData container class
#
# Author P G Jones - 20/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import ROOT

EBins = 2400
ELow = 0.0
EHigh = 24.0
RBins = 100
RLow = 0.0
RHigh = 10000

def apply_radial_spectrum(energy_spectrum, radial_spectrum):
    """ Returns a TH2D given the energy and radial spectra."""
    full_spectrum = default_raw(energy_spectrum.GetName())
    radial_axis = full_spectrum.GetYaxis()
    for bin_energy in range(1, full_spectrum.GetNbinsX() + 1):
        count_energy = energy_spectrum.GetBinContent(bin_energy)
        for bin_radius in range(1, full_spectrum.GetNbinsY() + 1):
            fraction = radial_spectrum.GetBinContent(bin_radius)
            full_spectrum.SetBinContent(bin_energy, bin_radius, count_energy * fraction)
    return full_spectrum

def flattern(full_spectrum):
    """ Remove the radial dependence and return a TH1D energy spectrum."""
    energy_spectrum = default_detected(full_spectrum.GetName())
    for bin_energy in range(1, full_spectrum.GetNbinsX() + 1):
        count = 0.0
        for bin_radius in range(1, full_spectrum.GetNbinsY() + 1):
            count += full_spectrum.GetBinContent(bin_energy, bin_radius)
        energy_spectrum.SetBinContent(bin_energy, count)
    return energy_spectrum

def internal(radius):
    """ Return the standard r^3 internal spectra radial histogram."""
    global RBins, RLow, RHigh
    spectrum = ROOT.TH1D("r^3", "r^3", RBins, RLow, RHigh)
    for iBin in range(1, RBins + 1):
        r = spectrum.GetBinLowEdge(iBin)
        dR = spectrum.GetBinWidth(iBin)
        if r < radius:
            spectrum.SetBinContent(iBin, (dR**3 + 3.0 * dR * r * (r + dR)) / radius**3)
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum

def default_raw(name="Temp"):
    """ Return an empty raw spectrum (TH2D)."""
    global EBins, ELow, EHigh, RBins, RLow, RHigh
    spectrum = ROOT.TH2D(name, name, EBins, ELow, EHigh, RBins, RLow, RHigh)
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum

def default_detected(name="Temp"):
    """ Return an empty detected spectrum (TH1D)."""
    global EBins, ELow, EHigh
    spectrum = ROOT.TH1D(name, name, EBins, ELow, EHigh)
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum

def default_energy(name="Temp"):
    """ Return an empty energy spectrum (TH1D)."""
    global EBins, ELow, EHigh
    spectrum = ROOT.TH1D(name, name, EBins, ELow, EHigh)
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum
