#!/usr/bin/env python
# Author P G Jones - 26/03/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class for internal backgrounds, e.g. Nd, Te...
import Spectra
import math
import Constants
import RadialUtil

class InternalBackground( Spectra.Spectra ):
    """ All the internal backgrounds derive from this, rather than from Spectra."""

    def __init__( self, name ):
        """ Construct a new internal background with name=name."""
        super( InternalBackground, self ).__init__( name )
        self._HalfLife   = 1.0 # Years
        self._AtomicMass = 1.0 # u, i.e. mass is 1 u
        self._ScintTargetFraction = 0.0 # g/g in sctinillator
        self._NdTargetFraction    = 0.0 # g/g in Nd loading
        self._TeTargetFraction    = 0.0 # g/g in Te loading
        return
    def SetTargetFractions( self, scintTarget = None, ndTarget = None, teTarget = None ):
        """ Set Target fractions in g/g. """
        if scintTarget != None:
            self._ScintTargetFraction = scintTarget
        if ndTarget != None:
            self._NdTargetFraction = ndTarget
        if teTarget != None:
            self._TeTargetFraction = teTarget
        return
    def GetTargetFractions( self ):
        """ Return the Target fractions in g/g."""
        return [ self._ScintTargetFraction, self._NdTargetFraction, self._TeTargetFraction ]
    def GetActivity( self ):
        """ Activity per year."""
        mass = self._DetectorInfo._ScintMass * self._ScintTargetFraction \
            + self._DetectorInfo._NdMass * self._NdTargetFraction \
            + self._DetectorInfo._TeMass * self._TeTargetFraction
        activity = mass * math.log(2) / ( Constants.kU * self._AtomicMass * self._HalfLife )
        return activity
    def Initialise( self ):
        """ By default set the radial hist to r^3 for internals."""
        super( InternalBackground, self ).Initialise()
        self._RadialHist = RadialUtil.StandardInternal()
        return
