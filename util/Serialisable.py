#!/usr/bin/env python
# Author P G Jones - 29/01/2012 <p.g.jones@qmul.ac.uk>
# Base class allows derived classes to be easily serialised/deserialised
import pickle

class Serialisable( object ):
    """ Includes load and save functions, works for any dervied class."""
    def Save( self, fileName = "Simulation.pkl" ):
        """ Pickle and save the simulation data."""
        outFile = open( fileName, "w" )
        pickle.dump( self.__dict__, outFile, 2 )
        outFile.close()
        return
    def Load( self, fileName = "Simulation.pkl" ):
        """ Load and unpickle the simulation data."""
        inFile = open( fileName, "r" )
        temp = pickle.load( inFile )
        inFile.close()
        self.__dict__.update( temp )
        return
    
