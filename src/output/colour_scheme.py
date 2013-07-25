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
                          "130Te0v" : ROOT.kRed,
                          "130Te2v" : ROOT.kBlue,
                          "14C"     : ROOT.kPink,
                          "40K"     : ROOT.kPink + 2,
                          "39Ar"    : ROOT.kMagenta,
                          "85Kr"    : ROOT.kMagenta + 1,
                          "232Th"   : ROOT.kGreen,
                          "238U"    : ROOT.kOrange,                         
                          "PEP"     : ROOT.kCyan,
                          "CNO"     : ROOT.kCyan + 1,
                          "B8"      : ROOT.kCyan + 2,
                          "Be7"     : ROOT.kBlue,
                          "176Lu"   : ROOT.kBlack,
                          "138La"   : ROOT.kBlack,
                          "147Sm"   : ROOT.kBlack,
                          "148Sm"   : ROOT.kBlack,
                          "227Ac"   : ROOT.kBlack,
                          "235U"    : ROOT.kBlack,
                          "144Nd"   : ROOT.kBlack,
                          "150Nd0v" : ROOT.kBlack,
                          "150Nd2v" : ROOT.kBlack }
                       
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
