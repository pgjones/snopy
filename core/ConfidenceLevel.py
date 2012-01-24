#!/usr/bin/env python
# Author P G Jones - 23/01/2012 <p.jones22@physics.ox.ac.uk>
# Calculates the signal limits for a given confidence level
import ROOT
import math
import LogUtil

class ConfidenceLevel( object ):
    """ Base class for classes that calculate the signal limit at a set confidence level."""
    def __init__( self, cl = 0.9 ):
        """ Initialise with a default 90% condifence level required."""
        self._CL = cl
        return
    def SignalLimit( self, bgHist, signalHist, sigmas ):
        """ Set the histograms and sigma background fluctuations required."""
        self._BGHist = bgHist
        self._SignalHist = signalHist
        self._Sigmas = sigmas
        return self._SetLimits()

class IterativeLevel( ConfidenceLevel ):
    """ Base class for confidence level techniques that must iterate the signal to find the limit."""
    def _SetLimits( self ):
        """ Set the limits for each sigma."""
        maxSignal = self._BGHist.Integral( self._BGHist.GetXaxis().FindBin( 3.0 ), self._BGHist.GetXaxis().FindBin( 3.7 ) ) / 2.0 # "Seed" value REPLACE PHIL
        upperSignal = maxSignal # Current upper limit on the signal
        lowerSignal = 0.0       # Current lower limit on the signal 
        signal = lowerSignal + ( upperSignal - lowerSignal ) / 2.0 # Current signal test value
        results = self._Sigmas # Initialise a results list
        # Must iterate from lowest sigma first, for efficiency
        sortedSigmas = sorted( self._Sigmas )
        sortedSigmas.reverse()
        for sigma in sortedSigmas:
            LogUtil.Log( "Sigma:%i" % sigma, 2 )
            while True:
                self._SignalHist.Scale( signal / self._SignalHist.GetSumOfWeights() )
                print signal,
                cl = 1.0 - self._GetCL( sigma )
                print cl
                # is CL the level required?
                if math.fabs( cl - self._CL ) < ( self._CL ) / 100:
                    results[ results.index( sigma ) ] = signal
                    # Calculate for next sigma, keep signal limits for efficiency
                    upperSignal = signal
                    lowerSignal = 0.0 
                    break
                else:
                    if cl > self._CL:
                        upperSignal = signal
                    else:
                        lowerSignal = signal
                signal = lowerSignal + ( upperSignal - lowerSignal ) / 2.0
        return

class TLimitLevel( IterativeLevel ):
    """ Set a confidence level using the ROOT TLimit software."""
    def _GetCL( self, sigma ):
        """ Return the current confidence level."""
        rTLimit = ROOT.TLimit()
        rConfidenceLevel = rTLimit.ComputeLimit( self._SignalHist, self._BGHist, self._BGHist )
        return rConfidenceLevel.GetExpectedCLs_b( sigma )
