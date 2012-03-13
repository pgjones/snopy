#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.g.jones@qmul.ac.uk>
# All solar signals/backgrounds, manual spectra shapes
import Background
import SpectrumUtil

class SPEP( Background.SolarBackground ):
    """ PEP signal/background definition."""
    def __init__( self ):
        super( SPEP, self ).__init__( "PEP" )
        self._EventsPerKtYear = 10834 # DocDB-83
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( SPEP, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        for iBin in range( 1, SpectrumUtil.NBins + 1 ):
            T = self._PreHist.GetBinCenter( iBin ) # Kinetic energy
            Ne = 0
            if( T <= 1.2 + self._PreHist.GetBinWidth( iBin ) ):
                Ne = 100 - 23.85 * T + 6.84 * T**2
            self._PreHist.SetBinContent( iBin, Ne )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class SCNO( Background.SolarBackground ):
    """ CNO signal/background definition."""
    def __init__( self ):
        super( SCNO, self ).__init__( "CNO" )
        self._EventsPerKtYear = 21900 # DocDB-83
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( SCNO, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        for iBin in range( 1, SpectrumUtil.NBins + 1 ):
            T = self._PreHist.GetBinCenter( iBin ) # Kinetic energy
            Ne = 0
            if( T <= 1.0 + self._PreHist.GetBinWidth( iBin ) ):
                Ne = 382.649 - 191.188 * T - 459.082 * T**2 + 307.816 * T**3
            elif( T <= 1.5 + self._PreHist.GetBinWidth( iBin ) ):
                Ne = 332.084 - 423.353 * T + 134.585 * T**2
            self._PreHist.SetBinContent( iBin, Ne )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class SB8( Background.SolarBackground ):
    """ B8 signal/background definition."""
    def __init__( self ):
        super( SB8, self ).__init__( "B8" )
        self._EventsPerKtYear = 1837 # DocDB-83
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( SB8, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        for iBin in range( 1, SpectrumUtil.NBins + 1 ):
            T = self._PreHist.GetBinCenter( iBin ) # Kinetic energy
            Ne = 3.28229 - 0.219904 * T + 0.00981048 * T**2 - 0.0105927 * T**3 + 0.00151589 * T**4 - 7.66537e-05 * T**5 + 1.31912e-06 * T**6
            self._PreHist.SetBinContent( iBin, Ne )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return

class SBe7( Background.SolarBackground ):
    """ Be7 signal/background definition."""
    def __init__( self ):
        super( SBe7, self ).__init__( "Be7 nu" )
        self._EventsPerKtYear = 199913 # DocDB-83
        return
    def Initialise( self, fiducialVolume, scintMass, ndMass, teMass ):
        """ Set the PreHist spectra to a years unprocessed events."""
        super( SBe7, self ).Initialise( fiducialVolume, scintMass, ndMass, teMass )
        for iBin in range( 1, SpectrumUtil.NBins + 1 ):
            T = self._PreHist.GetBinCenter( iBin ) # Kinetic energy
            Ne = 0
            if( T <= 0.65 + self._PreHist.GetBinWidth( iBin ) ):
                Ne = 3439.38 - 1531.56 * T + 654.453 * T**2
            self._PreHist.SetBinContent( iBin, Ne )
        self._PreHist.Scale( 1.0 / self._PreHist.GetSumOfWeights() )
        return
    
