import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np
import matplotlib.pyplot as plt

import ModelFunctions as mf
import AnalysisFunctions as af
import MainAnalysis as main

def test_plot_fiberResponse2D_section_1(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    main.RunAnalysis()    
       
    op.wipe()
    
    Model = 'test'
    LoadCase = 'Pushover'
    element1 = 1
    section1 = 1
    
    opp.plot_fiberResponse2D(Model, LoadCase, element1, section1, InputType = 'stress', tstep=1)
    plt.close()
    assert True == True
