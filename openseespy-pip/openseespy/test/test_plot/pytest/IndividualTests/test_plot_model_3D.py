import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np
import matplotlib.pyplot as plt


"""
Author: cslotboom
This file tests if the plot_model() functions works for 3D beam, quad and brick elements

"""


def Model_3D():

    op.wipe()
    
    op.model('basic','-ndm',3,'-ndf',6)
    
    mat1 = 1
    op.nDMaterial('ElasticIsotropic',mat1,1.,0.1)
    mat2 = 2
    op.uniaxialMaterial('Elastic',mat2,1.)
    
    
    nodeCoordsx = np.array([0,1,2,3,4])*1.
    nodeCoordsy = np.array([0,1])*1.
    nodeCoordsz = np.array([0,1])*1.
    
    
    # Element connectivity
    element1D = np.array([[1,1,11], [2,2,12], [3,3,13], [4,4,14], [5,5,15],
                          [6,6,16], [7,7,17], [8,8,18], [9,9,19], [10,10,20]])
    element4D = np.array([[21,12,13,18,17], [22,13,14,19,18]])
    element8D = np.array([[30,1,2,7,6,11,12,17,16], [31,4,5,10,9,14,15,20,19]])
    
    elements = [element1D, element4D, element8D]
    
    # Define Nodes
    tag = 0
    for z in nodeCoordsz:
        for y in nodeCoordsy:
            for x in nodeCoordsx:
                tag += 1
                op.node(tag, x, y, z)
    
    
    # Define Elements 2node
    for element in element1D:
        eleTag = int(element[0])
        nodei = int(element[1])
        nodej = int(element[2])
        
        # op.element('elasticBeamColumn', eleTag, *eleNodes, Area, E_mod, Iz, transfTag[, '-mass', massPerLength][, '-cMass'][, '-release', releaseCode])
        # op. element('Truss', eleTag, *eleNodes, A, matTag[, '-rho', rho][, '-cMass', cFlag][, '-doRayleigh', rFlag])
        op.element('Truss', eleTag, nodei, nodej, 1., 2)
        
    
    
    # Define Elements 4node
    for element in element4D:
        eleTag = int(element[0])
        nodei = int(element[1])
        nodej = int(element[2])
        nodek = int(element[3])
        nodel = int(element[4])
        eleNodes = [nodei, nodej, nodek, nodel]
        
        # op.element('FourNodeTetrahedron', eleTag, *eleNodes, matTag[, b1, b2, b3])
        op.element('FourNodeTetrahedron', eleTag, *eleNodes, mat1)
        # op.element('quad', eleTag, nodei, nodej, nodek, nodel, 1., 'PlaneStrain', mat1)
        
    # Define Elements 3node
    for element in element8D:
        eleTag = int(element[0])
        nodei = int(element[1])
        nodej = int(element[2])
        nodek = int(element[3])
        nodel = int(element[4])  
        nodeii = int(element[5])
        nodejj = int(element[6])
        nodekk = int(element[7])
        nodell = int(element[8])
        eleNodes = [nodei, nodej, nodek, nodel, nodeii, nodejj, nodekk, nodell]
    
        op.element('stdBrick', eleTag, *eleNodes, mat1)
        

def test_plot_fn(monkeypatch):
    # repress the show plot attribute
    monkeypatch.setattr(plt, 'show', lambda: None)
    Model_3D()    
    
    opp.plot_model()
    plt.close()
    
    assert True
