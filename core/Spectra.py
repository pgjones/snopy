#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.jones22@physics.ox.ac.uk>

class Spectra( object ):
    """ All backgrounds and signal types derive from this. This contains the spectra (energy histogram) for the background or signal."""
    
    def __init__( self, name ):
        """ Default constructor, just sets up a generic spectra."""
        self._PreHist = None
        self._PostHist = None
        self._SpectraName = name # Each Spectra type must have a unique name
        self._PileupLevel = 0    # Pileup backgrounds must be considered specially, 0 is no pileup, 1 single pileup, 2 double etc... 
        return
    def __eq__( self, rhs ):
        """ Check if two spectra are identical, uses the unique spectra name."""
        return type( self ) == type( rhs ) and self._SpectraName == rhs._SpectraName
    def GetName( self ):
        """ Return the spectra unique name."""
        return self._SpectraName
    def GetHist( self ):
        """ Return the spectra histogram, for processing etc..."""
        if self._PostHist = None:
            return self._PreHist
        else:
            return self._PostHist
    def SetHist( self, hist ):
        """ Set the spectra histogram, only the PostHist can be set."""
        self._PostHist = hist
        self._PostHist.SetName( self.GetName() )
    def GetActivity( self ):
        """ Return the spectra pre processed activity per year."""
        return 0.0

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
        if spectraType is MCType:
            self._PreHist = #Convert
        elif spectraType is EVType:
            self._PostHist = #Convert
        else:
            print "Error wrong or no spectraType given."
        self._Activity = activity
        return
    def GetActivity( self ):
        """ Return the spectra pre processed activity per year."""
        return self._Activity
