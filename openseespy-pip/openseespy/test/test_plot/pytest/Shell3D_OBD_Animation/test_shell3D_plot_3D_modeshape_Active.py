
import numpy as np
import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opp
import matplotlib.pyplot as plt
from shell3D import RunAnalysis

    
def test_plot_modeshape_3D_Active(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)

    RunAnalysis()    
    opp.plot_modeshape(1, 200)
    plt.close()
    opp.plot_modeshape(2, 200)    
    plt.close()
    assert True == True    