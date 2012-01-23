#!/usr/bin/env python
# Author P G Jones - 23/01/2012 <p.jones22@physics.ox.ac.uk>
# Calculates the signal limits for a given simulation

class SimulationSignalLimits( object ):
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
    def CalculateLimits( self, years ):
        """ Calculate a limit for each year in years."""
        
    def _CalcLimit( self, numYears ):
        """ Private function returns the limit on the signal for the years given."""
        # First produce the summed background histogram
        bgHist = SpectrumUtil.RawSpectrum( "Background" )
        for bg in self._Simulation.GetBackgrounds():
            bgHist.Add( bg.NewHist( numYears ) )
        # Now produce the signal histogram
        signalHist = self._Simulation.Getsignal().NewHist( numYears )
        # Now set the limit

        
                        
