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
    function = TF1( "r^3", "[0]*x^3", LowBin, HighBin )
    function.SetParameter( 0, 1.0 )
    spectrum = TH1D( "r^3", "[0]*x^3", NBins, LowBin, HighBin )
    spectrum.Add( function )
    spectrum.Scale( 1.0 / spectrum.GetSumOfWeights() ) # Normalise 
    spectrum.SetDirectory(0) # Stop ROOT trying to memory manage it
    return spectrum
