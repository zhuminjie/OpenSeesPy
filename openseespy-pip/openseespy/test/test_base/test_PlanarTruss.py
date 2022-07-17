import openseespy.opensees as ops
from math import asin, cos, sin, tan

# Plane 3bar Truss Example

#REFERENCES: 
# 1) Popov, E. "Engineering Mechanics of Solids", Prentice Hall, 1990.
#      Linear: Example 2.14 
#      NonLinear: Example 2.23 

print("=============================================================================")
print("Planar Truss.py: Verification 2d Linear and Nonlinear Truss Example by Popov")
print("  - Linear (Example 2.14)")

# planar 3 bar system, all bars same A & E, unit load P acing
#
def test_PlanarTruss():
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

    # create the finite element model
    ops.wipe()

    ops.model('Basic', '-ndm', 2, '-ndf', 2)

    dX = L*tan(alphaRad)

    ops.node( 1,    0.0,          0.0)
    ops.node( 2,    dX,          0.0)
    ops.node( 3, 2.0*dX,  0.0)
    ops.node( 4,    dX,         -L     )

    ops.fix( 1, 1, 1)
    ops.fix( 2, 1, 1)
    ops.fix( 3, 1, 1)

    ops.uniaxialMaterial('Elastic', 1, E)
    ops.element('Truss', 1, 1, 4, A, 1)
    ops.element('Truss', 2, 2, 4, A, 1)
    ops.element('Truss', 3, 3, 4, A, 1)

    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1)
    ops.load( 4, 0., -P)

    ops.numberer( 'Plain')
    ops.constraints( 'Plain')
    ops.algorithm( 'Linear')
    ops.system('ProfileSPD')
    ops.integrator('LoadControl', 1.0)
    ops.analysis('Static')
    ops.analyze(1)


    # determine PASS/FAILURE of test
    testOK = 0

    #
    # print table of camparsion
    #          

    comparisonResults = F2, F1, F2
    print("\nElement Force Comparison:")
    tol = 1.0e-6
    print('{:>10}{:>15}{:>15}'.format('Element','OpenSees','Popov'))


    for i in range(1,4):
        exactResult = comparisonResults[i-1]
        eleForce = ops.eleResponse(i, 'axialForce')
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



    print("\n\n  - NonLinear (Example2.23)")

    #EXACT
    # Exact per Popov

    PA = (sigmaYP*A) * (1.0+2*cosA*cosA*cosA)
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

    ops.uniaxialMaterial( 'ElasticPP', 1, E, sigmaYP/E)
    ops.element('Truss', 1, 1, 4, A, 1)
    ops.element('Truss', 2, 2, 4, A, 1)
    ops.element('Truss', 3, 3, 4, A, 1)

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
    #print node 4
    #print ele

    ops.analyze(1)
    osDispB = ops.nodeDisp( 4, 2)

    #print node 4
    #print ele


    # determine PASS/FAILURE of test
    testOK = 0

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



