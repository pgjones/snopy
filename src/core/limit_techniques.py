#!/usr/bin/env python
#
# limit_techniques.py
#
# Classes to calculate the limits under differing statistical techniques. Returns a limit.
#
# Author P G Jones - 28/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import ROOT
import math

class TLimit(object):
    """ Calculates limits using the TLimit (CLs) statistical technique."""
    def __init__(self, cl=0.9):
        """ Initialise with signal, summed background and data spectrum."""
        self._cl = cl
    def calculate(self, detected_data_set, data):
        """ Calculate the limit."""
        signal = detected_data_set.get_signal()
        background = detected_data_set.get_summed_background()
        max_signal = background.Integral(signal.FindFirstBinAbove(0.1),
                                         signal.FindLastBinAbove(0.1))
        upper_signal = max_signal # Current upper limit on the signal
        lower_signal = 0.0       # Current lower limit on the signal 
        current_signal = lower_signal + (upper_signal - lower_signal) / 2.0 # Test signal value
        results = [] # Default start
        # Must iterate from highest sigma first (max signal), for efficiency
        for sigma in range(2, -3, -1):
            while True:
                signal.Scale(current_signal / signal.GetSumOfWeights())
                rTLimit = ROOT.TLimit()
                rConfidenceLevel = rTLimit.ComputeLimit(signal, background, data)
                cl = rConfidenceLevel.GetExpectedCLs_b(sigma)
                # is CL the level required?
                if math.fabs(cl - 1.0 + self._cl) < (1.0 - self._cl) / 100 \
                        or upper_signal - lower_signal < 0.0001:
                    results.append(current_signal)
                    # Calculate for next sigma, keep signal limits for efficiency
                    upper_signal = current_signal
                    lower_signal = 0.0
                    break
                else:
                    if cl < 1.0 - self._cl:
                        upper_signal = current_signal
                    else:
                        lower_signal = current_signal
                current_signal = lower_signal + (upper_signal - lower_signal) / 2.0
        return result

class TFeldmanCousins(object):
    def __init__(self, low_energy, high_energy, cl=0.9):
        """ Initialise with signal, summed background and data spectrum."""
        self._low_energy = low_energy
        self._high_energy = high_energy
        self._cl = cl
    def calculate(self, detected_data_set, data):
        """ Calculate the limit."""
        rTFC = ROOT.TFeldmanCousins()
        rTFC.SetMuMax(100.0)
        bg = detected_data_set.get_summed_background()
        result = rTFC.CalculateUpperLimit(data.Integral(data.GetXaxis().FindBin(self._low_energy), 
                                                        data.GetXaxis().FindBin(self._high_energy)), 
                                          bg.Integral(bg.GetXaxis().FindBin(self._low_energy),
                                                      bg.GetXaxis().FindBin(self._high_energy)))
        return [result * 5] # Temporary method, should really caclulate for 2, 1, 0, -1, -2 sigma
