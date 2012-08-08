#!/usr/bin/env python
# Author P G Jones - 06/08/2012 <p.g.jones@qmul.ac.uk> : First Revision
# Standard background rejection used in this study, for both sno+py and Nassim's assumptions
import Spectra
import PileupBackground
import SpectrumUtil
import SignalRejection

class SNOPyRejection( SignalRejection.SignalRejection ):
    """ Specific rejection used by SNO+Py in this study."""
    def __init__( self ):
        super( SNOPyRejection, self ).__init__()
        return
    def GetTypeSurvivalFactor( self, name ):
        """ Return the expected survival factors."""
        if name is "214Bi": #99.99% rejection
            return ( 1.0 - 0.9999 )
        elif name is "208Tl": #90% rejection
            return ( 1.0 - 0.9 )
        return 1.0

class NassimRejection( SignalRejection.SignalRejection ):
    """ Specific rejection used by Nassim."""
    def __init__( self ):
        super( NassimRejection, self ).__init__()
        return
    def GetTypeSurvivalFactor( self, name ):
        """ TEMP: the /0.36 in Tl208 is to replicate Nassim's apparent lack of branching and the 0.8 is to replicate Nassim's apparent livetime correction."""
        if name is "214Bi":
            return ( 1.0 - 0.9999 ) * 0.8
        elif name is "208Tl":
            return ( 1.0 - 0.9 ) * 0.8 / 0.36
        return 0.8
