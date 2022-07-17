import openseespy.opensees as ops
from math import sin, cos
# Pinched Shell Cylindrical Problem
#Lindberg, G. M. M., D. Olson, and G. R. Cowper, "New Developments in the Finite Element
#AnalysisofShells,"QuarterlyBulletinoftheDivisionofMechanicalEngineeringandtheNational
#AeronauticalEstablishment,NationalResearchCouncilofCanada,vol. 4,1969.

# R = Radius, t= thickness, v = 0.3
# for R/t = 100, v = 0.3, L/R = 2 displacement under load = 164.24 * P / (E * t)
print("=====================================================================")
print("PinchedCantiliver: Validation of Shell Elements with Elastic Sections")

def test_PinchedCylinder():

    P = 1
    R = 300.
    L = 600.
    E = 3e6
    thickness = R/100.

    uExact = -164.24*P/(E*thickness)

    formatString = '{:>20s}{:>15.5e}'
    print("\n  Displacement Under Applied Load:\n")

    formatString = '{:>20s}{:>10s}{:>15s}{:>15s}{:>15s}'
    print(formatString.format("Element Type", "   mesh  ", "OpenSees", "Exact", "%Error"))

    for shellType in ['ShellMITC4', 'ShellDKGQ', 'ShellNLDKGQ']:
        for numEle in [4,16,32]:

            ops.wipe()

            # ----------------------------
            # Start of model generation
            # ----------------------------
            ops.model('basic', '-ndm', 3, '-ndf', 6)
            
            radius = R
            length = L/2.

            
            E = 3.0e6
            v = 0.3
            PI = 3.14159
            
            ops.nDMaterial('ElasticIsotropic', 1, E, v)
            ops.nDMaterial('PlateFiber', 2, 1)
            ops.section('PlateFiber', 1, 2, thickness)
            #section ElasticMembranePlateSection  1   E v thickness 0.
            nR =  numEle
            nY = numEle

            tipNode = (nR+1)*(nY+1)
            
            #create nodes
            nodeTag = 1
            for i in range(nR+1):
                theta = i*PI/(2.0*nR)
                xLoc = 300*cos(theta)
                zLoc = 300*sin(theta)

                for j in range(nY+1):
                    yLoc = j*length/(1.0*nY)
                    ops.node(nodeTag, xLoc, yLoc, zLoc)
                    nodeTag += 1


            #create elements
            eleTag = 1
            for i in range(nR):
                iNode = i*(nY+1)+1
                jNode = iNode +1
                lNode = iNode+(nY+1)
                kNode = lNode+1
                for j in range(nY):
                    ops.element(shellType, eleTag, iNode, jNode, kNode, lNode, 1)
                    eleTag += 1
                    iNode += 1
                    jNode += 1
                    kNode += 1
                    lNode += 1

            # define the boundary conditions
            ops.fixX(radius,  0, 0, 1, 1, 1, 0, '-tol', 1.0e-2)
            ops.fixZ(radius,  1, 0, 0, 0, 1, 1, '-tol', 1.0e-2)
            ops.fixY(      0.,   1, 0, 1, 0, 0, 0, '-tol', 1.0e-2)
            ops.fixY(length,  0, 1, 0, 1, 0, 1, '-tol', 1.0e-2)
            
            #define loads
            ops.timeSeries('Linear', 1)
            ops.pattern('Plain', 1, 1) 
            ops.load(tipNode, 0., 0., -1./4.0, 0., 0., 0.) 
            
            
            ops.integrator('LoadControl',  1.0 )
            ops.test('EnergyIncr',     1.0e-10,    20,       0)
            ops.algorithm('Newton')
            ops.numberer('RCM')
            ops.constraints('Plain') 
            ops.system('Umfpack')
            ops.analysis('Static') 
            
            ops.analyze(1)
            res = ops.nodeDisp(tipNode, 3)
            err = abs(100*(uExact-res)/uExact)
            formatString = '{:>20s}{:>5d}{:>3s}{:>2d}{:>15.5e}{:>15.5e}{:>15.2f}'
            print(formatString.format(shellType, numEle, " x ", numEle, res, uExact, err))


    tol = 5.0
    if abs(100*(uExact-res)/uExact) > tol:
        testOK = 1
    else:
        testOK = 0


    assert testOK == 0

