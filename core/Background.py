#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.jones22@physics.ox.ac.uk>

class Background( Spectra ):
    """ Base class for background spectras."""
    kU = 1.66e-27 # Atomic mass unit Kg

    def __init__( self, name ):
        """ Constructor, requires a unique name from the derived class."""
        super( Background, self ).__init__( name )
        self._HalfLife   = 1.0 # Years
        self._AtomicMass = 1.0 # u, i.e. mass is 1 u
        self._ScintTargetFraction = 0.0 # g/g in sctinillator
        self._NdTargetFraction    = 0.0 # g/g in Nd loading
    def SetTargetFractions( self, scintTarget, ndTarget ):
        """ Set Target fractions in g/g."""
        self._ScintTargetFraction = scintTarget
        self._NdTargetFraction = ndTarget
        # Values changed, must reinitialise
        self.Initialise() 
        return
    def GetTargetFractions( self ):
        """ Return the Target fractions in g/g."""
        return [ self._ScintTargetFraction, self._NdTargetFraction ]
    def GetActivity( self ):
        """ Activity per year."""
        activity = self._ScintMass * self._ScintTargetFraction + self._NdMass * self._NdTargetFraction
        activity *= math.log(2) / ( kU * self._AtomicMass * self._HalfLife )
        return activity

class SolarBackground( Spectra ):
    """ Base class for solar backgrounds. """
    def __init__( self, name ):
        """ Constructor, requires a unique name from the derived class."""
        super( SolarBackground, self ).__init__( name )
        self._EventsPerKtYear = 1
    def SetEventsPerKtYear( self, eventsPerKtYear ):
        """ Set the number of events per Kt of scintillator per year."""
        self._EventsPerKtYear = eventsPerKtYear
        return
    def SetEventsPerKtYear( self ):
        """ Get the number of events per Kt of scintillator per year."""
        return self._EventsPerKtYear
    def GetActivity( self ):
        """ Activity per year."""
        activity = self._ScintMass * self._EventsPerKtYear / 1000000
        return activity
