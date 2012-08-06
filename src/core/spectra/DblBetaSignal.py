#!/usr/bin/env python
# Author P G Jones - 26/03/2012 <p.g.jones@qmul.ac.uk> : First revision
# The Double Beta signal base class
import Spectra
import math
import Constants
import RadialUtil

class DblBetaSignal( Spectra.Spectra ):
    """ All the double beta signals derive from this, rather than from Spectra."""

    def __init__( self, name ):
        """ Construct a new pileup background with name=name."""
        super( DblBetaSignal, self ).__init__( name )
        self._HalfLife   = 1.0 # Years
        self._AtomicMass = 1.0 # u, i.e. mass is 1 u#
        self._mass = 1e-3 # In eV
        self._NME = 1.0 # Raw units
        self._G = 1e-14 # In years^-1
        self._NdTargetFraction = 0.0 # g/g in Nd loading
        self._TeTargetFraction = 0.0 # g/g in Te loading
        return
    def GetHalfLife( self ):
        """ Return the half-life."""
        return Constants.kme**2 / ( self._G * self._NME**2 * self._mass**2 )# year
    def SetTargetFractions( self, ndTarget = None, teTarget = None ):
        """ Set Target fractions in g/g. """
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
        mass = self._DetectorInfo._NdMass * self._NdTargetFraction + self._DetectorInfo._TeMass * self._TeTargetFraction
        activity = mass * math.log(2) / ( Constants.kU * self._AtomicMass * self.GetHalfLife() )
        return activity
    # Very useful signal converters
    def SignalToHalfLife( self, activity ):
        """ Returns the half life given an observed activity in years."""
        mass = self._DetectorInfo._NdMass * self._NdTargetFraction + self._DetectorInfo._TeMass * self._TeTargetFraction
        mass *= self.GetFiducialFraction()
        halfLife = mass * math.log(2) / ( Constants.kU * self._AtomicMass * activity )
        return halfLife
    def SignalToMass( self, activity ):
        """ Returns the mass given an activity in years."""
        halfLife = self.SignalToHalfLife( activity )
        return math.sqrt( Constants.kme**2 / ( self._G * self._NME**2 * halfLife ) )
    # Now the functions that must be overloaded
    def Initialise( self ):
        """ By default set the radial hist to r^3 for internals."""
        super( DblBetaSignal, self).Initialise()
        self._RadialHist = RadialUtil.StandardInternal()
        return
