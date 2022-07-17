import openseespy.opensees as ops
print("==========================================")
print("Start Eigen analysis of a two-storey shear frame")
import math
import os
# Eigen analysis of a two-storey shear frame; Example 10.4 from "Dynamics of Structures" book by Anil Chopra - using equalDOF and very high Ib

# units: in, kips
def test_EigenAnal_twoStoryShearFrame7():
    ops.wipe()

    #input
    m =  100.0/386.0
    numModes = 2

    #material
    Ac = 63.41
    Ic = 320.0
    E = 30000.0
    Ib = 10e+12
    Ab = 63.41

    #geometry
    L = 288.
    h = 144.

    # define the model
    #---------------------------------
    #model builder
    ops.model('BasicBuilder', '-ndm', 2, '-ndf', 3)					

    # nodal coordinates:
    ops.node(1,   0.,  0.) 
    ops.node(2,   L,  0. )
    ops.node(3,   0.,  h )
    ops.node(4,   L,  h )
    ops.node(5,   0.,   2*h)
    ops.node(6,   L,   2*h)

    # Single point constraints -- Boundary Conditions
    ops.fix(1, 1, 1, 1)
    ops.fix(2, 1, 1, 1)

    # MP constraints
    ops.equalDOF(3, 4, 2, 3)
    ops.equalDOF(5, 6, 2, 3)

    # assign mass
    ops.mass(3, m, 0., 0. )
    ops.mass(4, m, 0., 0. )
    ops.mass(5,  m/2., 0., 0. )
    ops.mass(6,  m/2., 0., 0. )

    # define geometric transformation:
    TransfTag = 1
    ops.geomTransf('Linear', TransfTag )

    # define elements:
    # columns
    ops.element('elasticBeamColumn',1, 1, 3, Ac, E,   2.*Ic, TransfTag)
    ops.element('elasticBeamColumn',2, 3, 5, Ac, E,  Ic   ,        TransfTag)
    ops.element('elasticBeamColumn',3, 2, 4, Ac, E,   2.*Ic, TransfTag)
    ops.element('elasticBeamColumn',4, 4, 6, Ac, E,  Ic     ,      TransfTag)
    # beams
    ops.element('elasticBeamColumn',5, 3, 4, Ab, E,  Ib      ,     TransfTag)
    ops.element('elasticBeamColumn',6, 5, 6, Ab, E,  Ib       ,    TransfTag)

    # record eigenvectors
    #----------------------
    # for { k 1 } { k <= numModes } { incr k } {
    #     recorder Node -file format "modes/mode%i.out" k -nodeRange 1 6 -dof 1 2 3  "eigen k"
    # }

    # perform eigen analysis
    #-----------------------------
    lamb = ops.eigen(numModes)

    # calculate frequencies and periods of the structure
    #---------------------------------------------------
    omega = []
    f = []
    T = []
    pi = 3.141593


    for lam in lamb :
        print("labmbda = ", lam)
        omega.append(math.sqrt(lam))
        f.append(math.sqrt(lam)/(2*pi))
        T.append((2*pi)/math.sqrt(lam))


    print("periods are ", T)

    # write the output file cosisting of periods
    #--------------------------------------------
    period = "Periods.txt"
    Periods = open(period, "w")
    for t in T:
        Periods.write(repr(t)+'\n')
        
    Periods.close()


    # create display  for mode shapes
    #---------------------------------
    #                 windowTitle xLoc yLoc xPixels yPixels
    # recorder display "Mode Shape 1"  10    10     500      500     -wipe  
    # prp h h 1                                         # projection reference point (prp) defines the center of projection (viewer eye)
    # vup  0  1 0                                         # view-up vector (vup) 
    # vpn  0  0 1                                         # view-plane normal (vpn)     
    # viewWindow -200 200 -200 200                        # coordiantes of the window relative to prp  
    # display -1 5 20 
    # the 1st arg. is the tag for display mode (ex. -1 is for the first mode shape)
                                                        # the 2nd arg. is magnification factor for nodes, the 3rd arg. is magnif. factor of deformed shape
    # recorder display "Mode Shape 2" 10 510 500 500 -wipe
    # prp h h 1
    # vup  0  1 0
    # vpn  0  0 1
    # viewWindow -200 200 -200 200
    # display -2 5 20


    # Run a one step gravity load with no loading (to record eigenvectors)
    #-----------------------------------------------------------------------
    ops.integrator('LoadControl', 0.0, 1, 0.0, 0.0)

    # Convergence test
    #                     tolerance maxIter displayCode
    ops.test('EnergyIncr',    1.0e-10,    100,        0)

    # Solution algorithm
    ops.algorithm('Newton')

    # DOF numberer
    ops.numberer('RCM')

    # Constraint handler
    ops.constraints('Transformation')


    # System of equations solver
    ops.system('ProfileSPD')

    ops.analysis('Static')
    res = ops.analyze(1)
    if res < 0:
        print("Modal analysis failed")


    # get values of eigenvectors for translational DOFs
    #---------------------------------------------------
    f11 = ops.nodeEigenvector(3, 1, 1)
    f21 = ops.nodeEigenvector(5, 1, 1)
    f12 = ops.nodeEigenvector(3, 2, 1)
    f22 = ops.nodeEigenvector(5, 2, 1)
    print("eigenvector 1: ",  [f11/f21, f21/f21])
    print("eigenvector 2: ",  [f12/f22, f22/f22])

    assert abs(T[0]-0.5148773207872785)<1e-12 and abs(T[1]-0.25743866038265584)<1e-12 and abs(f11/f21-0.49999999998933464)<1e-12 and abs(f21/f21-1.0)<1e-12 and abs(f12/f22+1.0000000000213303)<1e-12 and abs(f22/f22-1.0)<1e-12
    print("==========================================")
