#!/usr/bin/env python
#
#cosmic_te .py
#
# Generators for backgrounds introduced with teluriumium
#
# Author P G Jones, E Arushanova  - 20/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import cosmogenic_gen
import decay_util


class Gen60Co(cosmogenic_gen.CosmogenicGen):
    """ Cobalt 60 background definition."""
    def __init__(self):
        super(Gen60Co, self).__init__("60Co")
    def _generate(self):
        spectrum = decay_util.beta(0.3182, 0.9988)
        spectrum.Add(decay_util.gamma(1.173228, 0.9985))  
        spectrum.Add(decay_util.gamma(1.332492, 0.999826))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen124Sb(cosmogenic_gen.CosmogenicGen):
    """ Antimony 124 background definition."""
    def __init__(self):
        super(Gen124Sb, self).__init__("124Sb")
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


class Gen127Sb(cosmogenic_gen.CosmogenicGen):
    """ Antimony 127 background definition."""
    def __init__(self):
        super(Gen127Sb, self).__init__("127Sb")
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.440, 1.141, 0.0155)
        spectrum.Add(decay_util.beta_gamma(0.504, 1.077, 0.054))
        spectrum.Add(decay_util.beta_gamma(0.657, 0.924, 0.013))
        spectrum.Add(decay_util.beta_gamma(0.796, 0.785, 0.045))
        spectrum.Add(decay_util.beta_gamma(0.798, 0.783, 0.18))
        spectrum.Add(decay_util.beta_gamma(0.896, 0.685, 0.358))
        spectrum.Add(decay_util.beta_gamma(0.950, 0.631, 0.046))
        spectrum.Add(decay_util.beta_gamma(1.108, 0.473, 0.234))
        spectrum.Add(decay_util.beta_gamma(1.241, 0.340, 0.017))
        spectrum.Add(decay_util.beta_gamma(1.493, 0.088, 0.02))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen126mSb(cosmogenic_gen.CosmogenicGen):
    """ Antimony 126m background definition."""
    def __init__(self):
        super(Gen126mSb, self).__init__("126mSb")
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.99, 2.683, 0.013)
        spectrum.Add(decay_util.beta_gamma(1.3, 2.373, 0.034))
        spectrum.Add(decay_util.beta_gamma(1.92, 1.753, 0.83))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen126Sb(cosmogenic_gen.CosmogenicGen):
    """ Antimony 126 background definition."""
    def __init__(self):
        super(Gen126Sb, self).__init__("126Sb")
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


class Gen22Na(cosmogenic_gen.CosmogenicGen):
    """ Natrium 22 background definition."""
    def __init__(self):
        super(Gen22Na, self).__init__("22Na")
    def _generate(self):
        spectrum = decay_util.beta(1.274537, 0.99941)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen44Sc(cosmogenic_gen.CosmogenicGen):   
    """ Scandium 44 background definition."""
    def __init__(self):
        super(Gen44Sc, self).__init__("44Sc")
    def _generate(self):
        spectrum = decay_util.gamma(1.15702, 0.999)  
        spectrum.SetName(self.get_name())
        return spectrum


class Gen46Sc(cosmogenic_gen.CosmogenicGen):
    """ Scandium 46 background definition."""
    def __init__(self):
        super(Gen46Sc, self).__init__("46Sc")
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.3569, 2.0098, 0.999964)  
        spectrum.SetName(self.get_name())
        return spectrum


class Gen68Ga(cosmogenic_gen.CosmogenicGen):
    """ Gallium 68 background definition."""
    def __init__(self):
        super(Gen68Ga, self).__init__("68Ga")
    def _generate(self):
        spectrum = decay_util.gamma(1.07734,0.0322)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen26Al(cosmogenic_gen.CosmogenicGen):    
    """ Aluminium 26 background definition."""
    def __init__(self):
        super(Gen26Al, self).__init__("26Al")
    def _generate(self):
        spectrum = decay_util.gamma(1.17342,0.8173)
        spectrum.SetName(self.get_name())
        return spectrum
        

class Gen56Co(cosmogenic_gen.CosmogenicGen):  
    """ Cobalt 56 background definition."""
    def __init__(self):
        super(Gen56Co, self).__init__("56Co")
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


