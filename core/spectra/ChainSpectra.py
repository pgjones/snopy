#!/usr/bin/env python
# Author P G Jones - 07/02/2012 <p.g.jones@qmul.ac.uk>
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure, allows externals
# Chain spectra together to form a single background with all backgrounds in equilibrium
import Spectra
import SpectrumUtil

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
    def GetBackgrounds( self ):
        """ Return the backgrounds."""
        return self._Backgrounds
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
        return
    # Overloaded methods to get the hists (from the component bgs)
    def GetHist( self ):
        """ This should not be called on a chain spectra."""
        raise Exception( "ChainSpectra::GetHist should not be called" )
    def SetHist( self, hist ):
        """ This should not be called on a chain spectra."""
        raise Exception( "ChainSpectra::SetHist should not be called" )
    def NewHist( self, numYears ):
        """ Return the spectra histogram scaled to the number of events for numYears of runtime."""
        hist = SpectrumUtil.RawSpectrum( self._Name )
        for bg in self._Backgrounds:
            bgHist = bg.GetHist().Clone( bg.GetName() )
            bgHist.Scale( self.GetActivity() * numYears )
            hist.Add( bgHist )
        return hist
