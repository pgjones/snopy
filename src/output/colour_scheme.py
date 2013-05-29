#!/usr/bin/env python
#
# colour_scheme.py
#
# Contains the colour scheme classes - maps colours to background names
#
# Author P G Jones - 24/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import ROOT

class ColourScheme(object):
    """ Returns the ROOT colour given a background name."""
    def get_colour(self, bgName):
        """ Default return black."""
        return ROOT.kBlack

class DefaultColours(ColourScheme):
    """ Default colour scheme, chosen by Phil."""
    def __init__(self):
        """ Set the default colour list."""
        self._colours = { "Generic" : ROOT.kBlack,
                          "150Nd0v" : ROOT.kRed,
                          "150Nd2v" : ROOT.kBlue,
                          "130Te0v" : ROOT.kRed,
                          "130Te2v" : ROOT.kBlue,
                          "144Nd"   : ROOT.kCyan,
                          "14C"     : ROOT.kGreen,
                          "40K"     : ROOT.kGreen + 3,
                          "39Ar"    : ROOT.kGreen - 3,
                          "85Kr"    : ROOT.kGreen - 6,
                          "PEP"     : ROOT.kBlue + 2,
                          "CNO"     : ROOT.kBlue + 2,
                          "B8"      : ROOT.kBlue + 2,
                          "176Lu"   : ROOT.kOrange,
                          "138La"   : ROOT.kRed - 3,
                          "147Sm"   : ROOT.kOrange - 3,
                          "148Sm"   : ROOT.kOrange - 6,
                          "227Ac"   : ROOT.kMagenta,
                          "235U"    : ROOT.kMagenta + 3,
                          "232Th Chain"   : ROOT.kSpring,
                          "238U Chain"    : ROOT.kPink + 2 }
        self._fill_colours = { 0 : ROOT.kGreen,
                               1 : ROOT.kBlue,
                               2 : ROOT.kGreen,
                               3 : ROOT.kWhite }
    def get_colour(self, bgName):
        """ Return the colour by bgName."""
        assert(isinstance(bgName, basestring))
        elements = bgName.split("+")
        colour = self._colours[ "Generic" ]
        if elements[0] in self._colours:
            colour = self._colours[ elements[0] ]
        colour += len(elements) - 1
        return colour
    def get_fill_colour(self, index):
        """ Return the colour by drawing order (index, 0 is first)."""
        if index in self._fill_colours:
            return self._fill_colours[ index ]
        else:
            return ROOT.kBlack
        
class SolarColours(DefaultColours):
    """ Default Solar colour scheme, chosen by Helen & Phil"""
    def __init__(self):
        """ Set the solar colour list."""
        self._colours = { "Generic" : ROOT.kBlack,
                          "B8"      : ROOT.kBlue,
                          "PEP"     : ROOT.kRed,
                          "CNO"     : ROOT.kGreen,
                          "Be7"     : ROOT.kMagenta,
                          "14C"     : ROOT.kGreen + 3,
                          "85Kr"    : ROOT.kYellow + 1,
                          "39Ar"    : ROOT.kCyan,
                          "40K"     : ROOT.kOrange + 1,
                          "232Th Chain"   : ROOT.kSpring + 2,
                          "238U Chain"    : ROOT.kPink + 2 }
