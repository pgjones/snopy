#!/usr/bin/env python
# Author P G Jones - 24/01/2012 <p.jones22@physics.ox.ac.uk>
# Plots the limits calculated by the SimulationSignalLimits class

class PlotLimits( object ):
    """ Plots the limits in a SimulationSignalLimits under varying options."""
    def __init__( self, signalLimits ):
        """ Construct with some limits."""
        if not isinstance( signalLimits, SimulationSignalLimits.SimulationSignalLimits ):
            print "Simulation Signal Limit is of incorrect type:", type( simulation )
            return
        self._Limits =  signalLimits
        return
    def Plot( self ):
        """ Plot the limits."""
        # Set the ROOT settings
        ROOT.gROOT.SetStyle("Plain")
        ROOT.gStyle.SetCanvasBorderMode(0)
        ROOT.gStyle.SetPadBorderMode(0)
        ROOT.gStyle.SetPadColor(0)
        ROOT.gStyle.SetCanvasColor(0)
        ROOT.gStyle.SetLabelSize( 0.06, "xyz" )
        ROOT.gStyle.SetTitleSize( 0.06, "xyz" )
        ROOT.gStyle.SetOptStat(0)
        ROOT.gStyle.SetPadTickX(1)
        ROOT.gStyle.SetPadTickY(1)
        
        self._Graphs  = []
        # Produce a graph for each sigma in the set
        for sigma in self._Limits.GetSigmas()
            self._Graphs.append( ROOT.TGraph() )
            self._Graphs[-1].SetName( sigma + "#sigma" )
        # Run over the years and set the graph points
        for yearIndex, year in enumerate( self._Limits.GetYears() ):
            # Run over the limits for this year
            for sigmaIndex, limits in enumerate( self._Limits.GetLimits()[ yearIndex ] ):
                self._Graphs[ sigmaIndex ].SetPoint( yearIndex, year, limits[ sigmaIndex ] )
        
        # Now plot the graphs
        self._Canvas = ROOT.TCanvas()
        self._FrameGraph = ROOT.TGraph()
        self._FrameGraph.Draw( "A" )
        self._FrameGraph.GetXaxis().SetTitle( "Livetime Years [yr]." )
        self._FrameGraph.GetYaxis().SetTitle( "Limits" )
        for graph in self._Graphs:
            graph.Draw( "L" )
        
        return self._Canvas
    
