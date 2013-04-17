#!/usr/bin/env python
#
# te_backgrounds.py
#
# Generators for backgrounds introduced with neodymium
#
# Author P G Jones - 17/04/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import radioactive_gen
import decay_util

class Gen130Te0v(radioactive_gen.DoubleBetaGen):
    """ Tellurium 130 background definition."""
    def __init__(self):
        # Kolita limit, conservative Dueck IBM and Klapdor claim mass
        super(Gen130Te0v, self).__init__("130Te0v", 130, 2.22e-14, 3.4, 320e-3)
    def _generate(self):
        spectrum = decay_util.neutrinoless_double_beta(2.5303, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum
