#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.jones22@physics.ox.ac.uk>

SpectraTypes = {} 

# Register scint backgrounds
import ScintBackgrounds
SpectraTypes["14C"]  = ScintBackgrounds.B14C
SpectraTypes["40K"]  = ScintBackgrounds.B40K
SpectraTypes["39Ar"] = ScintBackgrounds.B39Ar
SpectraTypes["85Kr"] = ScintBackgrounds.B85Kr
# Register Nd backgrounds
import NdBackgrounds
SpectraTypes["150Nd2v"] = NdBackgrounds.B150Nd
SpectraTypes["144Nd"] = NdBackgrounds.B144Nd
SpectraTypes["176Lu"] = NdBackgrounds.B176Lu
SpectraTypes["138La"] = NdBackgrounds.B138La
SpectraTypes["147Sm"] = NdBackgrounds.B147Sm
SpectraTypes["148Sm"] = NdBackgrounds.B148Sm
SpectraTypes["227Ac"] = NdBackgrounds.B227Ac
SpectraTypes["235U"]  = NdBackgrounds.B235U
# Register solar backgrounds/signals
import SolarSignals
SpectraTypes["PEP"] = SolarSignals.SPEP
SpectraTypes["CNO"] = SolarSignals.SCNO
SpectraTypes["B8"]  = SolarSignals.SB8
# Register Nd signal
import NdSignal
SpectraTypes["150Nd0v"] = NdSignal.S150Nd
