import openseespy.opensees as ops
from math import tan, asin, cos, sin
# This Extends PlanarTruss.py verification test to:
#   1) run different element options to test: TrussSection and FiberSection2d And Uniaxial Section
#   2) run different solver options to test:

# Plane 3bar Truss Example

#REFERENCES: 
#     as per PlanarTruss.py

print("=============================================================================")
print("Planar Truss.py: Verification 2d Linear and Nonlinear Truss Example by Popov")

# planar 3 bar system, all bars same A & E, unit load P acing
#
def test_PlanarTrussExtra():
    A = 10.0
    E = 3000.
    L = 200.0
    alpha = 30.0
    P = 200.0

    sigmaYP = 60.0

    pi = 2.0*asin(1.0)
    alphaRad = alpha*pi/180.
    cosA = cos(alphaRad)
    sinA = sin(alphaRad)


    # EXACT RESULTS per Popov
    F1 = P/(2*cosA*cosA*cosA + 1)
    F2 = F1*cosA*cosA
    disp = -F1*L/(A*E)


    b = 1.0
    d = A
    z = A
    y = 1.0

    numFiberY = 10  # note we only need so many to get the required accuracy on eigenvalue 1e-7!
    numFiberZ = 1

    # create the finite element model
    for sectType in ['Fiber', 'Uniaxial']:

        print("  - Linear (Example 2.14) sectType: ", sectType)
        
        testOK = 0

        ops.wipe()
        
        ops.model( 'Basic', '-ndm', 2, '-ndf', 2)
        
        dX = L*tan(alphaRad)
        
        ops.node(1,    0.0,          0.0)
        ops.node(2,    dX ,         0.0)
        ops.node(3,  2.0*dX,  0.0)
        ops.node(4,    dX,         -L     )
        
        ops.fix(1, 1, 1)
        ops.fix(2, 1, 1)
        ops.fix(3, 1, 1)
        
        if sectType == "Uniaxial":
            ops.uniaxialMaterial( 'Elastic', 1, A*E)
            ops.section( 'Uniaxial', 1, 1, 'P')
        else:
            ops.uniaxialMaterial( 'Elastic', 1, E)
            ops.section('Fiber', 1) 	
        #	    patch rect 1 numFiberY numFiberZ [expr -z/2.0] [expr -y/2.0] [expr z/2.0] [expr y/2.0]	    
            ops.patch( 'rect', 1, numFiberY, numFiberZ, -z, -y, 0., 0.)
        

        ops.element('Truss', 1, 1, 4, 1)
        ops.element('Truss', 2, 2, 4, 1)
        ops.element('Truss', 3, 3, 4, 1)
        
        ops.timeSeries( 'Linear', 1)
        ops.pattern( 'Plain', 1, 1) 
        ops.load( 4, 0., -P)
        
        
        ops.numberer( 'Plain')
        ops.constraints( 'Plain')
        ops.algorithm('Linear')
        ops.system('ProfileSPD')
        ops.integrator('LoadControl', 1.0)
        ops.analysis('Static')
        ops.analyze(1)
        
        #
        # print table of camparsion
        #          
        
        comparisonResults = F2, F1, F2
        print("\nElement Force Comparison:")
        tol = 1.0e-6
        print('{:>10}{:>15}{:>15}'.format('Element','OpenSees','Popov'))

        for i in range(1,4):
            exactResult = comparisonResults[i-1]
            eleForce =ops.eleResponse( i, 'axialForce')
            print('{:>10d}{:>15.4f}{:>15.4f}'.format(i, eleForce[0], exactResult))
            if abs(eleForce[0]-exactResult) > tol:
                testOK = -1
                print("failed force-> ", abs(eleForce[0]-exactResult), " ", tol)
        
        print("\nDisplacement Comparison:")
        osDisp = ops.nodeDisp( 4, 2)
        print('{:>10}{:>15.8f}{:>10}{:>15.8f}'.format('OpenSees:',osDisp,'Exact:', disp))
        if abs(osDisp-disp) > tol:
            testOK = -1
            print("failed linear disp")
        
        print("\n\n  - NonLinear (Example2.23) sectType: ", sectType)
        
        #EXACT
        # Exact per Popov
        
        PA =  (sigmaYP*A) * (1.0+2*cosA*cosA*cosA)
        dispA = PA/P*disp
        
        PB = (sigmaYP*A) * (1.0+2*cosA)
        dispB = dispA / (cosA*cosA)
        
        # create the new finite element model for nonlinear case
        #   will apply failure loads and calculate displacements
        
        ops.wipe()
        
        ops.model('Basic', '-ndm', 2, '-ndf', 2)

        ops.node( 1,    0.0,          0.0)
        ops.node( 2,    dX,          0.0)
        ops.node( 3, 2.0*dX,  0.0)
        ops.node( 4,    dX,         -L     )

        ops.fix( 1, 1, 1)
        ops.fix( 2, 1, 1)
        ops.fix( 3, 1, 1)


        if sectType == "Uniaxial":
            ops.uniaxialMaterial( 'ElasticPP', 1, A*E, sigmaYP/E)
            ops.section( 'Uniaxial', 1, 1, 'P')
        else:
            ops.uniaxialMaterial( 'ElasticPP', 1, E, sigmaYP/E)
            ops.section( 'Fiber', 1) 	
            ops.patch( 'rect', 1, numFiberY, numFiberZ, -z/2.0, -y/2.0, z/2.0, y/2.0)


        ops.element('Truss', 1, 1, 4, 1)
        ops.element('Truss', 2, 2, 4, 1)
        ops.element('Truss', 3, 3, 4, 1)

        ops.timeSeries( 'Path', 1, '-dt', 1.0, '-values', 0.0, PA, PB, PB)
        ops.pattern('Plain', 1, 1)
        ops.load( 4, 0., -1.0)
        
        ops.numberer('Plain')
        ops.constraints('Plain')
        ops.algorithm('Linear')
        ops.system('ProfileSPD')
        ops.integrator('LoadControl', 1.0)
        ops.analysis('Static')
        ops.analyze(1)

        osDispA = ops.nodeDisp( 4, 2)
        
        ops.analyze(1)
        osDispB = ops.nodeDisp( 4, 2)
        
        print("\nDisplacement Comparison:")
        print("elastic limit state:")
        osDisp = ops.nodeDisp( 4, 2)
        print('{:>10}{:>15.8f}{:>10}{:>15.8f}'.format('OpenSees:',osDispA,'Exact:',dispA))

        if abs(osDispA-dispA) > tol:
            testOK = -1
            print("failed nonlineaer elastic limit disp")

        print("collapse limit state:")
        print('{:>10}{:>15.8f}{:>10}{:>15.8f}'.format('OpenSees:',osDispB,'Exact:',dispB))

        if abs(osDispB-dispB) > tol:
            testOK = -1
            print("failed nonlineaer collapse limit disp")



    assert testOK == 0



