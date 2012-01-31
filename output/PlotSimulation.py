#!/usr/bin/env python 
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# Plots the spectra in a simulation
import Simulation
import ROOT
import SpectrumUtil
import LogUtil
import ColourUtil

class PlotSimulation( object ):
    """ Plots the spectra in a simulation under varying options."""
    def __init__( self, simulation, colourScheme ):
        """ Construct with a simulation of spectra."""
        if not isinstance( simulation, Simulation.Simulation ):
            LogUtil.Log( "Simultion is of incorrect type:" + str( type( simulation ) ) )
        self._Simulation =  simulation   
        if not isinstance( colourScheme, ColourUtil.ColourUtil ):
            LogUtil.Log( "Colour Scheme is of incorrect type" + str( type( colourScheme ) ) )
        self._ColourScheme = colourScheme
        return
    def Plot( self, numYears, eLow, eHigh ):
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
        
        self._Canvas = ROOT.TCanvas()
        self._Canvas.Divide( 2, 1 ) # Two columns, separate legend canvas
        self._Legend = ROOT.TLegend( 0.05, 0.05, 0.95, 0.95 )
        self._Legend.SetFillColor( ROOT.kWhite )
        self._Histograms = [] # All plotted histograms, to store in memory
        frameHist = SpectrumUtil.RawSpectrum( "TEMP" )
        self._Histograms.append( frameHist )
        vc1 = self._Canvas.cd(1)
        vc1.SetLeftMargin( 0.155 )
        vc1.SetBottomMargin( 0.15 )
        vc1.SetTopMargin( 0.05 )
        vc1.SetRightMargin( 0.05 )
        frameHist.Draw()
        frameHist.GetYaxis().SetRangeUser( 1e-1, 1e14 )
        frameHist.GetXaxis().SetRangeUser( eLow, eHigh )
        frameHist.GetXaxis().SetTitle( "Energy [MeV]" )
        frameHist.GetXaxis().SetTitleOffset( 1.0 )
        frameHist.GetYaxis().SetTitle( "Events per " + str( (SpectrumUtil.HighBin - SpectrumUtil.LowBin) / SpectrumUtil.NBins ) + " MeV" )
        frameHist.GetYaxis().SetTitleOffset( 1.3 )
        # Create summed background and bg + signal histograms
        self._SumBGHist = SpectrumUtil.RawSpectrum( "Sum BG" )
        self._SumBGSigHist = SpectrumUtil.RawSpectrum( "Sum BG + Signal" )
        # Draw backgrounds and signal and summed histograms
        for bg in self._Simulation.GetBackgrounds():
            hist = bg.NewHist( numYears )
            hist.Draw("SAME")
            hist.SetLineColor( self._ColourScheme.GetColour( bg.GetName() ) )
            hist.SetLineStyle( bg.GetPileupLevel() + 1 )
            self._Histograms.append( hist )
            self._SumBGHist.Add( hist )
            self._Legend.AddEntry( hist, bg.GetName(), "l" )
        self._SumBGSigHist.Add( self._SumBGHist )
        self._SignalHist = self._Simulation.GetSignal().NewHist( numYears )
        self._SignalHist.Draw("SAME")
        self._Histograms.append( hist )
        self._SumBGSigHist.Add( self._SignalHist )
        # Now draw the summed histograms
        self._SumBGHist.Draw("SAME")
        self._SumBGSigHist.SetLineStyle( 2 )
        self._SumBGSigHist.Draw("SAME")
        self._Canvas.cd(1).SetLogy()
        self._Canvas.cd(2)
        # Draw the legend on a different canvas
        self._Legend.SetNColumns( len( self._Histograms ) / 10 + 1 )
        self._Legend.Draw()
        self._Canvas.cd()
        return self._Canvas
