#!/usr/bin/env python
#
# CosmogenicGen
#
# Base class for generating cosmogenic backgrounds (radioactive generators with rates not mass)
#
# Author P G Jones - 20/06/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import generator
import math
import constants

class CosmogenicGen(generator.Generator):
    """ Base class for generating radioactive decay spectra."""
    def __init__(self, name):
        """ Initialise with an unique name."""
        super(RadioactiveGen, self).__init__(name)
    def generate(self, activity):
        """ Return a energy spectrum for this background/signal."""
        spectrum = self._generate()
        spectrum.Scale(self._activity)
        return spectrum
####################################################################################################
# Functions to override
    def _generate(self):
        """ Generate the spectrum as a function of energy and radius, normalised to one event."""
        pass
