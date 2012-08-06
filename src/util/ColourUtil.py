#!/usr/bin/env python
# Author P G Jones - 29/01/2012 <p.g.jones@qmul.ac.uk>
# Classes set the colour scheme for backgrounds
import ROOT

class ColourUtil( object ):
    """ Returns the ROOT colour given a background name."""
    def GetColour( self, bgName ):
        """ Default return black."""
        return ROOT.kBlack

class DefaultColours( ColourUtil ):
    """ Default colour scheme, chosen by Phil."""
    def __init__( self ):
        """ Set the default colour list."""
        self._Colours = { "Generic" : ROOT.kBlack,
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
        self._FillColours = { 0 : ROOT.kGreen,
                              1 : ROOT.kBlue,
                              2 : ROOT.kGreen,
                              3 : ROOT.kWhite }
    def GetColour( self, bgName ):
        """ Return the colour by bgName."""
        assert( isinstance( bgName, basestring ) )
        elements = bgName.split( "+" )
        colour = self._Colours[ "Generic" ]
        if elements[0] in self._Colours:
            colour = self._Colours[ elements[0] ]
        colour += len( elements ) - 1
        return colour
    def GetFillColour( self, index ):
        """ Return the colour by drawing order (index, 0 is first)."""
        if index in self._FillColours:
            return self._FillColours[ index ]
        else:
            return ROOT.kBlack
        
class SolarColours( DefaultColours ):
    """ Default Solar colour scheme, chosen by Helen & Phil"""
    def __init__( self ):
        """ Set the solar colour list."""
        self._Colours = { "Generic" : ROOT.kBlack,
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
        return
