#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.g.jones@qmul.ac.uk>
# The Nd Signal(s?)
import Background
import SpectrumUtil
import math

kme = 511e3 #in eV

class S150Nd( Background.Background ):
    """ Neodymium 150 signal definition."""
    # 
    def __init__( self ):
        """ Construct the Neodynium signal."""
        global me
        super( S150Nd, self ).__init__( "150Nd0v" )
        self._NdTargetFraction = 0.056 # 5.6% Natural abundance
        self._mass = 320e-3 # eV, Kalpdor claim
        self._NME = 2.3 # Conservative IBM
        self._G = 19.2e-14 # Nasim: 26.9e-14
        self._HalfLife = kme**2 / ( self._G * self._NME**2 * self._mass**2 )# year
        self._AtomicMass = 150
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( S150Nd, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.NeutrinolessDoubleBetaDecay( 3.37138, self.GetActivity() ) )
        return
    def SignalToHalfLife( self, activity ):
        """ Returns the half life given an activity in years."""
        halfLife = self._ScintMass * self._ScintTargetFraction + self._NdMass * self._NdTargetFraction
        halfLife *= math.log(2) / ( Background.Background.kU * self._AtomicMass * activity )
        return halfLife
    def SignalToMass( self, activity ):
        """ Returns the mass given an activity in years."""
        global kme
        halfLife = self.SignalToHalfLife( activity )
        return math.sqrt( kme**2 / ( self._G * self._NME**2 * halfLife ) )

