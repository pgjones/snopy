#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# All backgrounds/signals are a spectra object, this objects holds the actual histograms
import SpectrumUtil

class Spectra( object ):
    """ All backgrounds and signal types derive from this. This contains the spectra (energy histogram) for the background or signal."""
    
    def __init__( self, name ):
        """ Default constructor, just sets up a generic spectra."""
        self._PreHist = None # Always contains 1 year of events
        self._PostHist = None # Always contains 1 year of events
        self._Name = name # Each Spectra type must have a unique name
        self._ScintMass = 1.0 # kg
        self._NdMass = 1.0 # kg
        self._TeMass = 1.0 # kg
        self._PileupLevel = 0 # No pileup, single pileup or double pileup 
        self._PileupEvents = 0 # Number of events per year that take place as pileup instead of a pure spectra, only if PileupLevel == 0
        self._FiducialVolume = 1.0 # Percentage of total volume used after fiducial volume cut
        return
    def __eq__( self, rhs ):
        """ Check if two spectra are identical, uses the unique spectra name."""
        return type( self ) == type( rhs ) and self._Name == rhs._Name
    def GetName( self ):
        """ Return the spectra unique name."""
        return self._Name
    def GetPileupLevel( self ):
        """ Return the pileup level."""
        return self._PileupLevel
    def GetHist( self ):
        """ Return the spectra histogram, for processing etc..."""
        if self._PostHist is None:
            return self._PreHist
        else:
            return self._PostHist
    def NewHist( self, numYears ):
        """ Return the spectra histogram scaled to the number of events for numYears of runtime."""
        hist = self.GetHist()
        newHist = hist.Clone( self._Name )
        newHist.SetDirectory(0)
        newHist.Scale( self._FiducialVolume * numYears * self.GetActivity() / newHist.GetSumOfWeights() ) # PHIL TEMP FV
        return newHist
    def SetHist( self, hist ):
        """ Set the spectra histogram, only the PostHist can be set."""
        self._PostHist = hist
        self._PostHist.SetName( self.GetName() )
    def GetActivity( self ):
        """ Return the spectra pre processed activity per year."""
        return 0.0
    def GetNetActivity( self ):
        """ Return the net activity, i.e. predicted activity minus pileup events."""
        return self.GetActivity() - self._PileupEvents
    def AddPileupEvents( self, numEvents ):
        """ Increase the number of events that will occur as pileup instead of the pure spectra."""
        self._PileupEvents += numEvents
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events, default fill."""
        self._FiducialVolume = fiducialVolume
        self._ScintMass = scintMass
        self._NdMass = ndMass
        self._TeMass = teMass
        if self._PreHist is None and self._PostHist is None:
            self._PreHist = SpectrumUtil.RawSpectrum( self._Name )
            self._PostHist = None
        return

class PileupSpectra( Spectra ):
    """ Special Spectra type for pileup, allows correct activity calculation."""
    def __init__( self, name, pileupLevel, hist, activity ):
        """ Construct with a name."""
        super( PileupSpectra, self ).__init__( name )
        self._PileupLevel = pileupLevel
        self._Activity = activity
        self._PreHist = hist
        self._PreHist.SetName( name )
        return
    def GetActivity( self ):
        """ Overridden activity for pileup."""
        return self._Activity

class LoadedSpectra( Spectra ):
    """ Spectra loaded from a file instead of generated."""
    MCType = 0
    EVType = 1

    def __init__( self, name, spectraHist, spectraType, pileupLevel, activity ):
        """ Create the spectra with an existing histogram of spectraType = { Spectra.MCType, Spectra.EVType }.
        Spectra.MCType indicates a mc (pre energy resolution, rejection etc...) type histogram and Spectra.EVType indicates post. """
        super( Spectra, self ).__init__( name ) # Default setup first
        if pileupLevel < 0:
            print "Erroneous pileup level given, construction failed."
            return
        self._PileupLevel = pileupLevel
        #if spectraType is MCType:
        #    self._PreHist = #Convert
        #elif spectraType is EVType:
        #    self._PostHist = #Convert
        #else:
        #    print "Error wrong or no spectraType given."
        self._Activity = activity
        return
    def GetActivity( self ):
        """ Return the spectra pre processed activity per year."""
        return self._Activity
