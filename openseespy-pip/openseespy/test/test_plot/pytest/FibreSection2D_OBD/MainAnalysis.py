import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np
import matplotlib.pyplot as plt

import ModelFunctions as mf
import AnalysisFunctions as af

# =============================================================================
# Load control with Disp
# =============================================================================

def RunAnalysis():
    op.wipe()
    
    # Build Model
    mf.getSections()
    mf.buildModel()
    
    # Prepare Outputs
    Model = 'test'
    LoadCase = 'Pushover'
    element1 = 1
    section1 = 1
    element2 = 2
    section2 = 3
    opp.createODB(Model, LoadCase)
    opp.saveFiberData2D(Model, LoadCase, element1, section1)
    opp.saveFiberData2D(Model, LoadCase, element2, section2)
    
    # Run Analysis
    af.PushoverLcD(0.001)
    
    op.wipe()

