#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.g.jones@qmul.ac.uk>
# All Nd backgrounds bar the decay chains
import Background
import SpectrumUtil

class B150Nd( Background.Background ):
    """ Neodymium 150 background definition."""
    # A.W. Thesis
    def __init__( self ):
        super( B150Nd, self ).__init__( "150Nd2v" )
        self._NdTargetFraction = 0.056 # 5.6% Natural abundance
        self._HalfLife = 9.11e18
        self._AtomicMass = 150
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B150Nd, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.DoubleBetaDecay( 3.37138, 1.0 ) )
        return

class B144Nd( Background.Background ):
    """ Neodymium 144 background definition."""
    # DocDB-507-v2
    def __init__( self ):
        super( B144Nd, self ).__init__( "144Nd" )
        self._NdTargetFraction = 2.38e-1 # DocDB-867
        self._HalfLife = 2.29e15
        self._AtomicMass = 144
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B144Nd, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 1.380, 1.0 ) )
        return

class B176Lu( Background.Background ):
    """ Lutetium 176 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=710176
    def __init__( self ):
        super( B176Lu, self ).__init__( "176Lu" )
        self._NdTargetFraction = 1.2e-7
        self._HalfLife = 3.78e10
        self._AtomicMass = 176
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B176Lu, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.194, 0.998, 0.0034 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.595, 0.597, 0.9966 ) )
        return

class B138La( Background.Background ):
    """ Lanthanium 138 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=570138
    def __init__( self ):
        super( B138La, self ).__init__( "138La" )
        self._NdTargetFraction = 5e-7
        self._HalfLife = 1.05e11
        self._AtomicMass = 138
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B138La, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.255, 0.789, 0.336 ) )
        self._PreHist.Add( SpectrumUtil.GammaDecay( 1.436, 0.664 ) )
        return

class B147Sm( Background.Background ):
    """ Samarium 147 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=620147
    def __init__( self ):
        super( B147Sm, self ).__init__( "147Sm" )
        self._NdTargetFraction = 5e-7
        self._HalfLife = 1.06e11
        self._AtomicMass = 147
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B147Sm, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 2.310, 1.0 ) )
        return

class B148Sm( Background.Background ):
    """ Samarium 148 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=620148
    def __init__( self ):
        super( B148Sm, self ).__init__( "148Sm" )
        self._NdTargetFraction = 5e-7
        self._HalfLife = 7e15
        self._AtomicMass = 148
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B148Sm, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 1.986, 1.0 ) )
        return

class B227Ac( Background.Background ):
    """ Actinium 227 background definition."""
    # 
    def __init__( self ):
        super( B227Ac, self ).__init__( "227Ac" )
        self._NdTargetFraction = 1e-18
        self._HalfLife = 2.1e1
        self._AtomicMass = 148
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B227Ac, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.0203, 0.0245, 0.10 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.0355, 0.0093, 0.35 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.0448, 0.54 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 5.042, 0.014 ) )
        return

class B235U( Background.Background ):
    """ Uranium 235 background definition."""
    # 
    def __init__( self ):
        super( B235U, self ).__init__( "235U" )
        self._NdTargetFraction = 5e-11
        self._HalfLife = 7.03e8
        self._AtomicMass = 235
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B235U, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 4.291, 0.3878, 1.0 ) )
        return
