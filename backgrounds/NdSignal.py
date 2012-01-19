#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.jones22@physics.ox.ac.uk>
# The Nd Signal(s?)
import Background
import SpectrumUtil

class S150Nd( Background.Background ):
    """ Neodymium 150 signal definition."""
    # 
    def __init__( self ):
        super( S150Nd, self ).__init__( "150Nd0v" )
        self._NdTargetFraction = 0.056 # 5.6% Natural abundance
        self._mass = 320e-3 # eV, Kalpdor claim
        self._NME = 2.3 # Conservative IBM
        self._G = 19.2e-14 # Nasim: 26.9e-14
        self._HalfLife = (511e3)**2 / ( self._G * self._NME**2 * self._mass**2 )# year
        self._AtomicMass = 150
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( S150Nd, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.NeutrinolessDoubleBetaDecay( 3.37138, self.GetActivity() ) )
        return
