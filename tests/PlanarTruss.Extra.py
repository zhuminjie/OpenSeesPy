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

    wipe()
    
    model( 'Basic', '-ndm', 2, '-ndf', 2)
    
    dX = L*tan(alphaRad)
    
    node(1,    0.0,          0.0)
    node(2,    dX ,         0.0)
    node(3,  2.0*dX,  0.0)
    node(4,    dX,         -L     )
    
    fix(1, 1, 1)
    fix(2, 1, 1)
    fix(3, 1, 1)
    
    if sectType == "Uniaxial":
        uniaxialMaterial( 'Elastic', 1, A*E)
        section( 'Uniaxial', 1, 1, 'P')
    else:
        uniaxialMaterial( 'Elastic', 1, E)
        section('Fiber', 1) 	
	#	    patch rect 1 numFiberY numFiberZ [expr -z/2.0] [expr -y/2.0] [expr z/2.0] [expr y/2.0]	    
        patch( 'rect', 1, numFiberY, numFiberZ, -z, -y, 0., 0.)
	

    element('Truss', 1, 1, 4, 1)
    element('Truss', 2, 2, 4, 1)
    element('Truss', 3, 3, 4, 1)
    
    timeSeries( 'Linear', 1)
    pattern( 'Plain', 1, 1) 
    load( 4, 0., -P)
    
    
    numberer( 'Plain')
    constraints( 'Plain')
    algorithm('Linear')
    system('ProfileSPD')
    integrator('LoadControl', 1.0)
    analysis('Static')
    analyze(1)
    
    #
    # print table of camparsion
    #          
    
    comparisonResults = F2, F1, F2
    print("\nElement Force Comparison:")
    tol = 1.0e-6
    print('{:>10}{:>15}{:>15}'.format('Element','OpenSees','Popov'))

    for i in range(1,4):
        exactResult = comparisonResults[i-1]
        eleForce =eleResponse( i, 'axialForce')
        print('{:>10d}{:>15.4f}{:>15.4f}'.format(i, eleForce[0], exactResult))
        if abs(eleForce[0]-exactResult) > tol:
            testOK = -1
            print("failed force-> ", abs(eleForce[0]-exactResult), " ", tol)
    
    print("\nDisplacement Comparison:")
    osDisp = nodeDisp( 4, 2)
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
    
    wipe()
    
    model('Basic', '-ndm', 2, '-ndf', 2)

    node( 1,    0.0,          0.0)
    node( 2,    dX,          0.0)
    node( 3, 2.0*dX,  0.0)
    node( 4,    dX,         -L     )

    fix( 1, 1, 1)
    fix( 2, 1, 1)
    fix( 3, 1, 1)


    if sectType == "Uniaxial":
        uniaxialMaterial( 'ElasticPP', 1, A*E, sigmaYP/E)
        section( 'Uniaxial', 1, 1, 'P')
    else:
        uniaxialMaterial( 'ElasticPP', 1, E, sigmaYP/E)
        section( 'Fiber', 1) 	
        patch( 'rect', 1, numFiberY, numFiberZ, -z/2.0, -y/2.0, z/2.0, y/2.0)


    element('Truss', 1, 1, 4, 1)
    element('Truss', 2, 2, 4, 1)
    element('Truss', 3, 3, 4, 1)

    timeSeries( 'Path', 1, '-dt', 1.0, '-values', 0.0, PA, PB, PB)
    pattern('Plain', 1, 1)
    load( 4, 0., -1.0)
    
    numberer('Plain')
    constraints('Plain')
    algorithm('Linear')
    system('ProfileSPD')
    integrator('LoadControl', 1.0)
    analysis('Static')
    analyze(1)

    osDispA = nodeDisp( 4, 2)
    
    analyze(1)
    osDispB = nodeDisp( 4, 2)
    
    print("\nDisplacement Comparison:")
    print("elastic limit state:")
    osDisp = nodeDisp( 4, 2)
    print('{:>10}{:>15.8f}{:>10}{:>15.8f}'.format('OpenSees:',osDispA,'Exact:',dispA))

    if abs(osDispA-dispA) > tol:
        testOK = -1
        print("failed nonlineaer elastic limit disp")

    print("collapse limit state:")
    print('{:>10}{:>15.8f}{:>10}{:>15.8f}'.format('OpenSees:',osDispB,'Exact:',dispB))

    if abs(osDispB-dispB) > tol:
        testOK = -1
        print("failed nonlineaer collapse limit disp")



if testOK == 0:
    print("\nPASSED Verification Test PlanarTruss.Extra.py \n\n")

else:
    print("\nFAILED Verification Test PlanarTruss.Extra.py \n\n")



