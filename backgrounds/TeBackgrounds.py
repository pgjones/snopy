#!/usr/bin/env python
# Author P G Jones - 29/02/2012 <p.g.jones@qmul.ac.uk> : First Revision
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure
# All Te backgrounds bar the decay chains
import InternalBackground
import SpectrumUtil

class B130Te( InternalBackground.InternalBackground ):
    """ Tellurium 130 background definition."""
    # A.W. Thesis
    def __init__( self ):
        super( B130Te, self ).__init__( "130Te2v" )
        self._TeTargetFraction = 0.345
        self._HalfLife = 7e20
        self._AtomicMass = 130
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B130Te, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.DoubleBetaDecay( 2.5303, 1.0 ) )
        return
