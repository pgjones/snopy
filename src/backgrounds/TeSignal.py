#!/usr/bin/env python
# Author P G Jones - 06/03/2012 <p.g.jones@qmul.ac.uk> : First Revision
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure
# The Te Signal(s?)
import DblBetaSignal
import SpectrumUtil

class S130Te( DblBetaSignal.DblBetaSignal ):
    """ Tellurium 130 signal definition."""
    
    def __init__( self ):
        """ Construct the Neodynium signal."""
        global me
        super( S130Te, self ).__init__( "130Te0v" )
        self._TeTargetFraction = 0.345 # 34.5% Natural abundance
        self._mass = 320e-3 # eV, Kalpdor claim
        self._NME = 3.4 # Conservative IBM Dueck
        #self._NME = 4.059 # S Biller recommendation
        self._G = 2.22e-14 # Kolita
        #self._G = 4.09e-14 # S Biller
        self._AtomicMass = 130
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        # Use the default r^3 radial dependence
        super( S130Te, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.NeutrinolessDoubleBetaDecay( 2.5303, 1.0 ) )
        return
