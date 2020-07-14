import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np
import matplotlib.pyplot as plt

"""
Author: cslotboom
This file tests if the plot_model() functions works for 2D beam, tri and quad elements

"""





def Model_2D():
    op.wipe()
    
    op.model('basic','-ndm',2,'-ndf',2)
    
    mat1 = 1
    op.nDMaterial('ElasticIsotropic',mat1,1.,0.1)
    mat2 = 2
    op.uniaxialMaterial('Elastic',mat2,1.)
    
    linTransform = 1
    # op.geomTransf('Linear', linTransform)
    
    
    nodeCoordsx = np.array([0,1,2,3])*1.
    nodeCoordsy = np.array([0,1])*1.
    
    
    # Element 1D connectivity
    element1D = np.array([[1,1,5], [2,2,6], [3,3,7], [4,4,8], [5,5,6], [6,6,7], 
                          [7,7,8]])
    element3D = np.array([[10,2,3,6], [11,3,6,7]])
    element4D = np.array([[20,1,2,6,5], [21,3,4,8,7]])
    
    elements = [element1D, element3D, element4D]
    
    # Define Nodes
    tag = 0
    for y in nodeCoordsy:
        for x in nodeCoordsx:
            tag += 1
            op.node(tag, x, y)
    
    
    # Define Elements 2node
    for element in element1D:
        eleTag = int(element[0])
        nodej = int(element[1])
        nodek = int(element[2])
        
        # op. element('Truss', eleTag, *eleNodes, A, matTag[, '-rho', rho][, '-cMass', cFlag][, '-doRayleigh', rFlag])
        op.element('Truss', eleTag, nodej, nodek, 1., 2)
        
        
    # Define Elements 3node
    for element in element3D:
        eleTag = int(element[0])
        nodej = int(element[1])
        nodek = int(element[2])
        nodel = int(element[3])
        # op. element('Tri31', eleTag, *eleNodes, thick, type, matTag[, pressure, rho, b1, b2])
        op.element('Tri31', eleTag, nodej, nodek, nodel, 1., 'PlaneStress', mat1)
    
    # Define Elements 4node
    for element in element4D:
        eleTag = int(element[0])
        nodej = int(element[1])
        nodek = int(element[2])
        nodel = int(element[3])
        nodem = int(element[4])
        
        # op.element('quad', eleTag, *eleNodes, thick, type, matTag[, pressure=0.0, rho=0.0, b1=0.0, b2=0.0])
        op.element('quad', eleTag, nodej, nodek, nodel, nodem, 1., 'PlaneStrain', mat1)

# Model_2D()
# opp.plot_model()

def test_plot_fn(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    Model_2D()    
    
    opp.plot_model()
    plt.close()
    assert True
