#!/usr/bin/env python
#
# RadioactiveGen
#
# Base class for generating radioactive backgrounds/signals
#
# Author P G Jones - 20/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import generator
import math
import constants

class RadioactiveGen(generator.Generator):
    """ Base class for generating radioactive decay spectra."""
    def __init__(self, name, atomic_mass, half_life):
        """ Initialise with an unique name."""
        super(RadioactiveGen, self).__init__(name)
        self._atomic_mass = atomic_mass
        self._half_life = half_life
    def generate(self, mass):
        """ Return a energy spectrum for this background/signal."""
        spectrum = self._generate()
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

class DoubleBetaGen(RadioactiveGen):
    """ Base class for generating double beta spectra."""
    def __init__(self, name, atomic_mass, G, NME, nu_mass):
        """ Initialise with the double beta parameters."""
        super(DoubleBetaGen, self).__init__(name, atomic_mass, constants.me**2 / ( G * NME**2 * nu_mass**2))
