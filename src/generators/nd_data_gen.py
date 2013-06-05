#!/usr/bin/env python
#
# NdDataGen
#
# Generates a full raw data set for Nd loaded scintillator
#
# Author P G Jones - 21/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import generators
import data_set
import spectrum_util

class NdDataGen(object):
    """ Generates a full raw data set for Nd loaded scintillator."""
    def __init__(self, scint_mass, loading):
        """ Initialise the target fractions dict, etc..."""
        self._signal_fraction = 0.056
        self._nd_fractions = { "150Nd2v" : 0.056,
                               "144Nd" : 2.38e-1,
                               "176Lu" : 1.2e-7,
                               "138La" : 5e-7,
                               "147Sm" : 5e-7,
                               "148Sm" : 5e-7,
                               "227Ac" : 1e-18,
                               "235U" : 5e-11,
                               "238U" : 1.0e-15,
                               "232Th" : 1.0e-14}
        self._scint_fractions = { "14C" : 1e-18,
                                  "40K" : 1.3e-18,
                                  "39Ar" : 2.75e-24,
                                  "85Kr" : 2.4e-25,
                                  "238U" : 1.6e-17,
                                  "232Th" : 6.8e-18}
        self._solar_backgrounds = [ "PEP", "CNO", "B8", "Be7" ]
        self._loading = loading
        self._scint_mass = scint_mass
        self._nd_mass = loading / 100.0 * scint_mass
        self._radius = 6000.0
    def set_scint_fraction(self, isotope, fraction):
        """ Set the fraction of an isotope in the scintillator."""
        if isotope in self._fractions:
            self._fractions[isotope] = fraction
        else:
            raise("Isotope not part of the Nd set.")
    def set_nd_fraction(self, isotope, fraction):
        """ Set the fraction of an isotope in the Nd."""
        if isotope in self._nd_fractions:
            self._nd_fractions[isotope] = fraction
        else:
            raise("Isotope not part of the Nd set.")
    def generate(self):
        """ Generate a raw data set for nd loaded scintillator."""
        gen_set = data_set.RawDataSet("Nd%d" % self._loading)
        # Scintillator backgrounds
        for isotope, fraction in self._scint_fractions.iteritems():
            energy_spectrum = generators.generators[isotope].generate(self._scint_mass * fraction)
            # Apply an internal radial dependence
            spectrum = spectrum_util.apply_radial_spectrum(energy_spectrum, 
                                                           spectrum_util.internal(self._radius))
            gen_set.add_background(spectrum)
        # Now Isotope backgrounds
        for isotope, fraction in self._nd_fractions.iteritems():
            energy_spectrum = generators.generators[isotope].generate(self._nd_mass * fraction)
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
        signal_energy_spectrum = generators.generators["150Nd0v"].generate(self._nd_mass * \
                                                                               self._signal_fraction)
        spectrum = spectrum_util.apply_radial_spectrum(signal_energy_spectrum, 
                                                       spectrum_util.internal(self._radius))
        gen_set.set_signal(spectrum)
        return gen_set
####################################################################################################
