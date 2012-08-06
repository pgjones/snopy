#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# Applies the energy resolution smearing
import Spectra
import ChainSpectra
import SpectrumUtil
import math

class EnergyResolution( object ):
    """ Energy Resolution base class. These classes apply smearing to the spectra to account for the energy resolution."""
    def ProcessSpectra( self, spectra ):
        """ Process the spectra by convolving in the energy resolution. """
        assert( isinstance( spectra, Spectra.Spectra ) )
        # Chain Spectra must be processed specially
        if isinstance( spectra, ChainSpectra.ChainSpectra ):
            for bg in spectra.GetBackgrounds():
                self.ProcessSpectra( bg )
            return # Do not Continue if chain spectra
        hist = spectra.GetHist()
        convolved = SpectrumUtil.RawSpectrum( hist.GetName() )
        # C( b1 ) = sum( b2 ) h( b2 ) * g[b2]( b1 - b2 )
        # Wish to convolve h with a gaussian which has a sigma dependent on b2, i.e. the energy in h
        for b1 in range( 1, SpectrumUtil.NBins + 1 ):
            h = 0
            for b2 in range( 1, SpectrumUtil.NBins + 1 ):
                sigma = self.GetSigma( hist.GetXaxis().GetBinCenter( b2 ) ) # In MeV
                c = sigma / hist.GetBinWidth( b1 ) # Convert to a sigma in number of bins from MeV
                N = 1.0 / ( c * math.sqrt( 2.0 * math.pi ) ) # Normalisation factor
                h = h + hist.GetBinContent( b2 ) * N * math.exp( -( b1 - b2 )**2 / ( 2.0 * c**2 ) )
            convolved.SetBinContent( b1, h )
        spectra.SetHist( convolved )
        return

    def GetSigma( self, energy ):
        """ Must notice the difference between sigma and resolution, resolution is typically FWHM. Return in MeV."""
        return 0.0
    def GetResolution( self, energy ):
        """ Must notice the difference between sigma and resolution, resolution is typically FWHM. Return in MeV."""
        return self.GetSigma( energy ) * 2.0 * math.sqrt( 2.0 * math.Log( 2 ) )

class Nhit( EnergyResolution ):
    """ Theorectical best case resolution for a given Nhit Per MeV."""
    def __init__( self, nHitPerMeV = 389 ):
        """ Constructor, has default nHitPerMeV value of 389."""
        self._NHitPerMeV = nHitPerMeV
        return
    def GetSigma( self, energy ):
        """ Overloaded version."""
        # Find MeV resolution at this energy
        numHits = self._NHitPerMeV * energy
        # Sigma in NHits is sqrt( numHits ) in energy it is times energy / numHits or 1 / NhitPerMeV
        sigma = math.sqrt( numHits ) / numHits * energy
        return sigma

class EnergyLookup( EnergyResolution ):
    """ Current best RAT energy fitter values."""
    def GetSigma( self, energy ):
        """ Return the resolution at this energy, in MeV."""
        #factor = 0.0375711 + 0.0334513 * energy # Full volume
        factor = 0.0406445 + 0.0217787 * energy # Fiducial Volume cut
        # Find MeV resolution at this energy
        sigma = factor
        return sigma