class Gen58Co(cosmogenic_gen.CosmogenicGen):    
    """ Cobalt 58 background definition."""
    def __init__(self):
        super(Gen58Co, self).__init__("58Co")
    def _generate(self):
        spectrum = decay_util.gamma(0.8107593, 0.9945)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen42K(cosmogenic_gen.CosmogenicGen):
    """ Potassium 42 background definition."""
    def __init__(self):
        super(Gen42K, self).__init__("42K")
    def _generate(self):
        spectrum = decay_util.beta_gamma(2.0008, 1.52465, 0.1764)
        spectrum.Add(decay_util.beta_gamma(3.5254, 0.0, 0.819))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen82Rb(cosmogenic_gen.CosmogenicGen):
    """ Rubidium 82 background definition."""
    def __init__(self):
        super(Gen82Rb, self).__init__("82Rb")
    def _generate(self):
        spectrum = decay_util.gamma(0.77652, 0.1508)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen84Rb(cosmogenic_gen.CosmogenicGen):
    """ Rubidium 84 background definition."""
    def __init__(self):
        super(Gen84Rb, self).__init__("84Rb")
    def _generate(self):
        spectrum = decay_util.beta(0.896, 0.039)
        spectrum.Add(decay_util.gamma(0.8816041, 0.689 ))  
        spectrum.SetName(self.get_name())
        return spectrum


class Gen90Y(cosmogenic_gen.CosmogenicGen):
    """ Yttrium 90 background definition."""
    def __init__(self):
        super(Gen90Y, self).__init__("90Y")
    def _generate(self):
        spectrum = decay_util.beta(2.2801, 0.999885) 
        spectrum.SetName(self.get_name())
        return spectrum


class Gen88Y(cosmogenic_gen.CosmogenicGen):
    """ Yttrium 88 background definition."""
    def __init__(self):
        super(Gen88Y, self).__init__("88Y")
    def _generate(self):
        spectrum = decay_util.gamma(0.898042, 0.937) 
        spectrum.Add(decay_util.gamma(1.836063, 0.992 ))  
        spectrum.SetName(self.get_name())
        return spectrum


class Gen102Rh(cosmogenic_gen.CosmogenicGen):
    """ Rhodium 102 background definition."""
    def __init__(self):
        super(Gen102Rh, self).__init__("102Rh")
    def _generate(self):
        spectrum = decay_util.beta(0.593, 0.02) 
        spectrum.Add(decay_util.beta(1.150, 0.2)) 
        spectrum.Add(decay_util.gamma(0.5566, 0.02))
        spectrum.Add(decay_util.gamma(0.46858, 0.029))
        spectrum.Add(decay_util.gamma(0.47506, 0.46))
        spectrum.Add(decay_util.gamma(0.62805, 0.045))
        spectrum.Add(decay_util.gamma(1.10316, 0.029))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen102mRh(cosmogenic_gen.CosmogenicGen): 
    """ Rhodium 102m background definition."""
    def __init__(self):
        super(Gen102mRh, self).__init__("102mRh")
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


class Gen106Rh(cosmogenic_gen.CosmogenicGen):
    """ Rhodium 106 background definition."""
    def __init__(self):
        super(Gen106Rh, self).__init__("106Rh")
    def _generate(self):
        spectrum = decay_util.beta_gamma(1.979, 1.562, 0.0177)
        spectrum.Add(decay_util.beta_gamma(2.407, 1.134, 0.1))
        spectrum.Add(decay_util.beta_gamma(3.029, 0.512, 0.081))
        spectrum.Add(decay_util.beta(3.541, 0.786))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen110mAg(cosmogenic_gen.CosmogenicGen):     
    """ Argentum 110m background definition."""     
    def __init__(self):
        super(Gen110mAg, self).__init__("110mAg")
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.083, 2.8092, 0.686)
        spectrum.Add(decay_util.beta_gamma(0.5306, 2.3623, 0.313))
        spectrum.SetName(self.get_name())
        return spectrum


class Gen125I(cosmogenic_gen.CosmogenicGen):    
    """ Iodine 125 background definition."""     
    def __init__(self):
        super(Gen125I, self).__init__("125I")
    def _generate(self):
        spectrum = decay_util.gamma(0.0354925, 0.0668)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen129I(cosmogenic_gen.CosmogenicGen):     
    """ Iodine 129 background definition."""     
    def __init__(self):
        super(Gen129I, self).__init__("129I")
    def _generate(self):
        spectrum = decay_util.beta_gamma(0.154, 0.039578, 1.0)
        spectrum.SetName(self.get_name())
        return spectrum


class Gen121mTe(cosmogenic_gen.CosmogenicGen):     
    """ Tellurium 121m background definition."""     
    def __init__(self):
        super(Gen121mTe, self).__init__("121mTe")
    def _generate(self):
        spectrum = decay_util.gamma(1.102149, 0.025)
        spectrum.Add(decay_util.gamma(0.212189, 0.815))
        spectrum.SetName(self.get_name())
        return spectrum
