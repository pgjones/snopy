#!/usr/bin/env python
# Author P G Jones - 07/02/2012 <p.g.jones@qmul.ac.uk>
# InternalBackgrounds from the U238 Chain
import InternalBackground
import SpectrumUtil
import ChainSpectra

class BUraniumChain( ChainSpectra.ChainSpectra ):
    def __init__( self ):
        """ Initialise with the known chain."""
        super( BUraniumChain, self ).__init__( "238U Chain" )
        self._Backgrounds = [ B238U(), B234Th(), B234mPa(), B234U(), B230Th(), B226Ra(), B222Rn(), B218Po(), B214Pb(), B214Bi(), B214Po() ]
        self._Fractions =   [ 1.0,     1.0,      1.0,       1.0,     1.0,      1.0,      1.0,      1.0,      1.0,      1.0,      1.0 ] 
        return

class B238U( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=920238
    def __init__( self ):
        super( B238U, self ).__init__( "238U" )
        self._ScintTargetFraction = 1.6e-17 # DocDB-507-v2
        self._NdTargetFraction = 1.0e-15
        self._TeTargetFraction = 1.0e-15 # GUESS
        self._HalfLife = 4.468e9
        self._AtomicMass = 238
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B238U, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 4.220, 0.0496, 0.209 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 4.270, 0.79 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return
    
class B234Th( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=900234
    def __init__( self ):
        super( B234Th, self ).__init__( "234Th" )
        self._HalfLife = 6.6e-2
        self._AtomicMass = 234
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B234Th, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.273, 0.703 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.106, 0.166, 0.192 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.106, 0.167, 0.076 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B234mPa( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=910534 
    def __init__( self ):
        super( B234mPa, self ).__init__( "234mPa" )
        self._HalfLife = 2.2e-6
        self._AtomicMass = 234
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B234mPa, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 2.197, 1.0 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B234U( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=920234
    def __init__( self ):
        super( B234U, self ).__init__( "234U" )
        self._HalfLife = 2.455e5
        self._AtomicMass = 234
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B234U, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 4.858, 0.714 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 4.805, 0.053, 0.284 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B230Th( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=900230
    def __init__( self ):
        super( B230Th, self ).__init__( "230Th" )
        self._HalfLife = 7.538e4
        self._AtomicMass = 230
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B230Th, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 4.770, 0.763 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 4.702, 0.067, 0.234 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B226Ra( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=880226 
    def __init__( self ):
        super( B226Ra, self ).__init__( "226Ra" )
        self._HalfLife = 1600
        self._AtomicMass = 226
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B226Ra, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 4.870, 0.9445 ) )
        self._PreHist.Add( SpectrumUtil.AlphaDecayWithGamma( 4.684, 0.186, 0.056 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B222Rn( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=860222 
    def __init__( self ):
        super( B222Rn, self ).__init__( "222Rn" )
        self._HalfLife = 1e-2
        self._AtomicMass = 222
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B222Rn, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 5.59, 1.0 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B218Po( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=840218
    def __init__( self ):
        super( B218Po, self ).__init__( "218Po" )
        self._HalfLife = 5.9e-6
        self._AtomicMass = 218
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B218Po, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 6.114, 1.0 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B214Pb( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=820214
    def __init__( self ):
        super( B214Pb, self ).__init__( "214Pb" )
        self._HalfLife = 5.1e-5
        self._AtomicMass = 214
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B214Pb, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 1.023, 0.093 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.728, 0.295, 0.405 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.671, 0.352, 0.46 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.489, 0.534, 0.01 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B214Bi( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=830214
    def __init__( self ):
        super( B214Bi, self ).__init__( "214Bi" )
        self._HalfLife = 3.8e-5
        self._AtomicMass = 214
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B214Bi, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 3.272, 0.199 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.894, 1.378, 0.072 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.729, 1.543, 0.03 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.508, 1.764, 0.169 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.425, 1.847, 0.083 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.382, 1.890, 0.016 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.278, 1.994, 0.014 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.261, 2.011, 0.017 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.255, 2.017, 0.029 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.064, 2.208, 0.055 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 1.153, 2.119, 0.041 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.849, 2.423, 0.027 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.790, 2.482, 0.015 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return
    
class B214Po( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=840214
    def __init__( self ):
        super( B214Po, self ).__init__( "214Po" )
        self._HalfLife = 5.2e-12
        self._AtomicMass = 214
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B214Po, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 7.833, 1.0 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B210Pb( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=820210
    def __init__( self ):
        super( B210Pb, self ).__init__( "210Pb" )
        self._HalfLife = 22.3
        self._AtomicMass = 210
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B210Pb, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.064, 0.16 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.017, 0.047, 0.84 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B210Bi( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=830210 
    def __init__( self ):
        super( B210Bi, self ).__init__( "210Bi" )
        self._HalfLife = 1.4e-2
        self._AtomicMass = 210
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B210Bi, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 1.162, 1.0 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class B210Po( InternalBackground.InternalBackground ):
    """ Uranium 238 background definition."""
    # http://nucleardata.nuclear.lu.se/NuclearData/toi/nuclide.asp?iZA=840210
    def __init__( self ):
        super( B210Po, self ).__init__( "210Po" )
        self._HalfLife = 0.38
        self._AtomicMass = 210
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B210Po, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.AlphaDecay( 5.407, 1.0 ) )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return
    
