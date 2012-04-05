#!/usr/bin/env python
# Author P G Jones - 05/04/2012 <p.g.jones@qmul.ac.uk> : First revision
# Convert RAT output files into sno+py format
import ROOT
import rat
import time
import SpectrumUtil
import RadialUtil

def ExtractData( fileName ):
    """ Extracts the data from the file, into the useful TH2D format of x=energy y=radius."""
    dataResult = ROOT.TH2D( "Spectra", "Energy Radial Data", SpectrumUtil.NBins, SpectrumUtil.LowBin, SpectrumUtil.HighBin, RadialUtil.NBins, RadialUtil.LowBin, RadialUtil.HighBin )
    for ds in rat.dsreader( fileName ):
        radius = ds.GetMC().GetMCParticle(0).GetPos().Mag()
        energy = ds.GetMC().GetTotScintEdepQuenched()
        dataResult.Fill( energy, radius )
    return dataResult

def SaveData( fileName, data ):
    """ Saves the TH2D, data into the file, fileName."""
    outFile = ROOT.TFile( fileName, "RECREATE" )
    data.Write()
    outFile.Close()

import optparse
if __name__ == '__main__':
    parser = optparse.OptionParser( usage = "usage: %prog input output", version="%prog 1.0" )
    (options, args) = parser.parse_args()
    if len( args ) != 2:
        parser.print_help()
    data = ExtractData( args[0] )
    SaveData( args[1], data )
