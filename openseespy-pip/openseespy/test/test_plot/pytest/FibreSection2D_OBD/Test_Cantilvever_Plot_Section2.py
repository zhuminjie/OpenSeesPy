import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np
import matplotlib.pyplot as plt

import ModelFunctions as mf
import AnalysisFunctions as af
import MainAnalysis as main

def test_plot_fiberResponse2D_section_2(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    main.RunAnalysis()    
       
    op.wipe()
    
    Model = 'test'
    LoadCase = 'Pushover'
    element2 = 2
    section2 = 3
    
    opp.plot_fiberResponse2D(Model, LoadCase, element2, section2, InputType = 'stress', tstep=1)
    plt.close()
    assert True == True

