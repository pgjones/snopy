#!/usr/bin/env python
#
# uranium_backgrounds.py
#
# The backgrounds due to the Uranium chain.
#
# Author P G Jones - 06/05/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import chain_gen
import radioactive_gen
import spectrum_util

class Gen238U(chain_gen.ChainGen):
    """ Uranium 238 background definition."""
    def __init__(self):
        super(Gen238U, self).__init__("238U", 
                                      238, 
                                      4.468e9,
                                      { "234Th" : 1.0, # Decay daughters
                                        "234mPa": 1.0,
                                        "234U"  : 1.0, 
                                        "230Th" : 1.0,
                                        "226Ra" : 1.0,
                                        "222Rn" : 1.0,
                                        "218Po" : 1.0,
                                        "214Pb" : 1.0,
                                        "214Bi" : 1.0,
                                        "214Po" : 1.0 } )
    def _generate(self):
        spectrum = decay_util.alpha_gamma(4.220, 0.0496, 0.209)
        spectrum.Add(decay_util.alpha(4.270, 0.79))
        spectrum.SetName(self.get_name())
        return spectrum
    
class Gen234Th(radioactive_gen.RadioactiveGen):
    """ Thorium 234 background definition."""
    def __init__(self):
        super(Gen234Th, self).__init__("234Th", 234, 6.6e-2)
    def _generate(self):
        spectrum = decay_util.beta(0.273, 0.703)
        spectrum.Add(decay_util.beta_gamma(0.106, 0.166, 0.192))
        spectrum.Add(decay_util.beta_gamma(0.106, 0.167, 0.076))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen234mPa(radioactive_gen.RadioactiveGen):
    """ Protactinium 234 background definition."""
    def __init__(self):
        super(Gen234mPa, self).__init__("234mPa", 234, 6.6e-2)
    def _generate(self):
        spectrum = decay_util.beta(2.197, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen234U(radioactive_gen.RadioactiveGen):
    """ Uranium 234 background definition."""
    def __init__(self):
        super(Gen234U, self).__init__("234U", 234, 2.455e5)
    def _generate(self):
        spectrum = decay_util.alpha(4.858, 0.714)
        spectrum.Add(decay_util.alpha_gamma(4.805, 0.053, 0.284))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen230Th(radioactive_gen.RadioactiveGen):
    """ Thorium 230 background definition."""
    def __init__(self):
        super(Gen230Th, self).__init__("230Th", 230, 7.538e4)
    def _generate(self):
        spectrum = decay_util.alpha(4.770, 0.763)
        spectrum.Add(decay_util.alpha_gamma(4.702, 0.067, 0.234))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen226Ra(radioactive_gen.RadioactiveGen):
    """ Radium 226 background definition."""
    def __init__(self):
        super(Gen226Ra, self).__init__("226Ra", 226, 1600)
    def _generate(self):
        spectrum = decay_util.alpha(4.870, 0.9445)
        spectrum.Add(decay_util.alpha_gamma(4.684, 0.186, 0.056))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen222Rn(radioactive_gen.RadioactiveGen):
    """ Radon 222 background definition."""
    def __init__(self):
        super(Gen222Rn, self).__init__("222Rn", 222, 1e-2)
    def _generate(self):
        spectrum = decay_util.alpha(5.59, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen218Po(radioactive_gen.RadioactiveGen):
    """ Polonium 218 background definition."""
    def __init__(self):
        super(Gen218Po, self).__init__("218Po", 218, 5.9e-6)
    def _generate(self):
        spectrum = decay_util.alpha(6.114, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen214Pb(radioactive_gen.RadioactiveGen):
    """ Lead 214 background definition."""
    def __init__(self):
        super(Gen214Pb, self).__init__("214Pb", 214, 5.1e-5)
    def _generate(self):
        spectrum = decay_util.beta(1.023, 0.093)
        spectrum.Add(decay_util.beta_gamma(0.728, 0.295, 0.405))
        spectrum.Add(decay_util.beta_gamma(0.671, 0.352, 0.46))
        spectrum.Add(decay_util.beta_gamma(0.489, 0.534, 0.01))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen214Bi(radioactive_gen.RadioactiveGen):
    """ Bismuth 214 background definition."""
    def __init__(self):
        super(Gen214Bi, self).__init__("214Bi", 214, 3.8e-5)
    def _generate(self):
        spectrum = decay_util.beta(3.272, 0.199)
        spectrum.Add(decay_util.beta_gamma(1.894, 1.378, 0.072))
        spectrum.Add(decay_util.beta_gamma(1.729, 1.543, 0.03))
        spectrum.Add(decay_util.beta_gamma(1.508, 1.764, 0.169))
        spectrum.Add(decay_util.beta_gamma(1.425, 1.847, 0.083))
        spectrum.Add(decay_util.beta_gamma(1.382, 1.890, 0.016))
        spectrum.Add(decay_util.beta_gamma(1.278, 1.994, 0.014))
        spectrum.Add(decay_util.beta_gamma(1.261, 2.011, 0.017))
        spectrum.Add(decay_util.beta_gamma(1.255, 2.017, 0.029))
        spectrum.Add(decay_util.beta_gamma(1.064, 2.208, 0.055))
        spectrum.Add(decay_util.beta_gamma(1.153, 2.119, 0.041))
        spectrum.Add(decay_util.beta_gamma(0.849, 2.423, 0.027))
        spectrum.Add(decay_util.beta_gamma(0.790, 2.482, 0.015))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen214Po(radioactive_gen.RadioactiveGen):
    """ Polonium 214 background definition."""
    def __init__(self):
        super(Gen214Po, self).__init__("214Po", 214, 5.2e-12)
    def _generate(self):
        spectrum = decay_util.alpha(7.833, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen210Pb(radioactive_gen.RadioactiveGen):
    """ Lead 210 background definition."""
    def __init__(self):
        super(Gen210Pb, self).__init__("210Pb", 210, 22.3)
    def _generate(self):
        spectrum = decay_util.beta(0.064, 0.16)
        spectrum.Add(decay_util.beta_gamma(0.017, 0.047, 0.84))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen210Bi(radioactive_gen.RadioactiveGen):
    """ Bismuth 210 background definition."""
    def __init__(self):
        super(Gen210Bi, self).__init__("210Bi", 210, 1.4e-2)
    def _generate(self):
        spectrum = decay_util.beta(1.162, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen210Po(radioactive_gen.RadioactiveGen):
    """ Polonium 210 background definition."""
    def __init__(self):
        super(Gen210Po, self).__init__("210Po", 210, 0.38)
    def _generate(self):
        spectrum = decay_util.alpha(5.407, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum
