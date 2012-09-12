#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure
# Revision         - 05/04/2012 <p.g.jones@qmul.ac.uk> : Spectra are only initialised if passed by name, otherwise initialisation is assumed
# Controls the simulation of the spectra and holds all the results.
import DetectorInfo
import EnergyResolution
import SignalRejection
import Spectra
import SpectraTypes
import types
import Pileup
import LogUtil
import Serialisable

class Simulation( Serialisable.Serialisable ):
    """ Simulation object, holds all the spectra, processing types, global variables such as Nd loading and pileup window etc..."""
    def __init__( self, ndLoading = 0.0, teLoading = 0.0, # %
                  fiducialRadius = 6000.0, #mm
                  scintMass=774000 ): #Kg
        """ Constructor, set default objects."""
        self._PileupWindow = 400.0 # ns
        ndMass = ndLoading / 100.0 * scintMass # e.g 0.1% loading default
        teMass = teLoading / 100.0 * scintMass # e.g 0.1% loading default
        self._DetectorInfo = DetectorInfo.DetectorInfo( scintMass,
                                                        ndMass,
                                                        teMass,
                                                        fiducialRadius ) # In mm
        # Now the processors
        self._EnergyResolution = EnergyResolution.EnergyResolution() # Start with the default energy resolution
        self._SignalRejection  = SignalRejection.SignalRejection()   # Start with the default rejection levels    
        # Now the spectra
        self._Backgrounds = []
        self._Signal      = None
        return
    def SetEnergyResolution( self, energyResolution ):
        """ Set the energy resolution."""
        if not isinstance( energyResolution, EnergyResolution.EnergyResolution ):
            LogUtil.Log( "Unknown energy resolution type:" + str( type( energyResolution ) ), -2 )
        self._EnergyResolution = energyResolution
        return
    def GetEnergyResolution( self ):
        """ Return the energy resolution."""
        return self._EnergyResolution

    def AddBackground( self, background ):
        """ Add a new background. """
        if isinstance( background, basestring ):
            self._Backgrounds.append( SpectraTypes.SpectraTypes[ background ]() )
            self._Backgrounds[-1].Initialise()
        elif isinstance( background, Spectra.Spectra ):
            self._Backgrounds.append( background )
        elif isinstance( background, types.ListType ):
            for bg in background:
                self.AddBackground( bg )
        else:
            LogUtil.Log( "Unknown background type:" + str( type( background ) ), -2 )
        self._Backgrounds[-1].SetDetectorInfo( self._DetectorInfo )
        return
    def AddSignal( self, signal ):
        """ Add a signal, replaces the existing. """
        if isinstance( signal, basestring ):
            self._Signal = SpectraTypes.SpectraTypes[ signal ]()
            self._Signal.Initialise()
        elif isinstance( signal, Spectra.Spectra ):
            self._Signal = signal
        self._Signal.SetDetectorInfo( self._DetectorInfo )
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
        LogUtil.Log( "Pileup Backgrounds", 0 )
        self._Backgrounds = Pileup.Pileup( self._Backgrounds, self._PileupWindow, self._SignalRejection )
        return 
    def ProcessEnergyResolution( self ):
        """ Run over the backgrounds and signal and apply the energy resolution. """
        LogUtil.Log( "Convolving Energy resolution", 0 )
        for background in self._Backgrounds:
            LogUtil.Log( background.GetName(), 1 )
            self._EnergyResolution.ProcessSpectra( background )
        LogUtil.Log( self._Signal.GetName(), 1 )
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
