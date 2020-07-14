import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np


import ModelFunctions as mf
import AnalysisFunctions as af

# =============================================================================
# Load control with Disp
# =============================================================================

op.wipe()

# Build Model
mf.getSections()
mf.buildModel()

# Prepare Outputs
Model = 'Cantilever'
LoadCase = 'Pushover'
element1 = 1
section1 = 1
element2 = 2
section2 = 3
opp.createODB(Model, LoadCase)
opp.saveFiberData2D(Model, LoadCase, element1, section1)
opp.saveFiberData2D(Model, LoadCase, element2, section2)

# # Run Analysis
af.PushoverLcD(0.05)

op.wipe()

# =============================================================================
# Animation outputs
# =============================================================================

opp.plot_fiberResponse2D(Model, LoadCase, element2, section2, InputType = 'stress', tstep=1)
opp.plot_fiberResponse2D(Model, LoadCase, element1, section1, InputType = 'stress', tstep=1)
ani1 = opp.animate_fiberResponse2D(Model, LoadCase, element1, section1, InputType = 'stress', rFactor = 4)
ani2 = opp.animate_fiberResponse2D(Model, LoadCase, element2, section2, InputType = 'stress', rFactor = 4)