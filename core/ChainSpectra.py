#!/usr/bin/env python
# Author P G Jones - 07/02/2012 <p.g.jones@qmul.ac.uk>
# Chain spectra together to form a single background with all backgrounds in equilibriumB
import SpectrumUtil
import Spectra

class ChainSpectra( Spectra.Spectra ):
    """ Add multiple backgrounds to form a chain in equilibirium."""
    def __init__( self, name ):
        """ Constructor, must specify the chain name."""
        super( ChainSpectra, self ).__init__( name )
        self._Backgrounds = []
        self._Fractions = []
    def AddBackground( self, bg, fraction ):
        """ Add a background of type bg, be sure to add in the chain order."""
        if not isinstance( bg, Background ):
            LogUtil.Log( "Background type is unknown, type:" + str( type( bg ) ) )
        self._Backgrounds.append( bg )
        self._Fractions.append( fraction )
        return
    def GetActivity( self ):
        """ Return the chain activity, head of the chain."""
        return self._Backgrounds[0].GetActivity()
    def Initialise( self, scintMass, ndMass ):
        """ Initialise the backgrounds."""
        super( ChainSpectra, self ).Initialise( scintMass, ndMass )
        for bg in self._Backgrounds:
            bg.Initialise( scintMass, ndMass )
        self._PreHist = SpectrumUtil.RawSpectrum( self._Name )
        for bg, fraction in zip( self._Backgrounds, self._Fractions ):
            self._PreHist.Add( bg.GetHist(), fraction )
        return
