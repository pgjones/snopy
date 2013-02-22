#!/usr/bin/env python
#
# solar_backgrounds.py
#
# The backgrounds due to solar neutrinos. These have distinct shapes, hard coded in this file.
#
# Author P G Jones - 21/02/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import solar_gen
import spectrum_util

class GenPEP(solar_gen.SolarGen):
    """ PEP neutrino background definition."""
    def __init__(self):
        super(GenPEP, self).__init__("PEP", 10834)
    def _generate(self):
        spectrum = spectrum_util.default_energy()
        for energy_bin in range(1, spectrum.GetNbinsX() + 1):
            T = spectrum.GetBinCenter(energy_bin)
            Ne = 0
            if T <= 1.2 + spectrum.GetBinWidth(energy_bin):
                Ne = 100 - 23.85 * T + 6.84 * T**2
            spectrum.SetBinContent(energy_bin, Ne)
        spectrum.Scale(1.0 / spectrum.GetSumOfWeights())
        spectrum.SetName(self.get_name())
        return spectrum

class GenCNO(solar_gen.SolarGen):
    """ CNO neutrino background definition."""
    def __init__(self):
        super(GenCNO, self).__init__("CNO", 21900)
    def _generate(self):
        spectrum = spectrum_util.default_energy()
        for energy_bin in range(1, spectrum.GetNbinsX() + 1):
            T = spectrum.GetBinCenter(energy_bin)
            Ne = 0
            if T <= 1.0 + spectrum.GetBinWidth(energy_bin):
                Ne = 382.649 - 191.188 * T - 459.082 * T**2 + 307.816 * T**3
            elif T <= 1.5 + spectrum.GetBinWidth(energy_bin):
                Ne = 332.084 - 423.353 * T + 134.585 * T**2
            spectrum.SetBinContent(energy_bin, Ne)
        spectrum.Scale(1.0 / spectrum.GetSumOfWeights())
        spectrum.SetName(self.get_name())
        return spectrum

class GenB8(solar_gen.SolarGen):
    """ B8 neutrino background definition."""
    def __init__(self):
        super(GenB8, self).__init__("B8", 2099)
    def _generate(self):
        spectrum = spectrum_util.default_energy()
        for energy_bin in range(1, spectrum.GetNbinsX() + 1):
            T = spectrum.GetBinCenter(energy_bin)
            Ne = 3.28229 - 0.219904 * T + 0.00981048 * T**2 - 0.0105927 * T**3 + 0.00151589 * T**4 - 7.66537e-05 * T**5 + 1.31912e-06 * T**6
            spectrum.SetBinContent(energy_bin, Ne)
        spectrum.Scale(1.0 / spectrum.GetSumOfWeights())
        spectrum.SetName(self.get_name())
        return spectrum

class GenBe7(solar_gen.SolarGen):
    """ Be7 neutrino background definition."""
    def __init__(self):
        super(GenBe7, self).__init__("Be7", 199913)
    def _generate(self):
        spectrum = spectrum_util.default_energy()
        for energy_bin in range(1, spectrum.GetNbinsX() + 1):
            T = spectrum.GetBinCenter(energy_bin)
            Ne = 0
            if T <= 0.65 + spectrum.GetBinWidth(energy_bin):
                Ne = 3439.38 - 1531.56 * T + 654.453 * T**2
            spectrum.SetBinContent(energy_bin, Ne)
        spectrum.Scale(1.0 / spectrum.GetSumOfWeights())
        spectrum.SetName(self.get_name())
        return spectrum

