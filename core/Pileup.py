#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# Calculates the pileup background shapes and rates
import SignalRejection
import Spectra
import PileupBackground
import MathUtil
import SpectrumUtil
import LogUtil

kns = 1e-9 # ns in seconds

def Pileup( backgrounds, pileupWindow, rejection ):
    """ Pileup all the backgrounds together within the pileup window whilst rejecting events."""
    assert( isinstance( rejection, SignalRejection.SignalRejection ) )
    pileupBackgrounds = []
    for bg1 in backgrounds:
        LogUtil.Log( bg1.GetName(), 1 )
        for bg2 in backgrounds:
            # Single Pileup here
            LogUtil.Log( "  +" + bg2.GetName(), 1 )
            activity = SinglePileupActivity( bg1, bg2, pileupWindow )
            if activity > 1:
                pileupBackgrounds.append( SinglePileupSpectra( bg1, bg2, activity, rejection ) )
                #bg1.AddPileupEvents( activity ) # Or k=0...
                #bg2.AddPileupEvents( activity )
            for bg3 in backgrounds:
                LogUtil.Log( "    ++" + bg3.GetName(), 1 )
                # Double Pileup here
                activity = DoublePileupActivity( bg1, bg2, bg3, pileupWindow )
                if activity > 1:
                    pileupBackgrounds.append( DoublePileupSpectra( bg1, bg2, bg3, activity, rejection ) )
                    #bg1.AddPileupEvents( activity )
                    #bg2.AddPileupEvents( activity )
                    #bg3.AddPileupEvents( activity )
            # Triple Pileup is currently neglected
    # Must now remove the duplicate or double counted backgrounds
    pileupBackgrounds = set( pileupBackgrounds )
    # Now add to backgrounds list
    backgrounds.extend( pileupBackgrounds )
    return backgrounds

def SinglePileupActivity( bg1, bg2, pileupWindow ):
    """ Return the number of events per year for single pileup."""
    global kns
    assert( isinstance( bg1, Spectra.Spectra ) )
    assert( isinstance( bg2, Spectra.Spectra ) )
    return bg1.GetActivity() * MathUtil.PoissonValue( bg2.GetActivity() * pileupWindow * kns / YearToSeconds(), 1 )

def DoublePileupActivity( bg1, bg2, bg3, pileupWindow ):
    """ Return the number of events per year for double pileup."""
    global kns
    assert( isinstance( bg1, Spectra.Spectra ) )
    assert( isinstance( bg2, Spectra.Spectra ) )
    assert( isinstance( bg3, Spectra.Spectra ) )
    if bg2 == bg3:
        return bg1.GetActivity() * MathUtil.PoissonValue( bg2.GetActivity() * pileupWindow * kns / YearToSeconds(), 2 )
    else:
        return bg1.GetActivity() * MathUtil.PoissonValue( bg2.GetActivity() * pileupWindow * kns / YearToSeconds(), 1 ) \
                                 * MathUtil.PoissonValue( bg3.GetActivity() * pileupWindow * kns / YearToSeconds(), 1 )
    return

def YearToSeconds():
    """ A Year in Seconds."""
    return 365.25 * 24 * 60 * 60

def SinglePileupSpectra( bg1, bg2, activity, rejection ):
    """ Produce a single pileup spectra from the two backgrounds, the activity and the rejection."""
    hist1 = bg1.GetHist()
    hist2 = bg2.GetHist()
    convolved = ConvolveReject( hist1, hist2, rejection )
    convolved.Scale( activity / convolved.GetSumOfWeights() )
    newBackground = PileupBackground.PileupBackground( bg1.GetName() + "+" + bg2.GetName(), 1, convolved, activity, bg1._DetectorInfo )
    return newBackground

def DoublePileupSpectra( bg1, bg2, bg3, activity, rejection ):
    """ Produce a double pileup spectra from the three backgrounds, the activity and the rejection."""
    hist1 = bg1.GetHist()
    hist2 = bg2.GetHist()
    hist3 = bg3.GetHist()
    # PHIL Rejection levels are not correct in this method
    convolved = ConvolveReject( hist1, hist2, rejection )
    convolved = ConvolveReject( convolved, hist3, rejection )
    convolved.Scale( activity / convolved.GetSumOfWeights() )
    newBackground = PileupBackground.PileupBackground( bg1.GetName() + "+" + bg2.GetName() + "+" + bg3.GetName(), 2, convolved, activity, bg1._DetectorInfo )
    return newBackground

def ConvolveReject( hist1, hist2, rejection ):
    """ Convole two histograms with a rejection level."""
    convolved = SpectrumUtil.RawSpectrum( "Convolved" )
    # (c)(b1) = sum(b2) h1(b2) * h2( b1 - b2 )
    for b1 in range( 1, SpectrumUtil.NBins + 1 ):
        h = 0.0
        for b2 in range( 1, SpectrumUtil.NBins + 1 ):
            diff = b1 - b2
            if diff >= 1 and diff <= SpectrumUtil.NBins:
                survivalFactor = rejection.GetPileupSurvivalFactor( hist1.GetXaxis().GetBinCenter( b2 ), hist2.GetXaxis().GetBinCenter( diff ) )
                h = h + hist1.GetBinContent( b2 ) * hist2.GetBinContent( diff ) * survivalFactor
        convolved.SetBinContent( b1, h )
    return convolved
