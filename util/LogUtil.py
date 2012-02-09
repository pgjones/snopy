#!/usr/bin/env python
# Author P G Jones - 24/01/2012 <p.g.jones@qmul.ac.uk>
# Logs text to the screen if the Verbosity is high enough
import sys

Verbosity = 0
kHeader = '\033[95m'
kOKBlue = '\033[94m'
kOKGreen = '\033[92m'
kWarning = '\033[93m'
kFail = '\033[91m'
kEnd = '\033[0m'


def Log( text, infoLevel = 0):
    """ Log the text to the screen if Verbosity is greater than infoLevel."""
    global Verbosity, kFail, kWarning, kOKGreen, kEnd
    if infoLevel == 0:
        text = kHeader + text + kEnd
    elif infoLevel == -1: # Warning
        text = kWarning + text + kEnd
    elif infoLevel < -1: # Error, quit the code
        print kFail + text + kEnd
        sys.exit(0)    
    if Verbosity >= infoLevel:
        for level in range( 0, infoLevel ):
            print "\t",
        print text
    return
