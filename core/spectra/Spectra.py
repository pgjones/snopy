#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk> : First revision
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure, allows externals
# Revision         - 05/04/2012 <p.g.jones@qmul.ac.uk> : Initialisation is for analytic spectra only, this will check
# All backgrounds/signals are a spectra object, this objects holds the actual histograms
import DetectorInfo
import LogUtil
import SpectrumUtil
import RadialUtil
from ROOT import TH2D, TFile

class Spectra( object ):
    """ All backgrounds and signals are spectra, and they all derived from this. 
    This class holds the raw spectrum histogram and the post detector effects histogram and the radial dependence histogram."""

    def __init__( self, name ):
        """ Construct a new spectra with name=name."""
        self._Name = name # Each Spectra type must have a unique name
        self._PreHist = None # This is the pre processing histogram and should be normalised to 1
        self._PostHist = None # This is the post processing histogram and should be normalised to 1
        self._RadialHist = None # This is the radial dependence histogram
        self._DetectorInfo = None # Reference to the detector information class
        return
    def SetDetectorInfo( self, detector ):
        """ Set the reference to the detector information class instance, this instance should belong to the simulation."""
        if isinstance( detector, DetectorInfo.DetectorInfo ):
            self._DetectorInfo = detector
        else:
            LogUtil.Log( "Unknown detector info type:" + str( type( detector ) ), -2 )
        return
    def __eq__( self, rhs ):
        """ Check if two spectra are identical, uses the unique spectra name."""
        return type( self ) == type( rhs ) and self._Name == rhs._Name
    def GetName( self ):
        """ Return the spectra unique name."""
        return self._Name
    def GetHist( self ):
        """ Return the spectra histogram, for processing etc..."""
        if self._PostHist is None:
            return self._PreHist
        else:
            return self._PostHist
        return
    def NewHist( self, numYears ):
        """ Return the spectra histogram scaled to the number of events for numYears of runtime."""
        hist = self.GetHist()
        newHist = hist.Clone( self._Name )
        newHist.SetDirectory(0)
        newHist.Scale( numYears * self.GetActivity() * self.GetFiducialFraction() / newHist.GetSumOfWeights() )
        return newHist
    def SetHist( self, hist ):
        """ Set the spectra histogram, only the PostHist can be set."""
        self._PostHist = hist
        self._PostHist.SetName( self.GetName() )
        return
    # Now the functions that may be useful to overload by derived classes
    def GetFiducialFraction( self ):
        """ Get the fraction of events that fall within the fiducial volume."""
        return self._RadialHist.Integral( self._RadialHist.FindBin( 0.0 ), self._RadialHist.FindBin( self._DetectorInfo._FiducialRadius ) )
    # Now the functions that must be overloaded by derived classes
    def GetActivity( self ):
        """ Return the spectra pre processed activity per year."""
        return 0.0
    def Initialise( self ):
        """ Initialise the pre hist, all global variables should be correctly set by this point."""
        self._PreHist = SpectrumUtil.RawSpectrum( self._Name )
        self._RadialHist = RadialUtil.RawSpectrum( self._Name + "_r" )
        return
    def ImportSpectra( self, fileName ):
        """ Import the spectra from an appropriate ROOT file."""
        rootFile = ROOT.TFile( fileName, "READ" )
        combinedHist = ROOT.TH2D( rootFile.Get( "Spectra" ) )
        self._RadialHist = combinedHist.ProjectionY( self._Name + "_r" )
        self._RadialHist.Scale( 1.0 / self._RadialHist.GetSumOfWeights() )
        self._PreHist = combinedHist.ProjectionX( self._Name )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        rootFile.Close()
        return
