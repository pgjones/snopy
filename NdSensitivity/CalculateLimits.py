#!/usr/bin/env python
# Author P G Jones - 06/08/2012 <p.g.jones@qmul.ac.uk>
# Calculate Nd loaded SNO+ limits under SNO+Py and Nassim assumptions
import Simulation
import SpectraTypes
import EnergyResolution
import ConfidenceLevel
import SimulationSignalLimits
import LogUtil
import Rejection


def CalcLimits( name, loading, signal, rejection ):
    """ Calculate the limits for Nd loading of loading with signal and rejection and save into name.pkl."""
    ndSimulation = Simulation.Simulation( ndLoading = loading, fiducialRadius = 0.8 * 6000.0 )
    allBackgroundsList = SpectraTypes.ScintBGList.keys()
    allBackgroundsList.extend( SpectraTypes.NdBGList.keys() )
    allBackgroundsList.extend( SpectraTypes.SolarSigList.keys() )
    allBackgroundsList.append( "232ThChain" )
    allBackgroundsList.append( "238UChain" )
    ndSimulation.AddBackground( allBackgroundsList )
    ndSimulation.AddSignal( signal )
    ndSimulation.SetSignalRejection( rejection )
    ndSimulation.ProcessRejection()
    if loading == 0.1:
        ndSimulation.SetEnergyResolution( EnergyResolution.Nhit( 400 ) )
    elif loading == 0.3:
        ndSimulation.SetEnergyResolution( EnergyResolution.Nhit( 200 ) )
    else:
        raise Exception( "No Nhit known for loading." )
    ndSimulation.ProcessEnergyResolution()

    tLimitCL = ConfidenceLevel.TLimitLevel( 0.9 )
    exampleLimits = SimulationSignalLimits.DblBetaSignalLimits( ndSimulation, tLimitCL )
    exampleLimits.CalculateLimits( [1.0, 2.0, 3.0, 4.0] )
    exampleLimits.Save( name + ".pkl" )
    return

if __name__ == '__main__':
    LogUtil.Verbosity = 1
    nassimSignal = SpectraTypes.SpectraTypes["150Nd0v"]()
    nassimSignal._G = 2.69e-13 # yr
    nassimSignal._NME = 2.5
    nassimSignal._mass = 350e-3
    nassimSignal.Initialise()
    CalcLimits( "NdNassim1", 0.1, nassimSignal, Rejection.NassimRejection() )
    CalcLimits( "NdNassim3", 0.3, nassimSignal, Rejection.NassimRejection() )
    snopySignal = SpectraTypes.SpectraTypes["150Nd0v"]()
    snopySignal.Initialise()
    CalcLimits( "Nd1", 0.1, snopySignal, Rejection.SNOPyRejection() )
    CalcLimits( "Nd3", 0.3, snopySignal, Rejection.SNOPyRejection() )
