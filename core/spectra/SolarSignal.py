#!/usr/bin/env python
# Author P G Jones - 26/03/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class for solar signals
import Spectra
import Constants
import RadialUtil

class SolarSignal( Spectra.Spectra ):
    """ All the solar signals derive from this, rather than from Spectra."""

    def __init__( self, name ):
        """ Construct a new solar signal with name=name."""
        super( SolarSignal, self ).__init__( name )
        self._EventsPerKtYear = 1
        return
    def SetEventsPerKtYear( self, eventsPerKtYear ):
        """ Set the number of events per Kt of scintillator per year."""
        self._EventsPerKtYear = eventsPerKtYear
        return
    def GetEventsPerKtYear( self ):
        """ Get the number of events per Kt of scintillator per year."""
        return self._EventsPerKtYear
    def GetActivity( self ):
        """ Activity per year."""
        activity = self._DetectorInfo._ScintMass * self._EventsPerKtYear / Constants.kKgPerKt
        return activity
    # Now the functions that should be overloaded
    def Initialise( self ):
        """ By default set the radial hist to r^3 for internals."""
        super( SolarSignal, self).Initialise()
        self._RadialHist = RadialUtil.StandardInternal()
        return
