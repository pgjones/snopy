#!/usr/bin/env python
# Author P G Jones - 02/02/2012 <p.g.jones@qmul.ac.uk>
# Prints the spectrum information
import Simulation
import LogUtil

class PrintSimulation( object ):
    """ Prints the spectra in a simulation under varying options."""
    def __init__( self, simulation ):
        """ Construct with a simulation of spectra."""
        if not isinstance( simulation, Simulation.Simulation ):
            LogUtil.Log( "Simultion is of incorrect type:" + str( type( simulation ) ), -2 )
        self._Simulation =  simulation
        return
    def Print( self, numYears, eLow, eHigh ):
        """ Prints the spectra information."""
        print LogUtil.kHeader + "Backgrounds" + LogUtil.kEnd
        print "Name & Activity"
        for index, bg in enumerate( self._Simulation.GetBackgrounds() ):
            hist = bg.NewHist( numYears )
            countsInDomain = hist.Integral( hist.GetXaxis().FindBin( eLow ), hist.GetXaxis().FindBin( eHigh ) )
            if countsInDomain > 1:
                #if index % 3 != 0:
                #    print "& ",
                print bg.GetName(),
                print " & %.2e" % bg.GetActivity(),
                #if index % 3 == 2:
                #    print "\\\\"
                #else:
                print " "
        print LogUtil.kHeader + "Signal" + LogUtil.kEnd
        print "Name & Activity"
        print self._Simulation.GetSignal().GetName(),
        print " & %.2e" % self._Simulation.GetSignal().GetActivity()
        return

