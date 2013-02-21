#!/usr/bin/env python
#
# nd_example.py
#
# Example script to generate, plot and limit set for a Nd Loaded detector.
#
# Author P G Jones - 24/12/2012 <p.g.jones@qmul.ac.uk> : First revision
####################################################################################################
import os
import time
import nd_data_gen
import simulation
import energy_resolution
import signal_rejection
import fiducial_rejection
import pickle
import plot_data
import plot_limits
import limit_calculator
import limit_techniques

detected_data = None
if not os.path.isfile("detected.pkl"):
    start_time = time.clock()
    nd_generator = nd_data_gen.NdDataGen(774000, 0.01)
    raw_data = nd_generator.generate()
    print "Finished generation in", time.clock() - start_time, "s"
    detector_sim = simulation.Simulation("Default Sim", raw_data)
    detector_sim.set_pileup(True)
    detector_sim.set_energy_resolution(energy_resolution.NhitResolution(400.0))
    detector_sim.set_fiducial_rejection(signal_rejection.NoRejection())
    detector_sim.set_rejection(fiducial_rejection.RadialFixedRejection(4500.0))
    detected_data = detector_sim.generate()
    print "Finsihed generation plus simulation in", time.clock() - start_time, "s"
    with open("detected.pkl", "w") as file_:
        pickle.dump(detected_data, file_)
else:
    with open("detected.pkl", "r") as file_:
        detected_data = pickle.load(file_)
plotter = plot_data.DetectedDataPlotter(detected_data, detected_data.get_signal())
plotter.plot(0.0, 6.0)
if not os.path.isfile("limits.pkl"):
    limit_calc = limit_calculator.LimitCalculator(detected_data, limit_techniques.TLimit())#TFeldmanCousins(3.0,3.5))
    limit_set = limit_calc.calculate()
    with open("limits.pkl", "w") as file_:
        pickle.dump(limit_set, file_)
else:
    with open("limits.pkl", "r") as file_:
        limit_set = pickle.load(file_)
limit_plotter = plot_limits.DblBetaLimitPlotter(150, limit_set, None)
limit_plotter.plot_mass(774000 * 0.01 * 0.056, 19.2e-14, 2.4)
raw_input("B")
