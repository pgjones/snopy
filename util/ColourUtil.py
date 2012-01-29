#!/usr/bin/env python
# Author P G Jones - 29/01/2012 <p.jones22@physics.ox.ac.uk>
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
                          "232Th"   : ROOT.kSpring,
                          "238U"    : ROOT.kPink + 2 }
    def GetColour( self, bgName ):
        """ Return the colour by bgName."""
        assert( isinstance( bgName, basestring ) )
        elements = bgName.split( "+" )
        colour = self._Colours[ "Generic" ]
        if elements[0] in self._Colours:
            colour = self._Colours[ elements[0] ]
        colour += len( elements )
        return colour
