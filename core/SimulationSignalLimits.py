#!/usr/bin/env python
# Author P G Jones - 23/01/2012 <p.jones22@physics.ox.ac.uk>
# Calculates the signal limits for a given simulation
import ConfidenceLevel
import Simulation
import SpectrumUtil
import LogUtil
import Serialisable

class SimulationSignalLimits( Serialisable.Serialisable ):
    """ Calculates the limit on the signal for varying years using a defined confidence level technique."""
    def __init__( self, simulation, confidenceLevel ):
        """ Initialise the class by passing a simulation and confidence level technique."""
        if not isinstance( simulation, Simulation.Simulation ):
            print "Unknown simulation type:", type( simulation )
            return
        if not isinstance( confidenceLevel, ConfidenceLevel.ConfidenceLevel ):
            print "Unknown confidence level type:", type( confidenceLevel )
            return
        self._Simulation = simulation
        self._ConfidenceLevel = confidenceLevel
        return
    def CalculateLimits( self, years = [ 1.0, 2.0, 3.0, 4.0 ] ):
        """ Calculate a limit for each year in years."""
        self._Years = years
        self._Limits = []
        LogUtil.Log( "Calculating limits:" )
        for year in self._Years:
            LogUtil.Log( "Year %i" % year, 1 )
            self._Limits.append( self._CalcLimit( year ) )
    def _CalcLimit( self, numYears ):
        """ Private function returns the limit on the signal for the years given."""
        # First produce the summed background histogram
        bgHist = SpectrumUtil.RawSpectrum( "Background" )
        for bg in self._Simulation.GetBackgrounds():
            bgHist.Add( bg.NewHist( numYears ) )
        # Now produce the signal histogram
        signalHist = self._Simulation.GetSignal().NewHist( numYears )
        # Now set the (2,1,0,-1,-2) background fluctuation (sigma) limit
        self._Sigmas = [ 2, 1, 0, -1, -2 ]
        return self._ConfidenceLevel.SignalLimit( bgHist, signalHist, self._Sigmas )
    def GetLimits( self ):
        """ Return a list of limit lists indexed by year, i.e. [ [], [], [] etc...]"""
        return self._Limits
    def GetYears( self ):
        """ Return the list of years."""
        return self._Years
    def GetSigmas( self ):
        """ Return the list of sigmas used."""
        return self._Sigmas
        
                        
