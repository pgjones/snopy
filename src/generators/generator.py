#!/usr/bin/env python
#
# generator.py
#
# Base class for generators
#
# Author P G Jones - 24/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import generator

class Generator(object):
    """ Base class for generator objects."""
    def __init__(self, name):
        """ Initialise with the generator name."""
        self._name = name
    def get_name(self):
        """ Return the generator name."""
        return self._name
