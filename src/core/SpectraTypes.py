#!/usr/bin/env python
# Author P G Jones - 18/01/2012 <p.g.jones@qmul.ac.uk>
# Convinient background and signal lists, and full listing

SpectraTypes = {} 
SolarSigList = {}
NdBGList = {} # Not the chains
TeBGList = {} # Not the chains
ScintBGList = {} # Not the chains

# Register scint backgrounds
import ScintBackgrounds
SpectraTypes["14C"]  = ScintBackgrounds.B14C
SpectraTypes["40K"]  = ScintBackgrounds.B40K
SpectraTypes["39Ar"] = ScintBackgrounds.B39Ar
SpectraTypes["85Kr"] = ScintBackgrounds.B85Kr
#
ScintBGList["14C"]  = ScintBackgrounds.B14C
ScintBGList["40K"]  = ScintBackgrounds.B40K
ScintBGList["39Ar"] = ScintBackgrounds.B39Ar
ScintBGList["85Kr"] = ScintBackgrounds.B85Kr
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
#
NdBGList["150Nd2v"] = NdBackgrounds.B150Nd
NdBGList["144Nd"] = NdBackgrounds.B144Nd
NdBGList["176Lu"] = NdBackgrounds.B176Lu
NdBGList["138La"] = NdBackgrounds.B138La
NdBGList["147Sm"] = NdBackgrounds.B147Sm
NdBGList["148Sm"] = NdBackgrounds.B148Sm
NdBGList["227Ac"] = NdBackgrounds.B227Ac
NdBGList["235U"]  = NdBackgrounds.B235U
# Register Te backgrounds
import TeBackgrounds
SpectraTypes["130Te2v"] = TeBackgrounds.B130Te
TeBGList["130Te2v"] = TeBackgrounds.B130Te
# Register solar backgrounds/signals
import SolarSignals
SpectraTypes["PEP"] = SolarSignals.SPEP
SpectraTypes["CNO"] = SolarSignals.SCNO
SpectraTypes["B8"]  = SolarSignals.SB8
SpectraTypes["Be7"]  = SolarSignals.SBe7
#
SolarSigList["PEP"] = SolarSignals.SPEP
SolarSigList["CNO"] = SolarSignals.SCNO
SolarSigList["B8"]  = SolarSignals.SB8
SolarSigList["Be7"]  = SolarSignals.SBe7
# Register Nd signal
import NdSignal
SpectraTypes["150Nd0v"] = NdSignal.S150Nd
# Register Te signal
import TeSignal
SpectraTypes["130Te0v"] = TeSignal.S130Te
# Register Chain Backgrounds
import UraniumBackgrounds
SpectraTypes["238UChain"] = UraniumBackgrounds.BUraniumChain
SpectraTypes["238U"] = UraniumBackgrounds.B238U
import ThoriumBackgrounds
SpectraTypes["232ThChain"] = ThoriumBackgrounds.BThoriumChain
SpectraTypes["232Th"] = ThoriumBackgrounds.B232Th
