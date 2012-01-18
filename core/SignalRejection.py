#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.jones22@physics.ox.ac.uk>

class SignalRejection( object ):
    """ Signal Rejection base class. These classes apply rejection to the no pileup spectra and return the survival factor
    of pileup events."""
    def __init__( self ):
        """ Constructor."""
        self._FiducialVolume = 1.0
        return
    def SetFiducialVolume( self, fiducialVolume ):
        """ Set the fiducial volume."""
        self._FiducialVolume = fiducialVolume
        return

    def ProcessSpectra( self, spectra ):
        """ Process the spectra by rejecting events."""
        assert( isinstance( spectra, Spectra.Spectra ) )
        # This function does not reject pileup spectra
        if spectra.GetPileupLevel() != 0:
            return
        hist = spectra.GetHist()
        for b1 in range( 1, SpectrumUtil.NBins + 1 ):
            hist.SetBinContent( b1, hist.GetBinContent( b1 ) * self.GetSurvivalFactor( hist.GetBinCenter( b1 ) ) )
        spectra.SetHist( hist )
        return

    def GetSurvivalFactor( self, energy ):
        """ The factor of events at this energy that survive."""
        return 1.0
    def GetPileupSurvivalFactor( self, energy1, energy2 ):
        """ The factor of events at the given pileup energies that survive."""
        return 1.0

class CurrentRejection( SignalRejection ):
    def __init__( self ):
        super( CurrentRejection, self ).__init__()
        #                       0.5    1.0    1.5    2.0    2.5    3.0    3.5     MeV
        self.SuvivalFactors = [ 0.402, 0.528, 0.716, 0.613, 0.673, 0.650, 0.630 ]
        self._NAVFraction = 5.4**3 / 6.0**3
        return
    def GetSurvivalFraction( self, energy ):
        """ Based on the pileup rejection factors 2011."""
        eBin = int( energy / 0.5 ) - 1
        if eBin > 5:
            survivalProb = self.SurvivalFactors[6]
        elif eBin < 0:
            survivalProb = self.SurvivalFactors[0]
        else:
            survivalProb = self.SurvivalFactors[eBin] + ( energy - eBin * 0.5 ) * ( self.SurvivalFactors[ eBin + 1 ] - self.SurvivalFactors[ eBin ] )
        # Assuming all NAV events are rejected, correct the survival factor based on the fiducial volume
        if self._FiducialVolume > self._NAVFraction: 
            survivalProb *= self._FiducialVolume - self._NAVFraction
        return survivalProb
    def GetPileupSurvivalFactor( self, energy1, energy2 ):
        """ Based on the pileup rejection factors 2011."""

        
