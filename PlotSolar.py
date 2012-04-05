#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk> : First revision
# This script adds all the spectra to a simulation, then calculates pileup backgrounds and then plots the result.
import Simulation
import PlotSimulation
import SpectraTypes
import EnergyResolution
import LogUtil
import ColourUtil
import PrintSimulation

exampleSimulation = Simulation.Simulation( ndLoading = 0.0 ) # No Nd
LogUtil.Verbosity = 2 # Print stuff to the screen
exampleSimulation.AddBackground( SpectraTypes.ScintBGList.keys() ) # Add the scint backgrounds
exampleSimulation.AddBackground( "238UChain" )
exampleSimulation.AddBackground( "232ThChain" )
# Add Solar signals, but designate one as a signal...B
exampleSimulation.AddBackground( "CNO" )
exampleSimulation.AddBackground( "PEP" )
exampleSimulation.AddBackground( "B8" )
exampleSimulation.AddSignal( "Be7" )
# Process the spectra
exampleSimulation.CalculatePileupBackgrounds() # Calculate all the pileup backgrounds (this is slow)
exampleSimulation.ProcessRejection() # Default is no rejection, so this is a waste of time
exampleSimulation.SetEnergyResolution( EnergyResolution.Nhit() ) # Choose the theorectical Nhit based energy resolution
exampleSimulation.ProcessEnergyResolution() # Apply the Nhit energy resolution
#exampleSimulation.Save( "SimulationSolar.pkl" )
#exampleSimulation.Load( "SimulationPileup.pkl" )

# Now the simulation can be plotted, first create a plotter
examplePlotter = PlotSimulation.PlotSimulation( exampleSimulation, ColourUtil.SolarColours() ) # Use the solar colour scheme
examplePlotter.Plot( 1.0, 0.0, 2.5 ) # Plot 1 years data, over the energy domain [0.0, 6.0]MeV
examplePrinter = PrintSimulation.PrintSimulation( exampleSimulation )
examplePrinter.Print( 1.0, 0.0, 6.0 ) # Print 1 years data, over the energy domain [0.0, 6.0]MeV
raw_input( "RET to exit" )
