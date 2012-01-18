#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.jones22@physics.ox.ac.uk>

class Simulation( object ):
    """ Simulation object, holds all the spectra, processing types, global variables such as Nd loading and pileup window etc..."""

    Verbosity = 0 # Higher than 0 prints stuff to the screen

    def __init__( self ):
        self._NdLoading      = 0.0 
        self._PileupWindow   = 400.0 #ns
        self._FiducialVolume = 1.0   #*100% fiducial volume percentage.
        
        # Now the processors
        self._EnergyResolution = EnergyResolution.EnergyResolution() # Start with the default energy resolution
        self._SignalRejection  = SignalRejection.SignalRejection()   # Start with the default rejection levels
    
        # Now the spectra
        self._Backgrounds = []
        self._Signal      = None
        return
    def AddBackground( self, background ):
        """ Add a new background. """
        if isinstance( background, basestring ):
            self._Backgrounds.append( SpectraTypes.SpectraTypes[ background ] )
        elif isinstance( background, Spectra.Spectra ):
            self._Backgrounds.append( background )
        elif isinstance( background, types.ListType ):
            for bg in background:
                self.AddBackground( bg )
        else:
            print "Unknown background type:", type( background )
        return
    def AddSignal( self, signal ):
        """ Add a signal, replaces the existing. """
        if isinstance( signal, basestring ):
            self._Signal = SpectraTypes.SpectraTypes[ signal ]
        elif isinstance( signal, Spectra.Spectra ):
            self._Signal = signal
        return
    def SetEnergyResolution( self, energyResoultion ):
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
        Pileup.Pileup( self._Backgrounds, self._PileupWindow, self._SignalRejection )
        return 
    def ProcessEnergyResolution( self ):
        """ Run over the backgrounds and signal and apply the energy resolution. """
        for background in self._Backgrounds:
            self._EnergyResolution.ProcessSpectra( background )
        self._EnergyResolution.ProcessSpectra( self._Signal )
        return
    def ProcessRejection( self ):
        """ Run over the backgrounds and signal and apply the rejection levels. """
        for background in self._Backgrounds:
            self._SignalRejection.ProcessSpectra( background )
        self._SignalRejection.ProcessSpectra( self._Signal )
        return
