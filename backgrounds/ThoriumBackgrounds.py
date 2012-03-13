#!/usr/bin/env python
# Author P G Jones - 07/02/2012 <p.g.jones@qmul.ac.uk>
# Backgrounds from the 232Th Chain
import Background
import SpectrumUtil
import ChainSpectra

class BThoriumChain( ChainSpectra.ChainSpectra ):
    def __init__( self ):
        """ Initialise with the known chain."""
        super( BThoriumChain, self ).__init__( "232Th Chain" )
        self._Backgrounds = [ B232Th(), B228Ra(), B228Ac(), B228Th(), B224Ra(), B220Rn(), B216Po(), B212Pb(), B212Bi(), B212Po(), B208Tl() ]
        self._Fractions =   [ 1.0,      1.0,      1.0,      1.0,      1.0,      1.0,      1.0,      1.0,      1.0,      0.64,     0.36 ]
        return

class B232Th( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=900232 
    def __init__( self ):
        super( B232Th, self ).__init__( "232Th" )
        self._ScintTargetFraction = 6.8e-18 # DocDB-507-v2
        self._NdTargetFraction = 1.0e-14
        self._TeTargetFraction = 1.0e-14 # GUESS
        self._HalfLife = 1.405e10
        self._AtomicMass = 232
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B232Th, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 4.082, 0.779 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 4.018, 0.064, 0.221 ) )
        return
    
class B228Ra( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=880228
    def __init__( self ):
        super( B228Ra, self ).__init__( "228Ra" )
        self._HalfLife = 5.75
        self._AtomicMass = 228
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B228Ra, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.039, 0.007, 1.0 ) )
        return

class B228Ac( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=890228
    def __init__( self ):
        super( B228Ac, self ).__init__( "228Ac" )
        self._HalfLife = 7e-4
        self._AtomicMass = 228
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B228Ac, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.158, 0.969, 0.31 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.758, 0.396, 0.116 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 2.069, 0.058, 0.1 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.959, 1.168, 0.035 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.973, 1.154, 0.056 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.005, 1.122, 0.058 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.104, 1.023, 0.03 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.596, 1.532, 0.081 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.489, 1.638, 0.012 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.481, 1.646, 0.042 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.403, 1.724, 0.016 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.439, 1.688, 0.026 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.445, 1.682, 0.012 ) )
        return

class B228Th( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=900228
    def __init__( self ):
        super( B228Th, self ).__init__( "228Th" )
        self._HalfLife = 1.9116
        self._AtomicMass = 228
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B228Th, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 5.520, 0.711 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 5.436, 0.084, 0.282 ) )
        return

class B224Ra( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=880224
    def __init__( self ):
        super( B224Ra, self ).__init__( "224Ra" )
        self._HalfLife = 1e-2
        self._AtomicMass = 224
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B224Ra, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 5.789, 0.95 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 5.548, 0.241, 0.05 ) )
        return
    
class B220Rn( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=860220 
    def __init__( self ):
        super( B220Rn, self ).__init__( "220Rn" )
        self._HalfLife = 1.8e-6
        self._AtomicMass = 220
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B220Rn, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 6.404, 1.0 ) )
        return

class B216Po( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=840216
    def __init__( self ):
        super( B216Po, self ).__init__( "216Po" )
        self._HalfLife = 4.6e-9 
        self._AtomicMass = 216
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B216Po, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 6.906, 1.0 ) )
        return

class B212Pb( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=820212
    def __init__( self ):
        super( B212Pb, self ).__init__( "212Pb" )
        self._HalfLife = 1.2e-3
        self._AtomicMass = 212
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B212Pb, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.574, 0.123 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.335, 0.239, 0.825 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.159, 0.415, 0.05 ) )
        return

class B212Bi( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=830212
    def __init__( self ):
        super( B212Bi, self ).__init__( "212Bi" )
        self._HalfLife = 1.2e-4
        self._AtomicMass = 212
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B212Bi, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.BetaDecay( 2.254, 0.555 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.527, 0.727, 0.04 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.741, 1.513, 0.014 ))
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.633, 1.621, 0.019 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 6.167, 0.04, 0.25 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 6.207, 0.0975 ) )
        return

class B212Po( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=840212 
    def __init__( self ):
        super( B212Po, self ).__init__( "212Po" )
        self._HalfLife = 9.5e-15
        self._AtomicMass = 212
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B212Po, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 8.954, 1.0 ) )
        return

class B208Tl( Background.Background ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=810208
    def __init__( self ):
        super( B208Tl, self ).__init__( "208Tl" )
        self._HalfLife = 5.8e-6
        self._AtomicMass = 208
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B208Tl, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.293, 3.708, 0.245 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.526, 3.475, 0.218 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.803, 3.198, 0.487 ) )                
        return
