#!/usr/bin/env python 
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# Plots the spectra in a simulation
import Simulation
import ROOT
import SpectrumUtil
import LogUtil
import ColourUtil
import PileupBackground

class PlotSimulation( object ):
    """ Plots the spectra in a simulation under varying options."""
    def __init__( self, simulation, colourScheme ):
        """ Construct with a simulation of spectra."""
        if not isinstance( simulation, Simulation.Simulation ):
            LogUtil.Log( "Simultion is of incorrect type:" + str( type( simulation ) ), -2 )
        self._Simulation =  simulation   
        if not isinstance( colourScheme, ColourUtil.ColourUtil ):
            LogUtil.Log( "Colour Scheme is of incorrect type" + str( type( colourScheme ) ), -2 )
        self._ColourScheme = colourScheme
        return
    def Plot( self, numYears, eLow, eHigh, canvas = None ):
        """ Plot ths spectra in the simulation."""
        # Set the ROOT style settings
        ROOT.gROOT.SetStyle("Plain")
        ROOT.gStyle.SetCanvasBorderMode(0)
        ROOT.gStyle.SetPadBorderMode(0)
        ROOT.gStyle.SetPadColor(0)
        ROOT.gStyle.SetCanvasColor(0)
        ROOT.gStyle.SetOptTitle(0)
        ROOT.gStyle.SetLabelSize( 0.06, "xyz" )
        ROOT.gStyle.SetTitleSize( 0.06, "xyz" )
        ROOT.gStyle.SetOptStat(0)

        if canvas is None:
            canvas = ROOT.TCanvas()
        self._Canvas = canvas
        self._Canvas.Divide( 2, 1 ) # Two columns, separate legend canvas
        self._Legend = ROOT.TLegend( 0.05, 0.05, 0.95, 0.95 )
        self._Legend.SetFillColor( ROOT.kWhite )
        self._Histograms = [] # All plotted histograms, to store in memory
        frameHist = SpectrumUtil.RawSpectrum( "Frame" )
        self._Histograms.append( frameHist )
        vc1 = self._Canvas.cd(1)
        vc1.SetLeftMargin( 0.155 )
        vc1.SetBottomMargin( 0.15 )
        vc1.SetTopMargin( 0.05 )
        vc1.SetRightMargin( 0.05 )
        frameHist.Draw()
        frameHist.GetXaxis().SetRangeUser( eLow, eHigh )
        frameHist.GetXaxis().SetTitle( "Energy [MeV]" )
        frameHist.GetXaxis().SetTitleOffset( 1.0 )
        frameHist.GetYaxis().SetTitle( "Events per " + str( (SpectrumUtil.HighBin - SpectrumUtil.LowBin) / SpectrumUtil.NBins ) + " MeV" )
        frameHist.GetYaxis().SetTitleOffset( 1.3 )
        # Create summed background and bg + signal histograms
        self._SumBGHist = SpectrumUtil.RawSpectrum( "Sum BG" )
        self._SumBGSigHist = SpectrumUtil.RawSpectrum( "Sum BG + Signal" )
        maxCounts = 0.0 # For rescaling the histogram axis
        # Draw backgrounds and signal and summed histograms
        for bg in self._Simulation.GetBackgrounds():
            hist = bg.NewHist( numYears )
            hist.Draw("SAME")
            hist.SetLineColor( self._ColourScheme.GetColour( bg.GetName() ) )
            if isinstance( bg, PileupBackground.PileupBackground ):
                hist.SetLineStyle( bg.GetPileupLevel() + 1 )
            self._Histograms.append( hist )
            self._SumBGHist.Add( hist )
            # Add to legend if visible in the energy domain
            countsInDomain = hist.Integral( hist.GetXaxis().FindBin( eLow ), hist.GetXaxis().FindBin( eHigh ) )
            if countsInDomain > 1:
                self._Legend.AddEntry( hist, bg.GetName(), "l" )
                maxCounts = max( [ maxCounts, countsInDomain ] )
            self._Canvas.Update()
        # Rescale the histogram axis
        frameHist.GetYaxis().SetRangeUser( 1e-1, maxCounts )
        # Draw the signal first
        self._SumBGSigHist.Add( self._SumBGHist )
        self._SignalHist = self._Simulation.GetSignal().NewHist( numYears )
        self._SignalHist.SetLineColor( self._ColourScheme.GetColour( self._Simulation.GetSignal().GetName() ) )
        self._SignalHist.Draw("SAME")
        self._Legend.AddEntry( self._SignalHist, self._Simulation.GetSignal().GetName() + " : Sig", "l" )
        self._Histograms.append( hist )
        self._SumBGSigHist.Add( self._SignalHist )
        # Now draw the summed histograms
        self._SumBGHist.SetLineWidth( 3 )
        self._SumBGHist.Draw("SAME")
        self._Legend.AddEntry( self._SumBGHist, "Sum BG", "l" )
        self._SumBGSigHist.SetLineWidth( 4 )
        self._SumBGSigHist.SetLineStyle( 2 )
        self._SumBGSigHist.Draw("SAME")
        self._Legend.AddEntry( self._SumBGSigHist, "Sum BG + Sig", "l" )
        self._Canvas.cd(1).SetLogy()
        self._Canvas.cd(2)
        # Draw the legend on a different canvas
        self._Legend.SetNColumns( self._Legend.GetNRows() / 50 + 1 )
        self._Legend.Draw()
        self._Canvas.cd()
        return self._Canvas
