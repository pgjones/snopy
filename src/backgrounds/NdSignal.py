#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.g.jones@qmul.ac.uk> : First revision
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure
# The Nd Signal(s?)
import DblBetaSignal
import SpectrumUtil

class S150Nd( DblBetaSignal.DblBetaSignal ):
    """ Neodymium 150 signal definition."""
    
    def __init__( self ):
        """ Construct the Neodynium signal."""
        global me
        super( S150Nd, self ).__init__( "150Nd0v" )
        self._NdTargetFraction = 0.056 # 5.6% Natural abundance
        self._mass = 320e-3 # eV, Kalpdor claim
        self._NME = 2.3 # Conservative IBM
        self._G = 19.2e-14 # Nasim: 26.9e-14
        self._AtomicMass = 150
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        # Use the default r^3 radial hist
        super( S150Nd, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.NeutrinolessDoubleBetaDecay( 3.37138, 1.0 ) )        
        return
