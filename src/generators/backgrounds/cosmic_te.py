#!/usr/bin/env python
#
# te_backgrounds.py
#
# Generators for backgrounds introduced with teluriumium
#
# Author P G Jones - 20/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import radioactive_gen
import decay_util


class Gen60Co(radioactive_gen.RadioactiveGen):
    """ Cobalt 60 background definition."""
    def __init__(self):
        super(Gen60Co, self).__init__("60Co", 60, 5.272)
    def _generate(self):
        spectrum = decay_util.beta(0.3182, 0.9988)
        spectrum.Add(decay_util.gamma(1.173228, 0.9985))  
        spectrum.Add(decay_util.gamma(1.332492, 0.999826))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen124Sb(radioactive_gen.RadioactiveGen):
    """ Antimony 124 background definition."""
    def __init__(self):
        super(Gen124Sb, self).__init__("124Sb", 124, 0.1649)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.2106, 2.6937, 0.0875)
        spectrum.Add(decay_util.beta_gamma(0.6106, 2.2937, 0.5124))
        spectrum.Add(decay_util.beta_gamma(0.865, 2.039, 0.03994))
        spectrum.Add(decay_util.beta_gamma(0.9464, 1.9579, 0.02144))
        spectrum.Add(decay_util.beta_gamma(1.5788, 1.3225, 0.0488))
        spectrum.Add(decay_util.beta_gamma(1.6557, 1.2486, 0.0257))
        spectrum.Add(decay_util.beta_gamma(2.3016, 0.6027, 0.232))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen126mSb(radioactive_gen.RadioactiveGen):
    """ Antimony 126m background definition."""
    def __init__(self):
        super(Gen126mSb, self).__init__("126mSb", 126, 0.00003643)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.99, 2.683, 0.013)
        spectrum.Add(decay_util.beta_gamma(1.3, 2.373, 0.034))
        spectrum.Add(decay_util.beta_gamma(1.92, 1.753, 0.83))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen126Sb(radioactive_gen.RadioactiveGen):
    """ Antimony 126 background definition."""
    def __init__(self):
        super(Gen126Sb, self).__init__("126Sb", 126, 0.03384)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.22, 3.45,  0.0209)
        spectrum.Add(decay_util.beta_gamma(0.48, 3.193,  0.29))
        spectrum.Add(decay_util.beta_gamma(0.5, 3.173,  0.059))
        spectrum.Add(decay_util.beta_gamma(0.6, 3.073,  0.084))
        spectrum.Add(decay_util.beta_gamma(0.68, 2.993,  0.042))
        spectrum.Add(decay_util.beta_gamma(0.86, 2.813,  0.081))
        spectrum.Add(decay_util.beta_gamma(0.91, 2.763,  0.049))
        spectrum.Add(decay_util.beta_gamma(1.18, 2.493,  0.16))
        spectrum.Add(decay_util.beta_gamma(1.45, 2.2233,  0.03))
        spectrum.Add(decay_util.beta_gamma(1.9, 1.773,  0.2))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen22Na(radioactive_gen.RadioactiveGen):
    """ Natrium 22 background definition."""
    def __init__(self):
        super(Gen22Na, self).__init__("22Na", 22, 2.602)
    def _generate(self):
        spectrum = decay_util.beta(1.274537, 0.99941)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen44Sc(radioactive_gen.RadioactiveGen):   
    """ Scandium 44 background definition."""
    def __init__(self):
        super(Gen44Sc, self).__init__("44Sc", 44, 0.0004532)
    def _generate(self):
        spectrum = decay_util.gamma(1.15702, 0.999)  
        spectrum.SetName(self.get_name())
        return spectrum


class Gen46Sc(radioactive_gen.RadioactiveGen):
    """ Scandium 46 background definition."""
    def __init__(self):
        super(Gen46Sc, self).__init__("46Sc", 46, 0.23)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.3569, 2.0098, 0.999964)  
        spectrum.SetName(self.get_name())
        return spectrum


class Gen68Ga(radioactive_gen.RadioactiveGen):
    """ Gallium 68 background definition."""
    def __init__(self):
        super(Gen68Ga, self).__init__("68Ga", 68, 0.00012867)
    def _generate(self):
        spectrum = decay_util.gamma(1.07734,0.0322)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen26Al(radioactive_gen.RadioactiveGen):    
    """ Aluminium 26 background definition."""
    def __init__(self):
        super(Gen26Al, self).__init__("26Al", 26, 7.166e5)
    def _generate(self):
        spectrum = decay_util.gamma(1.17342,0.8173)
        spectrum.SetName(self.get_name())
        return spectrum
        

