#!/usr/bin/env python
#
# TeDataGen
#
# Generates a full raw data set for Te loaded scintillator
#
# Author P G Jones - 05/06/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import generators
import data_set
import spectrum_util

class TeDataGen(object):
    """ Generates a full raw data set for Te loaded scintillator."""
    def __init__(self, scint_mass, loading):
        """ Initialise the target fractions dict, etc..."""
        self._signal_fraction = 0.0
        self._te_fractions = { "130Te2v" : 0.0 }
        self._scint_fractions = { "14C" : 1e-18,
                                  "40K" : 1.3e-18,
                                  "39Ar" : 2.75e-24,
                                  "85Kr" : 2.4e-25 }
        self._solar_backgrounds = [ "PEP", "CNO", "B8", "Be7" ]
        self._loading = loading
        self._scint_mass = scint_mass
        self._te_mass = loading / 100.0 * scint_mass
        self._radius = 6000.0
    def set_scint_fraction(self, isotope, fraction):
        """ Set the fraction of an isotope in the scintillator."""
        if isotope in self._fractions:
            self._fractions[isotope] = fraction
        else:
            raise("Isotope not part of the Te set.")
    def set_te_fraction(self, isotope, fraction):
        """ Set the fraction of an isotope in the Te."""
        if isotope in self._te_fractions:
            self._te_fractions[isotope] = fraction
        else:
            raise("Isotope not part of the Te set.")
    def generate(self):
        """ Generate a raw data set for Te loaded scintillator."""
        gen_set = data_set.RawDataSet("Te%d" % self._loading)
        # Scintillator backgrounds
        for isotope, fraction in self._scint_fractions.iteritems():
            energy_spectrum = generators.generators[isotope].generate(self._scint_mass * fraction)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)
        # Now Isotope backgrounds
        for isotope, fraction in self._te_fractions.iteritems():
            energy_spectrum = generators.generators[isotope].generate(self._te_mass * fraction)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)
        # Now Solar backgrounds
        for isotope in self._solar_backgrounds:
            energy_spectrum = generators.generators[isotope].generate(self._scint_mass)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)
        # Now the signal
        signal_energy_spectrum = generators.generators["130Te0v"].generate(self._te_mass * \
                                                                               self._signal_fraction)
        spectrum = spectrum_util.apply_radial_spectrum(signal_energy_spectrum, 
                                                       spectrum_util.internal(self._radius))
        gen_set.set_signal(spectrum)
        return gen_set
####################################################################################################
