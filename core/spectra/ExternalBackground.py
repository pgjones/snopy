#!/usr/bin/env python
# Author P G Jones - 26/03/2012 <p.g.jones@qmul.ac.uk> : First revision
# Base class for external backgrounds, e.g. U, Th, K
import Spectra

class ExternalBackground( Spectra.Spectra ):
    """ All the external backgrounds derive from this, rather than from Spectra."""
    # Maybe use ppm/ppb in the future??

    def __init__( self, name ):
        """ Construct a new external background with name=name."""
        super( ExternalBackground, self ).__init__( name )
        self._Activity = 1.0 # Events per year
        return
    def SetActivity( self, activity ):
        """ Set the activity per year."""
        self._Activity = activity
        return 
    def GetActivity( self ):
        """ Activity per year."""
        return self._Activity
