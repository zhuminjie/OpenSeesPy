
import openseespy.opensees as op
import openseespy.postprocessing.Get_Rendering as opp
import numpy as np


m = 1
mm = 0.001*m

Pa = 1.
MPa = 10**6*Pa
GPa = 10**9*Pa


def getSections():
    
    op.model('Basic', '-ndm', 2, '-ndf', 3)
    
    # Get material prorpeties
    Esteel = 200.*GPa
    Eflex = 1.
    Erigid = 100.*10**12
    
    # define materials
    op.uniaxialMaterial('Elastic', 1, Esteel)
    op.uniaxialMaterial('Elastic', 10, Eflex)
    op.uniaxialMaterial('Elastic', 20, Erigid)
    
    # Define Steel Material
    Fy = 350.*MPa
    E0 = 200.*GPa
    b = 0.0005
    
    #  uniaxialMaterial('Steel02', matTag, Fy, E0, b)    
    op.uniaxialMaterial('Steel02', 2, Fy, E0, b)    
    
    fpc = -30.*10**6
    fpcu = fpc*0.1
    epsc0 = -0.002
    epsU = epsc0*8
    lam = 0.2
    ft = -fpc/30
    Ets = 2*fpc / (epsc0 * 20)
    
    # Define Concrete Material
    #  uniaxialMaterial('Concrete02', matTag, fpc, epsc0, fpcu, epsU, lambda, ft, Ets)    
    op.uniaxialMaterial('Concrete02', 3, fpc, epsc0, fpcu, epsU, lam, ft, Ets)    
    
    # Geometry preprocessing   
    # Get Verticies
    h = 600*mm
    w = 400*mm
    vertices = np.array([-h/2, w/2, -h/2, -w/2, h/2, -w/2, h/2, w/2])
    
    # Define Rebar Info
    rebarZ = np.array([-150, 0, 150])*mm
    rebarY = np.array([150, 225])*mm
    Abar = np.pi*(30*mm/2)**2
    
    Nbar = len(rebarZ)*len(rebarY)
    rebarYZ = np.zeros([Nbar,2])

    for ii, Y in enumerate(rebarY):
        for jj, Z in enumerate(rebarZ):
            rebarYZ[ii*len(rebarZ) + jj, :] = [Y, Z]
         
    NfibeZ = 1
    NfibeY = 100         
            
    # Define Sections
    # Test Sections
    #  section('Fiber', secTag)
    op.section('Fiber', 1)
    
    #  patch('quad', matTag, numSubdivIJ, numSubdivJK, *crdsI, *crdsJ, *crdsK, *crdsL)
    op.patch('quad', 1, NfibeZ, NfibeY, *vertices)
    
    for YZ in rebarYZ:       
        #  fiber(yloc, zloc, A, matTag)
        op.fiber(*YZ, Abar, 1)
    
    # Actual Section
    #  section('Fiber', secTag)
    op.section('Fiber', 2)
    
    #  patch('quad', matTag, numSubdivIJ, numSubdivJK, *crdsI, *crdsJ, *crdsK, *crdsL)
    op.patch('quad', 3, NfibeZ, NfibeY, *vertices)
    
    for YZ in rebarYZ:       
        #  fiber(yloc, zloc, A, matTag)
        op.fiber(*YZ, Abar, 2)
        
    
    # Define transform and integration
    op.geomTransf('Linear', 1)
    op.geomTransf('PDelta', 2)
    
    #  beamIntegration('Lobatto', tag, secTag, N)
    op.beamIntegration('Lobatto', 1, 1, 4)
    op.beamIntegration('Lobatto', 2, 2, 4)
    
    
    
    return rebarYZ





def buildModel():   
    
    nodeX = np.array([0.,0.,0.,0.])
    nodeY = np.array([0.,1.,2.,3.])

    Nnode = len(nodeX)   
    
    # Define Nodes
    for ii in range(Nnode):
        tag = int(ii + 1)
        
        op.node(tag, nodeX[ii],nodeY[ii])
    
    # Assign boundary constraints
    op.fix(1,1,1,1)
    
    # define Element
    #  element('forceBeamColumn', eleTag, *eleNodes, transfTag, integrationTag, '-iter', maxIter=10, tol=1e-12, '-mass', mass=0.0)
    op.element('forceBeamColumn', 1, *[1,2], 1, 2, '-iter', 30, 1e-12)
    op.element('forceBeamColumn', 2, *[2,3], 1, 2, '-iter', 30, 1e-12)
    op.element('forceBeamColumn', 3, *[3,4], 1, 2, '-iter', 30, 1e-12)


    pass

