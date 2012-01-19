#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.jones22@physics.ox.ac.uk>
# All scint backgrounds bar the decay chains

# Register the spectra types in this file
SpectraTypes.SpectraTypes["14C"] = B14C
SpectraTypes.SpectraTypes["40K"] = B40K
SpectraTypes.SpectraTypes["39Ar"] = B39Ar
SpectraTypes.SpectraTypes["85Kr"] = B85Kr

class B14C( Background.Background ):
    """ Carbon 14 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=60014
    def __init__( self ):
        super( B14C, self ).__init__( "14C" )
        self._ScintTargetFraction = 1e-18 # DocDB-507-v2
        self._HalfLife = 5730 # year
        self._AtomicMass = 14
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B14C, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.156, self.GetActivity() ) )
        return

class B40K( Background.Background ):
    """ Potassium 40 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=190040
    def __init__( self ):
        super( B40K, self ).__init__( "40K" )
        self._ScintTargetFraction = 1.3e-18 # DocDB-507-v2
        self._HalfLife = 1.277e9 # year
        self._AtomicMass = 40
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B40K, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.BetaDecay( 1.311, 0.8928 * self.GetActivity() ) )
        self._PreHist.Add( SpectrumUtil.GammaDecay( 1.460, 0.1067 * self.GetActivity() ) )
        return

class B39Ar( Background.Background ):
    """ Argon 39 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=180039
    def __init__( self ):
        super( B39Ar, self ).__init__( "39Ar" )
        self._ScintTargetFraction = 2.75e-24 # DocDB-507-v2
        self._HalfLife = 269
        self._AtomicMass = 39
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B39Ar, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.565, self.GetActivity() ) )
        return
        
class B85Kr( Background.Background ):
    """ Krypton 85 background definition."""
    # http://nucleardata.nuclear.lu.se/nucleardata/toi/nuclide.asp?iZA=360085
    def __init__( self ):
        super( B39Ar, self ).__init__( "85Kr" )
        self._ScintTargetFraction = 2.4e-25 # DocDB-507-v2
        self._HalfLife = 10.756
        self._AtomicMass = 85
        return
    def Initialise( self, scintMass, ndMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( B40K, self ).Initialise( scintMass, ndMass )
        self._PreHist.Add( SpectrumUtil.BetaDecay( 0.687, 0.996 * self.GetActivity() ) )
        self._PreHist.Add( SpectrumUtil.BetaDecayWithGamma( 0.173, 0.514, 0.004 * self.GetActivity() ) )
        return
