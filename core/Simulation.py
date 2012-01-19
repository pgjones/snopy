#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.jones22@physics.ox.ac.uk>
# Controls the simulation of the spectra and holds all the results.
import EnergyResolution
import SignalRejection
import Spectra
import SpectraTypes
import types
import Pileup

class Simulation( object ):
    """ Simulation object, holds all the spectra, processing types, global variables such as Nd loading and pileup window etc..."""

    Verbosity = 0 # Higher than 0 prints stuff to the screen

    def __init__( self ):
        self._PileupWindow   = 400.0 #ns
        self._FiducialVolume = 1.0   #*100% fiducial volume percentage.
        self._ScintMass = 1000.0
        self._NdMass    = 0.01 * self._ScintMass
        
        # Now the processors
        self._EnergyResolution = EnergyResolution.EnergyResolution() # Start with the default energy resolution
        self._SignalRejection  = SignalRejection.SignalRejection()   # Start with the default rejection levels
    
        # Now the spectra
        self._Backgrounds = []
        self._Signal      = None
        return
    def SetEnergyResolution( self, energyResolution ):
        """ Set the energy resolution."""
        if isinstance( energyResolution, EnergyResolution.EnergyResolution ):
            self._EnergyResolution = energyResolution
        else:
            print "Unknown energy resolution type:", type( energyResolution )
        return

    def AddBackground( self, background ):
        """ Add a new background. """
        if isinstance( background, basestring ):
            self._Backgrounds.append( SpectraTypes.SpectraTypes[ background ]() )
        elif isinstance( background, Spectra.Spectra ):
            self._Backgrounds.append( background )
        elif isinstance( background, types.ListType ):
            for bg in background:
                self.AddBackground( SpectraTypes.SpectraTypes[ bg ]() )
        else:
            print "Unknown background type:", type( background )
            return
        self._Backgrounds[-1].Initialise( self._ScintMass, self._NdMass )
        return
    def AddSignal( self, signal ):
        """ Add a signal, replaces the existing. """
        if isinstance( signal, basestring ):
            self._Signal = SpectraTypes.SpectraTypes[ signal ]()
        elif isinstance( signal, Spectra.Spectra ):
            self._Signal = signal
        self._Signal.Initialise( self._ScintMass, self._NdMass )
        return
    def SetEnergyResolution( self, energyResolution ):
        """ Set the energy resolution type, must be a EnergyResolution.EnergyResolution derived object. """
        if isinstance( energyResolution, EnergyResolution.EnergyResolution ):
            self._EnergyResolution = energyResolution 
        else:
            print "Object passed of incorrect type:", type( energyResolution )
        return
    def SetSignalRejection( self, signalRejection ):
        """ Set the signal rejection type, must be a SignalRejection.SignalRejection derived object. """
        if isinstance( signalRejection, SignalRejection.SignalRejection ):
            self._SignalRejection = signalRejection
        else:
            print "Object passed of incorrect type:", type( signalRejection )
        return

    # Now the functions that do calculation
    def CalculatePileupBackgrounds( self ):
        """ Automatically calculates and adds the pileup backgrounds. """
        if Simulation.Verbosity > 0:
            print "Pileup Backgrounds:"
        Pileup.Pileup( self._Backgrounds, self._PileupWindow, self._SignalRejection, Simulation.Verbosity )
        return 
    def ProcessEnergyResolution( self ):
        """ Run over the backgrounds and signal and apply the energy resolution. """
        if Simulation.Verbosity > 0:
            print "Energy Resolution:"
        for background in self._Backgrounds:
            if Simulation.Verbosity > 0:
                print background.GetName()
            self._EnergyResolution.ProcessSpectra( background )
        self._EnergyResolution.ProcessSpectra( self._Signal )
        return
    def ProcessRejection( self ):
        """ Run over the backgrounds and signal and apply the rejection levels. """
        for background in self._Backgrounds:
            self._SignalRejection.ProcessSpectra( background )
        self._SignalRejection.ProcessSpectra( self._Signal )
        return
    
    def GetBackgrounds( self ):
        """ Return the backgrounds list."""
        return self._Backgrounds
    def GetSignal( self ):
        """ Return the signal spectra."""
        return self._Signal
