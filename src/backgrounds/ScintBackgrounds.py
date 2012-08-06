#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.g.jones@qmul.ac.uk> : First Revision
# Revision         - 26/03/2012 <p.g.jones@qmul.ac.uk> : New Spectra structure
# All scint backgrounds bar the decay chains
import InternalBackground
import SpectrumUtil

class B14C( InternalBackground.InternalBackground ):
    """ Carbon 14 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=60014
    def __init__( self ):
        super( B14C, self ).__init__( "14C" )
        self._ScintTargetFraction = 1e-18 # DocDB-507-v2
        self._HalfLife = 5730 # year
        self._AtomicMass = 14
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B14C, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.156, 1.0 ) )
        return

class B40K( InternalBackground.InternalBackground ):
    """ Potassium 40 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=190040
    def __init__( self ):
        super( B40K, self ).__init__( "40K" )
        self._ScintTargetFraction = 1.3e-18 # DocDB-507-v2
        self._HalfLife = 1.277e9 # year
        self._AtomicMass = 40
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B40K, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 1.311, 0.8928 ) )
        self._PreHist.Add( SpectrumUtil.GammaDecay( 1.460, 0.1067 ) )
        return

class B39Ar( InternalBackground.InternalBackground ):
    """ Argon 39 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=180039
    def __init__( self ):
        super( B39Ar, self ).__init__( "39Ar" )
        self._ScintTargetFraction = 2.75e-24 # DocDB-507-v2
        self._HalfLife = 269
        self._AtomicMass = 39
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B39Ar, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.565, 1.0 ) )
        return
        
class B85Kr( InternalBackground.InternalBackground ):
    """ Krypton 85 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=360085
    def __init__( self ):
        super( B85Kr, self ).__init__( "85Kr" )
        self._ScintTargetFraction = 2.4e-25 # DocDB-507-v2
        self._HalfLife = 10.756
        self._AtomicMass = 85
        return
    def Initialise( self ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B85Kr, self ).Initialise()
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.687, 0.996 ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.173, 0.514, 0.004 ) )
        return
