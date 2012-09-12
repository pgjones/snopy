#!/usr/bin/env python
# Author P G Jones - 02/02/2012 <p.g.jones@qmul.ac.uk>
# Prints the spectrum information
import Simulation
import ChainSpectra
import LogUtil
import EnergyResolution

class PrintSimulation( object ):
    """ Prints the spectra in a simulation under varying options."""
    def __init__( self, simulation ):
        """ Construct with a simulation of spectra."""
        if not isinstance( simulation, Simulation.Simulation ):
            LogUtil.Log( "Simultion is of incorrect type:" + str( type( simulation ) ), -2 )
        self._Simulation =  simulation
        return
    def PrintSigma( self, energy, numSigma ):
        """ Prints the counts in numSigma about the energy."""
        sigma  = self._Simulation.GetEnergyResolution().GetSigma( energy )
        self.Print( 1.0, energy - numSigma * sigma, energy + numSigma * sigma )
        return

    def Print( self, numYears, eLow, eHigh ):
        """ Prints the spectra information."""
        print LogUtil.kHeader + "Backgrounds" + LogUtil.kEnd
        print "Name & Activity"
        for index, bg in enumerate( self._Simulation.GetBackgrounds() ):
            if isinstance( bg, ChainSpectra.ChainSpectra ):
                for hist in bg.NewHistList( numYears ):
                    print "\t",
                    self.PrintHistInfo( hist, eLow, eHigh )
            else:
                hist = bg.NewHist( numYears )
                self.PrintHistInfo( hist, eLow, eHigh )
        print LogUtil.kHeader + "Signal" + LogUtil.kEnd
        print "Name & Activity"
        self.PrintHistInfo( self._Simulation.GetSignal().NewHist( numYears ), eLow, eHigh )
        return
    def PrintHistInfo( self, hist, eLow, eHigh ):
        """ Print the relevant info from the histogram."""
        countsInDomain = hist.Integral( hist.GetXaxis().FindBin( eLow ), hist.GetXaxis().FindBin( eHigh ) )
        print hist.GetName(),
        print " & %.2e" % countsInDomain,
        print " "
        return
        
