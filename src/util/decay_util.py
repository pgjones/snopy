#!/usr/bin/env python
#
# decay_util
#
# The various decay spectra
#
# Author P G Jones - 20/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import constants
import math
import spectrum_util
import alpha_util

def beta_gamma(q_beta, q_gamma, probability):
    """ Return a beta + gamma spectrum of probability."""
    spectrum = beta(q_beta, probability)
    return coincident_gamma(spectrum, q_gamma, 1.0) # Always a gamma with the beta

def alpha_gamma(q_alpha, q_gamma, probability):
    """ Return a alpha + gamma spectrum of probability."""
    spectrum = alpha(q_alpha, probability)
    return coincident_gamma(spectrum, q_gamma, 1.0) # Always a gamma with the alpha

def beta(q_beta, probability):
    """ Return a beta spectrum of probability."""
    spectrum = spectrum_util.default_energy()
    for energy_bin in range(1, spectrum.GetNbinsX() + 1):
        T = spectrum.GetBinCenter(energy_bin)
        Ne = 0
        if T <= q_beta + spectrum.GetBinWidth(energy_bin):
            bin_fraction = 1.0 # Fraction of bin to fill
            if T > q_beta: # Allow for bin widths
                bin_fraction = 1.0 - (T - q_beta) / spectrum.GetBinWidth(energy_bin)
                T = q_beta
            Ne = bin_fraction * math.sqrt(T**2 + 2 * T * constants.me) * (q_beta - T)**2 * (T + constants.me)
        spectrum.SetBinContent(energy_bin, Ne)
    spectrum.Scale(probability / spectrum.GetSumOfWeights())
    return spectrum

def beta_plus(q_beta, probability):
    """ Return a beta plus spectrum."""
    spectrum = beta(q_beta, probability)
    return conincident_gamma(spectrum, 1.022, 1.0) # Always annihilation gammas

def double_beta(q, probability):
    """ Return a double beta spectrum of probability."""
    spectrum = spectrum_util.default_energy()
    q = q / constants.me
    for energy_bin in range(1, spectrum.GetNbinsX() + 1):
        T = spectrum.GetBinCenter(energy_bin)
        T = T / constants.me
        Ne = 0
        if T <= q + spectrum.GetBinWidth(energy_bin):
            binFraction = 1.0 # Fraction of bin to fill
            if T > q: # Allow for bin widths
                binFraction = 1.0 - (T - q) / spectrum.GetBinWidth(energy_bin)
                T = q
            Ne = binFraction * T * (q - T)**5 * (1 + 2 * T + 4 * T**2 / 3 + T**3 / 3 + T**4 / 30)
        spectrum.SetBinContent(energy_bin, Ne)
    spectrum.Scale(probability / spectrum.GetSumOfWeights())
    return spectrum

def alpha(q_alpha, probability):
    """ Return an alpha spectrum of probability."""
    q_alpha = q_alpha / alpha_util.quenching_factor(q_alpha) # Quench the alpha energy
    spectrum = spectrum_util.default_energy()
    for energy_bin in range(1, spectrum.GetNbinsX() + 1):
        T = spectrum.GetBinCenter(energy_bin)
        Ne = 0
        # Delta function at end point
        if math.fabs(T - q_alpha) < spectrum.GetBinWidth(energy_bin):
            Ne = 1
        spectrum.SetBinContent(energy_bin, Ne)
    spectrum.Scale(probability / spectrum.GetSumOfWeights())
    return spectrum

def gamma(q_gamma, probability):
    """ Return a gamma spectrum of probability."""
    spectrum = spectrum_util.default_energy()
    for energy_bin in range(1, spectrum.GetNbinsX() + 1):
        T = spectrum.GetBinCenter(energy_bin)
        Ne = 0
        # Delta function at end point
        if math.fabs(T - q_gamma) < spectrum.GetBinWidth(energy_bin):
            Ne = 1
        spectrum.SetBinContent(energy_bin, Ne)
    spectrum.Scale(probability / spectrum.GetSumOfWeights())
    return spectrum

def neutrinoless_double_beta(q, probability):
    """ Return a neutrinoless double beta spectrum of probability."""
    spectrum = spectrum_util.default_energy()
    for energy_bin in range(1, spectrum.GetNbinsX() + 1):
        T = spectrum.GetBinCenter(energy_bin)
        Ne = 0
        # Delta function at end point
        if math.fabs(T - q) < spectrum.GetBinWidth(energy_bin):
            Ne = 1
        spectrum.SetBinContent(energy_bin, Ne)
    spectrum.Scale(probability / spectrum.GetSumOfWeights())
    return spectrum

def coincident_gamma(spectrum, q_gamma, probability):
    """ Shifts the spectrum in the appropriate ways to include the effects of
    coincident gamma emission. As this is indistinguishable."""
    for energy_bin in range(spectrum.GetNbinsX(), 0, -1):
        content = spectrum.GetBinContent(energy_bin)
        energy = spectrum.GetBinCenter(energy_bin)
        # Reduce fraction of events in this bin by 1 - probability
        spectrum.SetBinContent(energy_bin, content * (1.0 - probability))
        new_energy = energy + q_gamma
        new_bin = spectrum.GetXaxis().FindBin(new_energy)
        new_energyLow = spectrum.GetXaxis().GetBinLowEdge(energy_bin) + q_gamma
        new_energyHigh = new_energyLow + spectrum.GetXaxis().GetBinWidth(energy_bin)
        # Now fill correct bins
        high_bin_fraction = (new_energyHigh - spectrum.GetXaxis().GetBinLowEdge(new_bin + 1)) / (new_energyHigh - new_energyLow)
        if high_bin_fraction > 0.0:
            spectrum.SetBinContent(new_bin + 1, 1, spectrum.GetBinContent(new_bin + 1) + content * probability * high_bin_fraction)

        mid_bin_fraction = spectrum.GetXaxis().GetBinWidth(new_bin) / (new_energyHigh - new_energyLow)
        if mid_bin_fraction > 0.0:
            spectrum.SetBinContent(new_bin, 1, spectrum.GetBinContent(new_bin) + content * probability * mid_bin_fraction)

        low_bin_fraction = (spectrum.GetXaxis().GetBinLowEdge(new_bin) - new_energyLow) / (new_energyHigh - new_energyLow)
        if low_bin_fraction > 0.0:
            spectrum.SetBinContent(new_bin - 1, 1, spectrum.GetBinContent(new_bin - 1) + content * probability * low_bin_fraction)
    return spectrum
