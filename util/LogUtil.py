#!/usr/bin/env python
# Author P G Jones - 24/01/2012 <p.jones22@physics.ox.ac.uk>
# Logs text to the screen if the Verbosity is high enough

Verbosity = 0

def Log( text, infoLevel = 0):
    """ Log the text to the screen if Verbosity is greater than infoLevel."""
    global Verbosity
    if Verbosity >= infoLevel:
        for level in range( 0, infoLevel ):
            print "\t",
        print text
    return
