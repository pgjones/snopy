#!/usr/bin/env python
# Author P G Jones - 24/01/2012 <p.g.jones@qmul.ac.uk>
# Logs text to the screen if the Verbosity is high enough
import sys

Verbosity = 0

def Log( text, infoLevel = 0):
    """ Log the text to the screen if Verbosity is greater than infoLevel."""
    global Verbosity
    if infoLevel == 0:
        text = '\033[92m' + text + '\033[0m'
    if infoLevel < 0: # Error, quit the code
        print '\033[91m' + text + '\033[0m'
        sys.exit(0)
    if Verbosity >= infoLevel:
        for level in range( 0, infoLevel ):
            print "\t",
        print text
    return
