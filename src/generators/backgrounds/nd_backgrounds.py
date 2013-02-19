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

class Gen150Nd(radioactive_gen.RadioactiveGen):
    """ Neodymium 150 background definition."""
    def __init__(self):
        super(Gen150Nd, self).__init__("150Nd2v", 150, 9.11e18) # A.W. Thesis
    def _generate(self):
        spectrum = decay_util.double_beta(3.37138, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen144Nd(radioactive_gen.RadioactiveGen):
    """ Neodymium 144 background definition."""
    def __init__(self):
        super(Gen144Nd, self).__init__("144Nd", 144, 2.29e15) # DocDB-507-v2
    def _generate(self):
        spectrum = decay_util.alpha(1.380, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen176Lu(radioactive_gen.RadioactiveGen):
    """ Lutetium 176 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=710176
    def __init__(self):
        super(Gen176Lu, self).__init__("176Lu", 176, 3.78e10)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.194, 0.998, 0.0034)
        spectrum.Add(decay_util.beta_gamma(0.595, 0.597, 0.9966))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen138La(radioactive_gen.RadioactiveGen):
    """ Lanthanium 138 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=570138
    def __init__(self):
        super(Gen138La, self).__init__("138La", 138, 1.05e11)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.255, 0.789, 0.336)
        spectrum.Add(decay_util.gamma(1.436, 0.664))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen147Sm(radioactive_gen.RadioactiveGen):
    """ Samarium 147 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=620147
    def __init__(self):
        super(Gen147Sm, self).__init__("147Sm", 147, 1.06e11)
    def _generate(self):
        spectrum = decay_util.alpha(2.310, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen148Sm(radioactive_gen.RadioactiveGen):
    """ Samarium 148 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=620148
    def __init__(self):
        super(Gen148Sm, self).__init__("148Sm", 148, 7e15)
    def _generate(self):
        spectrum = decay_util.alpha(1.986, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen227Ac(radioactive_gen.RadioactiveGen):
    """ Actinium 227 background definition."""
    # 
    def __init__(self):
        super(Gen227Ac, self).__init__("227Ac", 227, 2.1e1)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.0203, 0.0245, 0.10)
        spectrum.Add(decay_util.beta_gamma(0.0355, 0.0093, 0.35))
        spectrum.Add(decay_util.beta(0.0448, 0.54))
        spectrum.Add(decay_util.alpha(5.042, 0.014))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen235U(radioactive_gen.RadioactiveGen):
    """ Uranium 235 background definition."""
    # 
    def __init__(self):
        super(Gen235U, self).__init__("235U", 235, 7.03e8)
    def _generate(self):
        spectrum = decay_util.alpha_gamma(4.291, 0.3878, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum
