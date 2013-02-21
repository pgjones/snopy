#!/usr/bin/env python
#
# plot_limits.py
#
# Plots limit sets.
#
# Author P G Jones - 29/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import math
import constants
import ROOT
import spectrum_util

class DblBetaLimitPlotter(object):
    """ Plots a set of Limits."""
    def __init__(self, atomic_mass, limits, colour_scheme):
        """ Initialise with the set of limits and the colour scheme."""
        self._colours = colour_scheme
        self._limits = limits
        self._atomic_mass = atomic_mass
        self._plots = []
    def plot_limit(self):
        """ Plot the raw limit values."""
        self._plots = [] # Reset the plots list
        plot = ROOT.TGraph()
        for index, year_limit in enumerate(self._limits.iter_limits()):
            plot.SetPoint(index, year_limit[0], year_limit[1][2])
            print index, year_limit
        self._plots.append(plot)
        self._plot()
    def plot_half_life(self, isotope_mass):
        """ Convert the limit to half-life and plot."""
        self._plots = [] # Reset the plots list
        plot = ROOT.TGraph()
        for index, year_limit in enumerate(self._limits.iter_limits()):
            plot.SetPoint(index, year_limit[0], self._convert_to_half_life(isotope_mass, 
                                                                           year_limit[1][2] / year_limit[0]))
        self._plots.append(plot)
        self._plot()
    def plot_mass(self, isotope_mass, G, NME):
        """ Convert the limit to neutrino mass and plot."""
        self._plots = [] # Reset the plots list
        plot = ROOT.TGraph()
        for index, year_limit in enumerate(self._limits.iter_limits()):
            plot.SetPoint(index, year_limit[0], self._convert_to_mass(isotope_mass, G, NME, 
                                                                      year_limit[1][2] / year_limit[0]))
        self._plots.append(plot)
        self._plot()
    ################################################################################################
    def _convert_to_half_life(self, isotope_mass, signal):
        """ Return the half-life equivalent for the signal."""
        return isotope_mass * math.log(2) / (constants.U * self._atomic_mass * signal)
    def _convert_to_mass(self, isotope_mass, G, NME, signal):
        """ Return the mass equivalent for the signal."""
        return math.sqrt(constants.me**2 / \
                             (G * NME**2 * self._convert_to_half_life(isotope_mass, signal)))
    def _plot(self):
        """ Plot the produced histograms.""" 
        ROOT.gROOT.SetStyle("Plain")
        ROOT.gStyle.SetCanvasBorderMode(0)
        ROOT.gStyle.SetPadBorderMode(0)
        ROOT.gStyle.SetPadColor(0)
        ROOT.gStyle.SetCanvasColor(0)
        ROOT.gStyle.SetOptTitle(0)
        ROOT.gStyle.SetLabelSize(0.06, "xyz")
        ROOT.gStyle.SetTitleSize(0.06, "xyz")
        ROOT.gStyle.SetOptStat(0)
        self._plots[0].Draw("AL")
