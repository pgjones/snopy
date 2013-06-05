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

class Gen232Th(chain_gen.ChainGen):
    """ Thorium 232 background definition."""
    def __init__(self):
        super(Gen232Th, self).__init__("232Th", 
                                       232, 
                                       1.405e10,
                                       { "228Ra" : 1.0, # Decay daughters
                                         "228Ac" : 1.0,
                                         "228Th" : 1.0,
                                         "224Ra" : 1.0,
                                         "220Rn" : 1.0,
                                         "216Po" : 1.0,
                                         "212Pb" : 1.0,
                                         "212Bi" : 1.0,
                                         "212Po" : 0.64,
                                         "208Tl" : 0.36 })

    def _generate(self):
        spectrum = decay_util.alpha(4.082, 0.779)
        spectrum.Add(decay_util.alpha_gamma(4.018, 0.064, 0.221))
        spectrum.SetName(self.get_name())
        return spectrum
    
class Gen228Ra(radioactive_gen.RadioactiveGen):
    """ Radium 228 background definition."""
    def __init__(self):
        super(Gen228Ra, self).__init__("228Ra", 228, 5.75)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.039, 0.007, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen228Ac(radioactive_gen.RadioactiveGen):
    """ Actinium 228 background definition."""
    def __init__(self):
        super(Gen228Ac, self).__init__("228Ac", 228, 7e-4)
    def _generate(self):
        spectrum = decay_util.beta_gamma(1.158, 0.969, 0.31)
        spectrum.Add(decay_util.beta_gamma(1.758, 0.396, 0.116))
        spectrum.Add(decay_util.beta_gamma(2.069, 0.058, 0.1))
        spectrum.Add(decay_util.beta_gamma(0.959, 1.168, 0.035))
        spectrum.Add(decay_util.beta_gamma(0.973, 1.154, 0.056))
        spectrum.Add(decay_util.beta_gamma(1.005, 1.122, 0.058))
        spectrum.Add(decay_util.beta_gamma(1.104, 1.023, 0.03))
        spectrum.Add(decay_util.beta_gamma(0.596, 1.532, 0.081))
        spectrum.Add(decay_util.beta_gamma(0.489, 1.638, 0.012))
        spectrum.Add(decay_util.beta_gamma(0.481, 1.646, 0.042))
        spectrum.Add(decay_util.beta_gamma(0.403, 1.724, 0.016))
        spectrum.Add(decay_util.beta_gamma(0.439, 1.688, 0.026))
        spectrum.Add(decay_util.beta_gamma(0.445, 1.682, 0.012))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen228Th(radioactive_gen.RadioactiveGen):
    """ Thorium 228 background definition."""
    def __init__(self):
        super(Gen228Th, self).__init__("228Th", 228, 1.9116)
    def _generate(self):
        spectrum = decay_util.alpha(5.520, 0.711)
        spectrum.Add(decay_util.alpha_gamma(5.436, 0.084, 0.282))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen224Ra(radioactive_gen.RadioactiveGen):
    """ Radium 224 background definition."""
    def __init__(self):
        super(Gen224Ra, self).__init__("224Ra", 224, 1e-2)
    def _generate(self):
        spectrum = decay_util.alpha(5.789, 0.95)
        spectrum.Add(decay_util.alpha_gamma(5.548, 0.241, 0.05))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen220Rn(radioactive_gen.RadioactiveGen):
    """ Radon 220 background definition."""
    def __init__(self):
        super(Gen220Rn, self).__init__("220Rn", 220, 1.8e-6)
    def _generate(self):
        spectrum = decay_util.alpha(6.404, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen216Po(radioactive_gen.RadioactiveGen):
    """ Polonium 216 background definition."""
    def __init__(self):
        super(Gen216Po, self).__init__("216Po", 216, 4.6e-9)
    def _generate(self):
        spectrum = decay_util.alpha(6.906, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen212Pb(radioactive_gen.RadioactiveGen):
    """ Lead 212 background definition."""
    def __init__(self):
        super(Gen212Pb, self).__init__("212Pb", 212, 1.2e-3)
    def _generate(self):
        spectrum = decay_util.beta(0.574, 0.123)
        spectrum.Add(decay_util.beta_gamma(0.335, 0.239, 0.825))
        spectrum.Add(decay_util.beta_gamma(0.159, 0.415, 0.05))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen212Bi(radioactive_gen.RadioactiveGen):
    """ Bismuth 212 background definition."""
    def __init__(self):
        super(Gen212Bi, self).__init__("212Bi", 212, 1.2e-4)
    def _generate(self):
        spectrum = decay_util.beta(2.254, 0.555)
        spectrum.Add(decay_util.beta_gamma(1.527, 0.727, 0.04))
        spectrum.Add(decay_util.beta_gamma(0.741, 1.513, 0.014))
        spectrum.Add(decay_util.beta_gamma(0.633, 1.621, 0.019))
        spectrum.Add(decay_util.alpha_gamma(6.167, 0.04, 0.25))
        spectrum.Add(decay_util.alpha(6.207, 0.0975))
        spectrum.SetName(self.get_name())
        return spectrum

class Gen212Po(radioactive_gen.RadioactiveGen):
    """ Polonium 212 background definition."""
    def __init__(self):
        super(Gen212Po, self).__init__("212Po", 212, 9.5e-15)
    def _generate(self):
        spectrum = decay_util.alpha(8.954, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum

class Gen208Tl(radioactive_gen.RadioactiveGen):
    """ Thalium 208 background definition."""
    def __init__(self):
        super(Gen208Tl, self).__init__("208Tl", 208, 5.8e-6)
    def _generate(self):
        spectrum = decay_util.beta_gamma(1.293, 3.708, 0.245)
        spectrum.Add(decay_util.beta_gamma(1.526, 3.475, 0.218))
        spectrum.Add(decay_util.beta_gamma(1.803, 3.198, 0.487))
        spectrum.SetName(self.get_name())
        return spectrum
