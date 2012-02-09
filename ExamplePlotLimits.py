#!/usr/bin/env python
# Author P G Jones - 24/01/2012 <p.g.jones@qmul.ac.uk>
# This script adds all the spectra to a simulation, then calculates pileup backgrounds, then calculates the limits and then plots them.
import Simulation
import PlotSimulation
import SpectraTypes
import EnergyResolution
import ConfidenceLevel
import SimulationSignalLimits
import LogUtil
import PlotLimits
import ColourUtil

exampleSimulation = Simulation.Simulation()
LogUtil.Verbosity = 2 # Print stuff to the screen
#allBackgroundsList = SpectraTypes.SpectraTypes.keys() # List of all the available spectra
#allBackgroundsList.remove( "150Nd0v" ) # Remove the signal
#exampleSimulation.AddBackground( allBackgroundsList ) # Can also do this individually
#exampleSimulation.AddSignal( "150Nd0v" ) # Add the signal specially
#exampleSimulation.CalculatePileupBackgrounds() # Calculate all the pileup backgrounds (this is slow)
#exampleSimulation.ProcessRejection() # Default is no rejection, so this is a waste of time
#exampleSimulation.SetEnergyResolution( EnergyResolution.Nhit() ) # Choose the theorectical Nhit based energy resolution
#exampleSimulation.ProcessEnergyResolution() # Apply the Nhit energy resolution

exampleSimulation.Load( "SimulationNoPileup.pkl" )

# Now calculate the limits using the TLimit confidence level
tLimitCL = ConfidenceLevel.TLimitLevel( 0.9 )
exampleLimits = SimulationSignalLimits.NdSignalLimits( exampleSimulation, tLimitCL )
#exampleLimits.CalculateLimits( [1.0, 2.0, 3.0, 4.0, 5.0] )
#exampleLimits.Save( "Limits.pkl" )
exampleLimits.Load( "Limits.pkl" )
exampleLimits.ConvertToHalfLife()

# Now plot these limits, first create a plotter
examplePlotter = PlotLimits.PlotLimits( exampleLimits, ColourUtil.DefaultColours() )
examplePlotter.Plot()
raw_input( "RET to exit" )
