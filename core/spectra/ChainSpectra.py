#!/usr/bin/env python
# Author P G Jones - 07/02/2012 <p.g.jones@qmul.ac.uk>
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure, allows externals
# Chain spectra together to form a single background with all backgrounds in equilibrium
import Spectra

class ChainSpectra( Spectra.Spectra ):
    """ Add multiple backgrounds to form a chain in equilibirium."""
    def __init__( self, name ):
        """ Constructor, must specify the chain name."""
        super( ChainSpectra, self ).__init__( name )
        self._Backgrounds = []
        self._Fractions = []
        return
    def SetDetectorInfo( self, detector ):
        """ Set the reference to the detector information class instance, this instance should belong to the simulation."""
        self._DetectorInfo = detector
        for bg in self._Backgrounds:
            bg.SetDetectorInfo( detector )
        return
    def AddBackground( self, bg, fraction ):
        """ Add a background of type bg, be sure to add in the chain order."""
        if not isinstance( bg, Spectra.Spectra ):
            LogUtil.Log( "Background type is unknown, type:" + str( type( bg ) ) )
        self._Backgrounds.append( bg )
        self._Fractions.append( fraction )
        return
    def GetActivity( self ):
        """ Return the chain activity, head of the chain."""
        return self._Backgrounds[0].GetActivity()
    def GetFiducialFraction( self ):
        """ Get the fraction of events that fall within the fiducial volume."""
        return self._Backgrounds[0].GetFiducialFraction()
    def SetTargetFractions( self, scintTarget = None, ndTarget = None, teTarget = None ):
        """ Set the top of the chain's target fractions."""
        self._Backgrounds[0].SetTargetFractions( scintTarget, ndTarget, teTarget )
    def GetTargetFractions( self ):
        """ Return the top of the chain's target fractions."""
        return self._Backgrounds[0].GetTargetFractions()
    def Initialise( self ):
        """ Initialise the chain."""
        super( ChainSpectra, self ).Initialise()
        for bg in self._Backgrounds:
            bg.Initialise()
        for bg, fraction in zip( self._Backgrounds, self._Fractions ):
            self._PreHist.Add( bg.GetHist(), fraction )
        return
