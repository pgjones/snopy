#!/usr/bin/env python
#
# nd_backgrounds.py
#
# Generators for backgrounds introduced with neodymium
#
# Author P G Jones - 20/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import radioactive_gen
import decay_util

class Gen150Nd0v(radioactive_gen.DoubleBetaGen):
    """ Neodymium 150 background definition."""
    def __init__(self):
        # Kolita limit, conservative Dueck IBM and Klapdor claim mass
        super(Gen150Nd0v, self).__init__("150Nd0v", 150, 15.4e-14, 2.3, 320e-3)
    def _generate(self):
        spectrum = decay_util.neutrinoless_double_beta(3.37138, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum
