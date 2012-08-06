#!/usr/bin/env python
# Author P G Jones - 26/03/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class for pileup backgrounds
import Spectra
import RadialUtil

class PileupBackground( Spectra.Spectra ):
    """ All the pileup backgrounds derive from this, rather than from Spectra."""

    def __init__( self, name, pileupLevel, hist, activity, detectorInfo ):
        """ Construct a new pileup background with name=name."""
        super( PileupBackground, self ).__init__( name )
        self._Activity = activity # Events per year
        self._PileupLevel = pileupLevel # 1 is single pileup, 2 double pileup etc...
        self._PreHist = hist
        self._RadialHist = RadialUtil.StandardInternal() # Assumption
        self._DetectorInfo = detectorInfo
        return
    def GetActivity( self ):
        """ Activity per year."""
        return self._Activity
    def GetPileupLevel( self ):
        """ Get the pileup level."""
        return self._PileupLevel
