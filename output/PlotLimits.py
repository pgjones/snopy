#!/usr/bin/env python
# Author P G Jones - 24/01/2012 <p.g.jones@qmul.ac.uk>
# Plots the limits calculated by the SimulationSignalLimits class
import ROOT
import SimulationSignalLimits
import LogUtil
import ColourUtil

class PlotLimits( object ):
    """ Plots the limits in a SimulationSignalLimits under varying options."""
    def __init__( self, signalLimits, colourScheme ):
        """ Construct with some limits."""
        if not isinstance( signalLimits, SimulationSignalLimits.SimulationSignalLimits ):
            LogUtil.Log( "Simulation Signal Limit is of incorrect type: " + str( type( simulation ) ), -1 )
        self._Limits =  signalLimits
        if not isinstance( colourScheme, ColourUtil.ColourUtil ):
            LogUtil.Log( "Colour Scheme is of incorrect type: " + str( type( colourScheme ) ), -1 )
        self._ColourScheme = colourScheme
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
        medianIndex = -1
        for index, sigma in enumerate( self._Limits.GetSigmas() ):
            self._Graphs.append( ROOT.TGraph() )
            self._Graphs[-1].SetName( "%i#sigma" % sigma )
            if sigma == 0: medianIndex = index
        # Run over the years and set the graph points
        limits = []
        for yearIndex, year in enumerate( self._Limits.GetYears() ):
            # Run over the limits for this year
            for sigmaIndex, limit in enumerate( self._Limits.GetLimits()[ yearIndex ] ):
                limits.append( limit )
                self._Graphs[ sigmaIndex ].SetPoint( yearIndex + 1, year, limit )
        # Now seperate the median limit graph
        self._MedianGraph = self._Graphs[ medianIndex ]
        del self._Graphs[ medianIndex ]
        self._MedianGraph.SetPoint( 0, self._MedianGraph.GetX()[1], self._MedianGraph.GetY()[1] )

        # Now plot the graphs
        self._Canvas = ROOT.TCanvas()
        minYear = min( self._Limits.GetYears() )
        maxYear = max( self._Limits.GetYears() )
        minLimit = min( limits )
        maxLimit = max( limits )
        self._FrameGraph = ROOT.TGraph()
        self._FrameGraph.SetPoint( 0, minYear, minLimit )
        self._FrameGraph.SetPoint( 1, maxYear, maxLimit )
        self._FrameGraph.Draw( "AP" )
        self._FrameGraph.GetXaxis().SetTitle( "Livetime Years [yr]." )
        self._FrameGraph.GetYaxis().SetTitle( "Limits" )
        self._Graphs.reverse()
        for index, graph in enumerate( self._Graphs ):
            # Set the plot colour
            graph.SetFillColor( self._ColourScheme.GetFillColour( index ) )
            # Set the bounding points for fill plots
            graph.SetPoint( 0, minYear, minLimit )
            graph.SetPoint( len( self._Limits.GetYears() ) + 1, maxYear, minLimit )
            graph.Draw( "F" )
        self._MedianGraph.Draw("L")

        return self._Canvas
    
