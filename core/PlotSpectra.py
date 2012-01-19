#!/usr/bin/env python 
# Author P G Jones - 18/01/2012 <p.jones22@physics.ox.ac.uk>
# Plots the spectra in a simulation
import Simulation
import ROOT
import SpectrumUtil

class PlotSpectra( object ):
    """ Plots the spectra in a simulation under varying options."""
    def __init__( self, simulation ):
        """ Construct with a simulation of spectra."""
        if isinstance( simulation, Simulation.Simulation ):
            self._Simulation =  simulation   
        else:
            print "Simultion is of incorrect type:", type( simulation )
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
        self._FrameHist = SpectrumUtil.RawSpectrum( "TEMP" )
        self._FrameHist.Draw()
        self._FrameHist.GetYaxis().SetRangeUser( 1e-1, 1e14 )
        self._FrameHist.GetXaxis().SetRangeUser( eLow, eHigh )
        self._FrameHist.GetXaxis().SetTitle( "Energy [MeV]" )
        self._FrameHist.GetYaxis().SetTitle( "Events per " + str( (SpectrumUtil.HighBin - SpectrumUtil.LowBin) / SpectrumUtil.NBins ) + " MeV" )
        # Create summed background and bg + signal histograms
        self._SumBGHist = SpectrumUtil.RawSpectrum( "Sum BG" )
        self._SumBGSigHist = SpectrumUtil.RawSpectrum( "Sum BG + Signal" )
        # Draw backgrounds and signal and summed histograms
        for bg in self._Simulation.GetBackgrounds():
            hist = bg.GetHist()
            hist.Draw("SAME")
            self._SumBGHist.Add( hist )
        self._SumBGSigHist.Add( self._SumBGHist )
        signalHist = self._Simulation.GetSignal().GetHist()
        signalHist.Draw("SAME")
        self._SumBGSigHist.Add( signalHist )
        self._Canvas().cd().SetLogy()
        return self._Canvas
