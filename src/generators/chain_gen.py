#!/usr/bin/env python
#
# ChainGen
#
# Base class for generating radioactive backgrounds that form chains
#
# Author P G Jones - 06/05/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import generator
import generators
import math
import constants

class ChainGen(generator.Generator):
    """ Base class for generating radioactive chain decay spectra."""
    def __init__(self, name, atomic_mass, half_life, chain):
        """ Initialise with an unique name."""
        super(ChainGen, self).__init__(name)
        self._atomic_mass = atomic_mass
        self._half_life = half_life
        self._chain = chain
    def generate(self, mass):
        """ Return a energy spectrum for this decay and the daughter decays."""
        spectrum = self._generate()
        for bg in self._chain.keys():
            bg_spectrum = generators.generators[bg]._generate()
            bg_spectrum.Scale(self._chain[bg])
            spectrum.Add(bg_spectrum)
        spectrum.Scale(self.get_activity(mass))
        return spectrum
    def get_activity(self, mass):
        """ Return the activity per year given the mass of this background/signal."""
        return mass * math.log(2) / ( constants.U * self._atomic_mass * self._half_life )
####################################################################################################
# Functions to override
    def _generate(self):
        """ Generate the spectrum as a function of energy and radius, normalised to one event."""
        pass
