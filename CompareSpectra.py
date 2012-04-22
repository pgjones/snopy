#!/usr/bin/env python
# Author P G Jones - 19/04/2012 <p.g.jones@qmul.ac.uk> : First revision
# Plot the extracted RAT format spectra against the analytic spectra.
import SpectraTypes
import DetectorInfo
import ROOT

def PlotSpectra( bgName, fileName ):
    """ Plot the spectra for background bgName both analytically and from the file, fileName."""
    analyticBG = SpectraTypes.SpectraTypes[ bgName ]()
    analyticBG.Initialise()
    fileBG = SpectraTypes.SpectraTypes[ bgName ]()
    fileBG.ImportSpectra( fileName )
    detectorInfo = DetectorInfo.DetectorInfo( 774000.0,
                                              0.01 / 100.0 * 774000.0,
                                              0.3 / 100.0 * 774000.0,
                                              6000.0 ) # In mm
    analyticBG.SetDetectorInfo( detectorInfo )
    fileBG.SetDetectorInfo( detectorInfo )

    c1 = ROOT.TCanvas()
    hists = [ analyticBG.NewHist( 1.0 ), fileBG.NewHist( 1.0 ) ]
    hists[0].Draw()
    hists[1].SetLineColor( ROOT.kRed )
    hists[1].Draw("SAME")
    c1.Update()
    raw_input( "RET to exit." )

import optparse
if __name__ == '__main__':
    parser = optparse.OptionParser( usage = "usage: %prog bg fileName", version="%prog 1.0" )
    (options, args) = parser.parse_args()
    if len( args ) != 2:
        parser.print_help()
    PlotSpectra( args[0], args[1] )
    
