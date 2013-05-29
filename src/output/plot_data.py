#!/usr/bin/env python
#
# plot_data.py
#
# Plots raw or detected data sets.
#
# Author P G Jones - 24/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import ROOT
import spectrum_util

class DataPlotter(object):
    """ Plots a set of TH1Ds."""
    def __init__(self, backgrounds, signal, colour_scheme):
        """ Initialise with the set of backgrounds the signal and the colour scheme."""
        self._colours = colour_scheme
        self._backgrounds = backgrounds
        self._signal = signal
    def plot(self, low_energy, high_energy):
        """ Plot the data."""
        ROOT.gROOT.SetStyle("Plain")
        ROOT.gStyle.SetCanvasBorderMode(0)
        ROOT.gStyle.SetPadBorderMode(0)
        ROOT.gStyle.SetPadColor(0)
        ROOT.gStyle.SetCanvasColor(0)
        ROOT.gStyle.SetOptTitle(0)
        ROOT.gStyle.SetLabelSize(0.06, "xyz")
        ROOT.gStyle.SetTitleSize(0.06, "xyz")
        ROOT.gStyle.SetOptStat(0)
        self._canvas = ROOT.TCanvas()
        self._canvas.Divide(2, 1) # Two columns, separate legend canvas
        self._legend = ROOT.TLegend(0.05, 0.05, 0.95, 0.95)
        self._legend.SetFillColor(ROOT.kWhite)
        self._histograms = [] # All plotted histograms, to store in memory
        frame = spectrum_util.default_energy()
        self._histograms.append(frame)
        vc1 = self._canvas.cd(1)
        vc1.SetLeftMargin(0.155)
        vc1.SetBottomMargin(0.15)
        vc1.SetTopMargin(0.05)
        vc1.SetRightMargin(0.05)
        frame.Draw()
        frame.GetXaxis().SetRangeUser(low_energy, high_energy)
        frame.GetXaxis().SetTitle("Energy [MeV]")
        frame.GetXaxis().SetTitleOffset(1.0)
        frame.GetYaxis().SetTitle("Events per %0.2f MeV" % frame.GetXaxis().GetBinWidth(1))
        frame.GetYaxis().SetTitleOffset(1.3)
        # Create summed background and bg + signal histograms
        self._summed_bg = spectrum_util.default_energy("Sum BG")
        self._sum_bg_signal = spectrum_util.default_energy("Sum BG + Signal")
        maxCounts = 0.0 # For rescaling the histogram axis
        # Draw backgrounds and signal and summed histograms
        for bg in self._backgrounds:
            print bg.GetName()
            hist = bg
            hist.Draw("SAME")
            hist.SetLineColor(self._colours.get_colour(bg.GetName()))
            self._histograms.append(hist)
            self._summed_bg.Add(hist)
            # Add to legend if visible in the energy domain
            countsInDomain = hist.Integral(hist.GetXaxis().FindBin(low_energy), hist.GetXaxis().FindBin(high_energy))
            if countsInDomain > 1:
                self._legend.AddEntry(hist, bg.GetName(), "l")
                maxCounts = max([maxCounts, countsInDomain])
            self._canvas.Update()
        # Rescale the histogram axis
        frame.GetYaxis().SetRangeUser(1e-1, maxCounts)
        # Draw the signal first
        self._sum_bg_signal.Add(self._summed_bg)
        self._signal.SetLineColor(self._colours.get_colour(self._signal.GetName()))
        self._signal.Draw("SAME")
        self._legend.AddEntry(self._signal, self._signal.GetName() + " : Sig", "l")
        self._histograms.append(self._signal)
        self._sum_bg_signal.Add(self._signal)
        # Now draw the summed histograms
        self._summed_bg.SetLineWidth(3)
        self._summed_bg.Draw("SAME")
        self._legend.AddEntry(self._summed_bg, "Sum BG", "l")
        self._sum_bg_signal.SetLineWidth(4)
        self._sum_bg_signal.SetLineStyle(2)
        self._sum_bg_signal.Draw("SAME")
        self._legend.AddEntry(self._sum_bg_signal, "Sum BG + Sig", "l")
        self._canvas.cd(1).SetLogy()
        self._canvas.cd(2)
        # Draw the legend on a different canvas
        self._legend.SetNColumns(self._legend.GetNRows() / 50 + 1)
        self._legend.Draw()
        self._canvas.cd()
        return self._canvas

class RawDataPlotter(DataPlotter):
    """ Plots a raw data set."""
    def __init__(self, raw_data_set, colour_scheme):
        """ Initialise with a raw data set and a colour scheme."""
        backgrounds = []
        for data in raw_data_set.iter_backgrounds():
            backgrounds.append(spectrum_util.flattern(data))
        super(RawDataPlotter, self).__init__(backgrounds, raw_data_set.get_signal(), colour_scheme)
            
class DetectedDataPlotter(DataPlotter):
    """ Plots a detected data set."""
    def __init__(self, detected_data_set, colour_scheme):
        """ Initialise with a detected data set and a colour scheme."""
        backgrounds = []
        for data in detected_data_set.iter_backgrounds():
            backgrounds.append(data)
        super(DetectedDataPlotter, self).__init__(backgrounds, detected_data_set.get_signal(), colour_scheme)
            
