#!/usr/bin/env python
# Author P G Jones - 26/03/2012 <p.g.jones@qmul.ac.uk> : First revision
# Holds the detector information, e.g. the mass of scintillator
import DetectorInfo

class DetectorInfo( object ):
    """ This class holds the basic detector information."""
    def __init__( self, scintMass = 1.0, ndMass = 0.0, teMass = 0.0, fiducialRadius = 6000.0 ):
        """ Construct this class with the appropriate scint, nd, te masses and the fiducial radius."""
        self._ScintMass = scintMass # Kg, Mass of the scintillator
        self._NdMass = ndMass # Kg, Mass of the Neodymium
        self._TeMass = teMass # Kg, Mass of the Tellurium
        self._FiducialRadius = fiducialRadius # mm, the fiducial radius 
