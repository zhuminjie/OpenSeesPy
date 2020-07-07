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
    Model = 'Cantilever'
    LoadCase = 'Pushover'
    element1 = 1
    section1 = 1
    element2 = 2
    section2 = 3
    opp.createODB(Model, LoadCase)
    opp.saveFiberData2D(Model, LoadCase, element1, section1)
    opp.saveFiberData2D(Model, LoadCase, element2, section2)
    
    # Run Analysis
    af.PushoverLcD(0.01)
    
    op.wipe()



# =============================================================================
# Animation outputs
# =============================================================================

def test_plot_fiberResponse2D(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    RunAnalysis()    
       
    op.wipe()
    
    Model = 'Cantilever'
    LoadCase = 'Pushover'
    element1 = 1
    section1 = 1
    element2 = 2
    section2 = 3
    
    opp.plot_fiberResponse2D(Model, LoadCase, element2, section2, InputType = 'stress', tstep=1)
    opp.plot_fiberResponse2D(Model, LoadCase, element1, section1, InputType = 'stress', tstep=1)
    assert True == True


def test_animate_fiberResponse2D(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    RunAnalysis()    
       
    op.wipe()
    
    Model = 'Cantilever'
    LoadCase = 'Pushover'
    element1 = 1
    section1 = 1
    element2 = 2
    section2 = 3
    
    ani1 = opp.animate_fiberResponse2D(Model, LoadCase, element1, section1, InputType = 'stress', rFactor = 4)
    ani2 = opp.animate_fiberResponse2D(Model, LoadCase, element2, section2, InputType = 'stress', rFactor = 4)
    assert True == True

