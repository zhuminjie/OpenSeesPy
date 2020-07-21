
import numpy as np
import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opp
import matplotlib.pyplot as plt
from shell3D import RunAnalysis


def test_animate_deformedshape_3D(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)

    RunAnalysis()
    
    ops.wipe()
    dt = 0.2
    Model = 'test'
    LoadCase = 'Transient'
    
    ani = opp.animate_deformedshape( Model, LoadCase, dt, scale=30)
    plt.close()
    assert True == True 