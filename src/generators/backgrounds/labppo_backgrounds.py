#!/usr/bin/env python
#
# labppo_backgrounds.py
#
# The backgrounds present in labppo.
#
# Author P G Jones - 22/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import radioactive_gen
import decay_util

class Gen14C(radioactive_gen.RadioactiveGen):
    """ Carbon 14 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=60014
    def __init__(self):
        super(Gen14C, self).__init__("14C", 14, 5730)
    def _generate(self):
        spectrum = decay_util.beta(0.156, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen40K(radioactive_gen.RadioactiveGen):
    """ Potassium 40 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=190040
    def __init__(self):
        super(Gen40K, self).__init__("40K", 40, 1.277e9)
    def _generate(self):
        spectrum = decay_util.beta(1.311, 0.8928)
        spectrum.Add(decay_util.gamma(1.460, 0.1067))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen39Ar(radioactive_gen.RadioactiveGen):
    """ Argon 39 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=180039
    def __init__(self):
        super(Gen39Ar, self).__init__("39Ar", 39, 269)
    def _generate(self):
        spectrum = decay_util.beta(0.565, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen85Kr(radioactive_gen.RadioactiveGen):
    """ Krypton 85 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=360085
    def __init__(self):
        super(Gen85Kr, self).__init__("85Kr", 85, 10.756)
    def _generate(self):
        spectrum = decay_util.beta(0.687, 0.996)
        spectrum.Add(decay_util.beta_gamma(0.173, 0.514, 0.004))
        spectrum.SetName(self.get_name())
        return spectrum
