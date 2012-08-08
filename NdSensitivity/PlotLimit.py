#!/usr/bin/env python
# Author P G Jones - 10/03/2012 <p.g.jones@qmul.ac.uk>
import ColourUtil
import SimulationSignalLimits
import Simulation
import ConfidenceLevel
import PlotLimits
import PlotSimulation
import PrintSimulation

fileName = raw_input( "File Name:" )

fileLimits = SimulationSignalLimits.DblBetaSignalLimits( Simulation.Simulation(), ConfidenceLevel.TLimitLevel( 0.9 ) )
fileLimits.Load( fileName )
#fileLimits.ConvertToHalfLife()
fileLimits.ConvertToMass()

limitPlotter = PlotLimits.PlotLimits( fileLimits, ColourUtil.DefaultColours() )
limitPlotter.Plot()
simulationPlotter = PlotSimulation.PlotSimulation( fileLimits.GetSimulation(), ColourUtil.DefaultColours() )
simulationPlotter.Plot( 3.0, 0.0, 6.0 )

simulationPrinter = PrintSimulation.PrintSimulation( fileLimits.GetSimulation() )
simulationPrinter.Print( 1.0, 0.0, 5.0 )
raw_input( "RET to exit" )
