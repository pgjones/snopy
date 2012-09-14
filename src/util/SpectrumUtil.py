#!/usr/bin/env python
# Author P G Jones - 19/01/2012 <p.g.jones@qmul.ac.uk>
from ROOT import TH1D
import math
import AlphaQuenchUtil

NBins   = 2400 # Number of histogram bins
LowBin  = 0.0 # Low end of the histogram energy domain [MeV]
HighBin = 24.0 # High end of the histogram energy domain [MeV]

kElectronMass = 0.511 # MeV mass of electron

def RawSpectrum( histName ):
    """ Return the raw spectrum with name histName. """
    global NBins, LowBin, HighBin
    spectrum = TH1D( histName, histName, NBins, LowBin, HighBin )
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum

def BetaDecayWithGamma( QBeta,
                        QGamma,
                        numEvents ):
    """ Convinience function to produce the beta + gamma spectrum. """
    hist = BetaDecay( QBeta, numEvents )
    hist = CoincidentGamma( hist, QGamma, 1.0 ) # Always get a gamma with the beta (assumed usage)
    return hist

def AlphaDecayWithGamma( QAlpha,
                         QGamma,
                         numEvents ):
    """ Convinience function to produce the alpha + gamma spectrum. """
    hist = AlphaDecay( QAlpha, numEvents )
    hist = CoincidentGamma( hist, QGamma, 1.0 ) # Always get a gamma with the alpha (assumed usage)
    return hist

def BetaDecay( Q,
               numEvents ):
    """ Produces a histogram filled with numEvents beta decay events with end point Q."""
    global NBins, kElectronMass
    hist = RawSpectrum( "Beta" )
    for iBin in range( 1, NBins + 1 ):
        T = hist.GetBinCenter( iBin ) 
        Ne = 0
        if( T <= Q + hist.GetBinWidth( iBin ) ):
            binFraction = 1.0 # Fraction of bin to fill
            if( T > Q ): # Allow for bin widths
                binFraction = 1.0 - ( T - Q ) / hist.GetBinWidth( iBin )
                T = Q
            Ne = binFraction * math.sqrt( T**2 + 2 * T * kElectronMass ) * ( Q - T )**2 * ( T + kElectronMass )
        hist.SetBinContent( iBin, Ne )
    hist.Scale( numEvents / hist.GetSumOfWeights() )
    return hist

def DoubleBetaDecay( Q,
               numEvents ):
    """ Produces a histogram filled with numEvents double beta decay events with end point Q."""
    global NBins, kElectronMass
    hist = RawSpectrum( "Beta" )
    Q = Q / kElectronMass        
    for iBin in range( 1, NBins + 1 ):
        T = hist.GetBinCenter( iBin )
        T = T / kElectronMass
        Ne = 0
        if( T <= Q + hist.GetBinWidth( iBin ) ):
            binFraction = 1.0 # Fraction of bin to fill
            if( T > Q ): # Allow for bin widths
                binFraction = 1.0 - ( T - Q ) / hist.GetBinWidth( iBin )
                T = Q
            Ne = binFraction * T * ( Q - T )**5 * ( 1 + 2 * T + 4 * T**2 / 3 + T**3 / 3 + T**4 / 30 )
        hist.SetBinContent( iBin, Ne )
    hist.Scale( numEvents / hist.GetSumOfWeights() )
    return hist

def AlphaDecay( Q,
                numEvents ):
    """ Produces a histogram filled with numEvents alpha decay events with end point Q."""
    global NBins
    # First renormalise the Q by the alpha quenching factor
    Q = Q / AlphaQuenchUtil.QuenchingFactor( Q )
    hist = RawSpectrum( "Alpha" )
    for iBin in range( 1, NBins + 1 ):
        T = hist.GetBinCenter( iBin )
        Ne = 0
        # Delta function at end point
        if( math.fabs( T - Q ) < hist.GetBinWidth( iBin ) ):
            Ne = 1
        hist.SetBinContent( iBin, Ne )
    hist.Scale( numEvents / hist.GetSumOfWeights() )
    return hist

def GammaDecay( Q,
                numEvents ):
    """ Produces a histogram filled with numEvents gamma decay events with end point Q."""
    global NBins
    hist = RawSpectrum( "Gamma" )
    for iBin in range( 1, NBins + 1 ):
        T = hist.GetBinCenter( iBin )
        Ne = 0
        # Delta function at end point
        if( math.fabs( T - Q ) < hist.GetBinWidth( iBin ) ):
            Ne = 1
        hist.SetBinContent( iBin, Ne )
    hist.Scale( numEvents / hist.GetSumOfWeights() )
    return hist

def NeutrinolessDoubleBetaDecay( Q,
                                 numEvents ):
    """ Produces a histogram filled with numEvents neutrinoless double beta decay events with end point Q."""
    global NBins
    hist = RawSpectrum( "Neutrinoless" )
    for iBin in range( 1, NBins + 1 ): 
        T = hist.GetBinCenter( iBin )
        Ne = 0
        # Delta function at end point
        if( math.fabs( T - Q ) < hist.GetBinWidth( iBin ) ):
            Ne = 1
        hist.SetBinContent( iBin, Ne )
    hist.Scale( numEvents / hist.GetSumOfWeights() )
    return hist

def CoincidentGamma( hist,
                     gammaEnergy,
                     gammaFraction ):
    """ Shifts the spectrum in the appropriate ways to include the effects of
    coincident gamma emission. As this is indistinguishable."""
    global NBins
    for iBin in range( NBins, 0, -1 ):
        content = hist.GetBinContent( iBin )
        currentEnergy = hist.GetBinCenter( iBin )
        # Reduce fraction of events in this bin by 1 - gammaFraction
        hist.SetBinContent( iBin, content * ( 1.0 - gammaFraction ) )
        newEnergy = currentEnergy + gammaEnergy
        newBin = hist.GetXaxis().FindBin( newEnergy )
        newEnergyLow = hist.GetBinLowEdge( iBin ) + gammaEnergy
        newEnergyHigh = newEnergyLow + hist.GetBinWidth( iBin )
        # Now fill correct bins
        fractionInHighBin = ( newEnergyHigh - hist.GetBinLowEdge( newBin + 1 ) ) / ( newEnergyHigh - newEnergyLow )
        if( fractionInHighBin > 0.0 ):
            hist.SetBinContent( newBin + 1, hist.GetBinContent( newBin + 1 ) + content * gammaFraction * fractionInHighBin )

        fractionInMidBin = hist.GetBinWidth( newBin ) / ( newEnergyHigh - newEnergyLow )
        if( fractionInMidBin > 0.0 ):
            hist.SetBinContent( newBin, hist.GetBinContent( newBin ) + content * gammaFraction * fractionInMidBin )

        fractionInLowBin = ( hist.GetBinLowEdge( newBin ) - newEnergyLow ) / ( newEnergyHigh - newEnergyLow )
        if( fractionInLowBin > 0.0 ):
            hist.SetBinContent( newBin - 1, hist.GetBinContent( newBin - 1 ) + content * gammaFraction * fractionInLowBin )

    return hist
