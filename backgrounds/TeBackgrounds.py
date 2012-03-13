#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.g.jones@qmul.ac.uk>
# All Te backgrounds bar the decay chains
import Background
import SpectrumUtil

class B130Te( Background.Background ):
    """ Tellurium 130 background definition."""
    # A.W. Thesis
    def __init__( self ):
        super( B130Te, self ).__init__( "130Te2v" )
        self._TeTargetFraction = 0.345
        self._HalfLife = 7e20
        self._AtomicMass = 130
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B130Te, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.DoubleBetaDecay( 2.5303, 1.0 ) )
        return
