#!/usr/bin/env python
# Author P G Jones - 06/03/2012 <p.g.jones@qmul.ac.uk>
# The Te Signal(s?)
import Background
import SpectrumUtil
import math

kme = 511e3 #in eV

class S130Te( Background.Background ):
    """ Tellurium 130 signal definition."""
    # 
    def __init__( self ):
        """ Construct the Neodynium signal."""
        global me
        super( S130Te, self ).__init__( "130Te0v" )
        self._TeTargetFraction = 0.345 # 34.5% Natural abundance
        self._mass = 320e-3 # eV, Kalpdor claim
        self._NME = 3.372 # Conservative IBM
        self._G = 4.09e-14
        self._HalfLife = kme**2 / ( self._G * self._NME**2 * self._mass**2 )# year
        self._AtomicMass = 130
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( S130Te, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.NeutrinolessDoubleBetaDecay( 2.5303, 1.0 ) )
        return
    def SignalToHalfLife( self, activity ):
        """ Returns the half life given an activity in years."""
        halfLife = self._ScintMass * self._ScintTargetFraction + self._TeMass * self._TeTargetFraction
        halfLife *= math.log(2) / ( Background.Background.kU * self._AtomicMass * activity )
        return halfLife
    def SignalToMass( self, activity ):
        """ Returns the mass given an activity in years."""
        global kme
        halfLife = self.SignalToHalfLife( activity )
        return math.sqrt( kme**2 / ( self._G * self._NME**2 * halfLife ) )

