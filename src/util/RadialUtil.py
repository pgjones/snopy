#!/usr/bin/env python
# Author P G Jones - 26/03/2012 <p.g.jones@qmul.ac.uk> : First revision
from ROOT import TH1D, TF1

NBins   = 600 # Number of histogram bins
LowBin  = 0.0 # Low end of the histogram radius domain [mm]
HighBin = 6000.0 # High end of the histogram radius domain [mm]

def RawSpectrum( histName ):
    """ Return the raw spectrum with name histName. """
    global NBins, LowBin, HighBin
    spectrum = TH1D( histName, histName, NBins, LowBin, HighBin )
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum

def StandardInternal():
    """ Return the standard r^3 internal spectra radial histogram."""
    global NBins, LowBin, HighBin
    spectrum = TH1D( "r^3", "r^3", NBins, LowBin, HighBin )
    for iBin in range( 1, NBins + 1 ):
        r = spectrum.GetBinLowEdge( iBin )
        dR = spectrum.GetBinWidth( iBin )
        spectrum.SetBinContent( iBin, ( pow( dR, 3.0 ) + 3.0 * dR * r * ( r + dR ) ) / pow( HighBin, 3.0 ) )
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum
