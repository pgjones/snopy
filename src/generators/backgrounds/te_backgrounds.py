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

class Gen130Te(radioactive_gen.RadioactiveGen):
    """ Tellurium 130 background definition."""
    def __init__(self):
        super(Gen130Te, self).__init__("130Te2v", 130, 7e20)
    def _generate(self):
        spectrum = decay_util.double_beta(2.5303, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum
