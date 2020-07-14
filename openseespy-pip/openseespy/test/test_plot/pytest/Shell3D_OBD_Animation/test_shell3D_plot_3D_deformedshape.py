
import numpy as np
import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opp
import matplotlib.pyplot as plt
from shell3D import RunAnalysis

def test_plot_deformedshape_3D(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)

    RunAnalysis()
    ops.wipe()
    Model = 'test'
    LoadCase = 'Transient'
    LoadCase2 = 'Transient_5s'
    
    # Deformed shape time steps, one that uses an exact step and one that doesn't
    opp.plot_deformedshape(Model, LoadCase, tstep = 3.1231, overlap = 'yes')
    plt.close()
    opp.plot_deformedshape(Model, LoadCase, tstep = 3., overlap = 'yes')
    plt.close()
    opp.plot_deformedshape(Model, LoadCase, tstep = 3.)
    plt.close()
    
    opp.plot_deformedshape(Model, LoadCase2, tstep = 3.1231, overlap = 'yes')
    plt.close()
    opp.plot_deformedshape(Model, LoadCase2, tstep = 3., overlap = 'yes')
    plt.close()
    opp.plot_deformedshape(Model, LoadCase2, tstep = 3.)  
    plt.close()
    assert True == True    