class Gen56Co(radioactive_gen.RadioactiveGen):  
    """ Cobalt 56 background definition."""
    def __init__(self):
        super(Gen56Co, self).__init__("56Co", 56, 0.212)
    def _generate(self):
        spectrum = decay_util.gamma(0.84677, 0.999399)
        spectrum.Add(decay_util.gamma(0.977372, 0.01421))
        spectrum.Add(decay_util.gamma(1.037843, 0.1405))
        spectrum.Add(decay_util.gamma(1.175101, 0.02252))
        spectrum.Add(decay_util.gamma(1.238288, 0.6646))
        spectrum.Add(decay_util.gamma(1.360212, 0.04283))
        spectrum.Add(decay_util.gamma(1.771357, 0.1541))
        spectrum.Add(decay_util.gamma(2.015215, 0.03016))
        spectrum.Add(decay_util.gamma(2.034791, 0.0777))
        spectrum.Add(decay_util.gamma(2.5985, 0.1697))
        spectrum.Add(decay_util.gamma(3.009645, 0.01036))
        spectrum.Add(decay_util.gamma(3.202029, 0.03209))
        spectrum.Add(decay_util.gamma(3.253503, 0.07923))
        spectrum.Add(decay_util.gamma(3.273079, 0.018759))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen58Co(radioactive_gen.RadioactiveGen):    
    """ Cobalt 58 background definition."""
    def __init__(self):
        super(Gen58Co, self).__init__("58Co", 58, 0.194)
    def _generate(self):
        spectrum = decay_util.gamma(0.8107593, 0.9945)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen42K(radioactive_gen.RadioactiveGen):
    """ Potassium 42 background definition."""
    def __init__(self):
        super(Gen42K, self).__init__("42K", 42, 0.00141096)
    def _generate(self):
        spectrum = decay_util.beta_gamma(2.0008, 1.52465, 0.1764)
        spectrum.Add(decay_util.beta_gamma(3.5254, 0.0, 0.819))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen82Rb(radioactive_gen.RadioactiveGen):
    """ Rubidium 82 background definition."""
    def __init__(self):
        super(Gen82Rb, self).__init__("82Rb", 82, 0.00000242)
    def _generate(self):
        spectrum = decay_util.gamma(0.77652, 0.1508)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen84Rb(radioactive_gen.RadioactiveGen):
    """ Rubidium 84 background definition."""
    def __init__(self):
        super(Gen84Rb, self).__init__("84Rb", 84, 0.089)
    def _generate(self):
        spectrum = decay_util.beta(0.896, 0.039)
        spectrum.Add(decay_util.gamma(0.8816041, 0.689 ))  
        spectrum.SetName(self.get_name())
        return spectrum


class Gen90Y(radioactive_gen.RadioactiveGen):
    """ Ytrium 90 background definition."""
    def __init__(self):
        super(Gen90Y, self).__init__("90Y", 90, 0.0073)
    def _generate(self):
        spectrum = decay_util.beta(2.2801, 0.999885) 
        spectrum.SetName(self.get_name())
        return spectrum


class Gen102Rh(radioactive_gen.RadioactiveGen):   
    """ Rhodium 102 background definition."""
    def __init__(self):
        super(Gen102Rh, self).__init__("102Rh", 102, 0.5679)
    def _generate(self):
        spectrum = decay_util.beta(1.150, 0.2)
        spectrum.Add(decay_util.beta_gamma(0.593, 0.557, 0.02)) 
        spectrum.Add(decay_util.gamma(0.46858, 0.029))
        spectrum.Add(decay_util.gamma(0.47506, 0.46))
        spectrum.Add(decay_util.gamma(0.62805, 0.045))
        spectrum.Add(decay_util.gamma(1.10316, 0.029))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen102mRh(radioactive_gen.RadioactiveGen): 
    """ Rhodium 102m background definition."""
    def __init__(self):
        super(Gen102mRh, self).__init__("102mRh", 102, 2.9)
    def _generate(self):
        spectrum = decay_util.gamma(0.41525, 0.021)
        spectrum.Add(decay_util.gamma(0.41852, 0.094))
        spectrum.Add(decay_util.gamma(0.4204, 0.032))
        spectrum.Add(decay_util.gamma(0.47506, 0.95))
        spectrum.Add(decay_util.gamma(0.62805, 0.083))
        spectrum.Add(decay_util.gamma(0.63129, 0.56))
        spectrum.Add(decay_util.gamma(0.6924, 0.016))
        spectrum.Add(decay_util.gamma(0.6956, 0.029))
        spectrum.Add(decay_util.gamma(0.69749, 0.44))
        spectrum.Add(decay_util.gamma(0.76684, 0.34))
        spectrum.Add(decay_util.gamma(1.04659, 0.34))
        spectrum.Add(decay_util.gamma(1.10316, 0.046))
        spectrum.Add(decay_util.gamma(1.11284, 0.19))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen106Rh(radioactive_gen.RadioactiveGen):
    """ Rhodium 106 background definition."""
    def __init__(self):
        super(Gen106Rh, self).__init__("106Rh", 106, 0.00000094)
    def _generate(self):
        spectrum = decay_util.beta_gamma(1.979, 1.562, 0.0177)
        spectrum.Add(decay_util.beta_gamma(2.407, 1.134, 0.1))
        spectrum.Add(decay_util.beta_gamma(3.029, 0.512, 0.081))
        spectrum.Add(decay_util.beta(3.541, 0.786))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen110mAg(radioactive_gen.RadioactiveGen):     
    """ Argentum 110m background definition."""     
    def __init__(self):
        super(Gen110mAg, self).__init__("110mAg", 110, 0.6845)
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.083, 2.8092, 0.686)
        spectrum.Add(decay_util.beta_gamma(0.5306, 2.3623, 0.313))
        spectrum.SetName(self.get_name())
        return spectrum
