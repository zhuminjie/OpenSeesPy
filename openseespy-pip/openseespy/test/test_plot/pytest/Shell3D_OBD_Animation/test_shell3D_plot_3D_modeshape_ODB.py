
import numpy as np
import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opp
import matplotlib.pyplot as plt
from shell3D import RunAnalysis


def test_plot_model_3D_ODB(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    
    RunAnalysis()
    ops.wipe()
    Model = 'test'
    opp.plot_model('nodes','elements',Model = Model)
    plt.close()
    assert True == True
