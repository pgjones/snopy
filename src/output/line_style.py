#!/usr/bin/env python
#
# line_style.py
#
# Contains the line styles for background names
#
# Author P G Jones - 09/06/2013 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import ROOT

class LineStyle(object):
    """ Returns the ROOT line style given a background name."""
    def get_style(self, bg_name):
        """ Default return normal line."""
        return 1

class Default(LineStyle):
    """ Default line styles, chosen by Phil."""
    def get_style(self, bg_name):
        """ Dashed for various levels of pileup."""
        num_plus = bg_name.count('+')
        if num_plus == 0:
            return 1
        elif num_plus == 1:
            return 2
        elif num_plus == 2:
            return 3
        
