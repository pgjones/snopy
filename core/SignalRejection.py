#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# All events can be rejected as pileup, these classes return the fraction that survive.
import Spectra
import ChainSpectra
import PileupBackground
import SpectrumUtil

class SignalRejection( object ):
    """ Signal Rejection base class. These classes apply rejection to the no pileup spectra and return the survival factor
    of pileup events."""
    def __init__( self ):
        """ Constructor."""
        self._FiducialVolume = 6000.0
        return
    def SetFiducialVolume( self, fiducialVolume ):
        """ Set the fiducial volume."""
        self._FiducialVolume = fiducialVolume
        return

    def ProcessSpectra( self, spectra ):
        """ Process the spectra by rejecting events."""
        assert( isinstance( spectra, Spectra.Spectra ) )
        # This function does not reject pileup spectra
        if isinstance( spectra, PileupBackground.PileupBackground ):
            return
        # Chain Spectra must be processed specially
        if isinstance( spectra, ChainSpectra.ChainSpectra ):
            for bg in spectra.GetBackgrounds():
                self.ProcessSpectra( bg )
            return # Do not Continue if chain spectra
        hist = spectra.GetHist()
        # Reduce the count by the type dependent survival factor
        hist.Scale( self.GetTypeSurvivalFactor( spectra.GetName() ) )
        for b1 in range( 1, SpectrumUtil.NBins + 1 ):
            # Now reduce the count by the energy dependent survival factor
            hist.SetBinContent( b1, hist.GetBinContent( b1 ) * self.GetSurvivalFactor( hist.GetBinCenter( b1 ) ) )
        spectra.SetHist( hist )
        return

    # Now the functions to overload
    def GetTypeSurvivalFactor( sef, name ):
        """ Some techniques target specific backgrounds, hence a specific rejection factor based on the spectra name."""
        return 1.0
    def GetSurvivalFactor( self, energy ):
        """ The factor of events at this energy that survive."""
        return 1.0
    def GetPileupSurvivalFactor( self, energy1, energy2 ):
        """ The factor of events at the given pileup energies that survive."""
        return 1.0

class CurrentRejection( SignalRejection ):
    def __init__( self ):
        super( CurrentRejection, self ).__init__()
        self._NAVFraction = 5.4**3 / 6.0**3
        return
    def GetSurvivalFraction( self, energy ):
        """ Based on the pileup rejection factors 2011."""
        #                    0.5    1.0    1.5    2.0    2.5    3.0    3.5     MeV
        suvivalFactors = [ 0.402, 0.528, 0.716, 0.613, 0.673, 0.650, 0.630 ]

        eBin = int( energy / 0.5 ) - 1
        if eBin > 5:
            survivalProb = survivalFactors[6]
        elif eBin < 0:
            survivalProb = survivalFactors[0]
        else:
            survivalProb = survivalFactors[eBin] + ( energy - eBin * 0.5 ) * ( survivalFactors[ eBin + 1 ] - survivalFactors[ eBin ] )
        # Assuming all NAV events are rejected, correct the survival factor based on the fiducial volume
        if self._FiducialVolume > self._NAVFraction: 
            survivalProb *= self._FiducialVolume - self._NAVFraction
        return survivalProb
    def GetPileupSurvivalFactor( self, energy1, energy2 ):
        """ Based on the pileup rejection factors 2011."""
        #                   0.5    1.0    1.5    2.0    2.5    3.0    3.5
        survivalFactors = [ 0.003, 0.004, 0.015, 0.013, 0.035, 0.056, 0.062,  #0.5
                            0.004, 0.001, 0.001, 0.003, 0.006, 0.001, 0.000,  #1.0
                            0.015, 0.001, 0.003, 0.004, 0.009, 0.000, 0.000,  #1.5
                            0.013, 0.003, 0.004, 0.003, 0.000, 0.000, 0.000,  #2.0
                            0.035, 0.006, 0.009, 0.000, 0.000, 0.000, 0.000,  #2.5
                            0.056, 0.001, 0.000, 0.000, 0.000, 0.000, 0.000,  #3.0
                            0.062, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000 ] #3.5
        # No data for high energy, assume all survive
        eBin1 = int( ( energy1 - 0.5 )/ 0.5 )
        eBin2 = int( ( energy2 - 0.5 )/ 0.5 )
        if eBin1 > 6:
            eBin1 = 6
        if eBin2 > 6:
            eBin2 = 6
        survivalProb = survivalFactors[ eBin1 + eBin2 * 7 ]
        if eBin1 != 6:
            survivalProb = survivalProb + ( energy1 - ( eBin1 ) * 0.5 - 0.5 ) * 2 * ( survivalFactors[ eBin1 + 1 + eBin2 * 7] - survivalFactors[ eBin1 + eBin2 * 7] )
        if eBin2 != 6:
            survivalProb = survivalProb + ( energy2 - ( eBin2 ) * 0.5 - 0.5 ) * 2 * ( survivalFactors[ eBin1 + eBin2 * 7 + 7] - survivalFactors[ eBin1 + eBin2 * 7] )
        if survivalProb < 0.0: # Mising data issue...
            return 0.0
        return survivalProb
