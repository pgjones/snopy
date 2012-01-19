#!/usr/bin/env python 
# Author P G Jones - 18/01/2012 <p.jones22@physics.ox.ac.uk>

class PlotSpectra( object ):
    """ Plots the spectra in a simulation under varying options."""
    def __init__( self, simulation ):
        """ Construct with a simulation of spectra."""
        if not isinstance( simulation, Simulation.Simulation ):
            print "Simultion is of incorrect type:", type( simulation )
        self._Simulation =  simulation
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
        frameHist = SpectrumUtil.RawSpectrum( "TEMP" )
        frameHist.Draw()
        frameHist.GetYaxis().SetRangeUser( 1e-1, 1e14 )
        frameHist.GetXaxis().SetRangeUser( eLow, eHigh )
        frameHist.GetXaxis().SetTitle( "Energy [MeV]" )
        frameHist.GetYaxis().SetTitle( "Events per " + str( (SpectrumUtil.HighBin - SpectrumUtil.LowBin) / SpectrumUtil.NBins ) + " MeV" )
        # Create summed background and bg + signal histograms
        self._SumBGHist = SpectrumUtil.RawSpectrum( "Sum BG" )
        self._SumBGSigHist = SpectrumUtil.RawSpectrum( "Sum BG + Signal" )
        # Draw backgrounds and signal and summed histograms
        for bg in self._Simulation.GetBackgrounds():
            hist = bg.GetHist()
            hist.Draw("SAME")
            self._SumBGHist.Add( hist )
        self._SumBGSigHist.Add( sumBGHist )
        signalHist = self._Simulation.GetSignal().GetHist()
        signalHist.Draw("SAME")
        self._SumBGSigHist.Add( signalHist )
        return self._Canvas
