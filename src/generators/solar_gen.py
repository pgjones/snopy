#!/usr/bin/env python
#
# SolarGen
#
# Base class for generating solar backgrounds/signals
#
# Author P G Jones - 21/02/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import generator
import math
import constants

class SolarGen(generator.Generator):
    """ Base class for generating solar spectra."""
    def __init__(self, name, events_per_Kt_year):
        """ Initialise with an unique name."""
        super(SolarGen, self).__init__(name)
        self._events_per_Kt_year = events_per_Kt_year
    def generate(self, mass):
        """ Return a energy spectrum for this background/signal."""
        spectrum = self._generate()
        spectrum.Scale(self.get_activity(mass))
        return spectrum
    def get_activity(self, mass):
        """ Return the activity per year given the mass of this background/signal."""
        return mass * self._events_per_Kt_year / constants.KgPerKt
####################################################################################################
# Functions to override
    def _generate(self):
        """ Generate the spectrum as a function of energy and radius, normalised to one event."""
        pass
