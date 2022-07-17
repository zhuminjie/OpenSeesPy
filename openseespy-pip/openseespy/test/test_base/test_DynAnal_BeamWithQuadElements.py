import openseespy.opensees as ops
# OpenSees Example: Simple supported beam modeled with 2D solid elements

# Units: kips, in, sec
# ----------------------------

print("========================================")
print("Start Simple supported beam modeled with 2D solid elements example")
from math import sqrt

def test_DynAnal_BeamWithQuadElements():

    ops.wipe() # clear opensees model

    # create data directory
    # file mkdir Data

    #-----------------------------
    # Define the model
    # ----------------------------

    # Create ModelBuilder with 2 dimensions and 2 DOF/node
    ops.model('BasicBuilder', '-ndm', 2, '-ndf', 2)

    # create the material
    ops.nDMaterial('ElasticIsotropic', 1, 1000.0, 0.25, 3.0)

    # set type of quadrilateral element (uncomment one of the three options)
    Quad = 'quad'
    #set Quad bbarQuad
    #set Quad enhancedQuad

    # set up the arguments for the three considered elements
    if Quad == "enhancedQuad":
        eleArgs = "PlaneStress2D 1"

    if Quad == "quad":  
        eleArgs = "1 PlaneStress2D 1"

    if Quad == "bbarQuad":
        eleArgs = "1"


    # set up the number of elements in x (nx) and y (ny) direction
    nx = 16 # NOTE: nx MUST BE EVEN FOR THIS EXAMPLE
    ny = 4

    # define numbering of node at the left support (bn), and the two nodes at load application (l1, l2)
    bn = nx + 1
    l1 = int(nx/2 + 1)
    l2 = int(l1 + ny*(nx+1))

    # create the nodes and elements using the block2D command
    ops.block2D(nx, ny, 1, 1, Quad,
            1., 'PlaneStress2D', 1,
            1,   0.,   0., 
            2,  40.,   0.,
            3,  40.,  10.,
            4,   0.,  10.)

    # define boundary conditions
    ops.fix(1, 1, 1)
    ops.fix(bn, 0, 1)

    # define the recorder
    #---------------------
    # recorder Node -file Data/Node.out -time -node l1 -dof 2 disp

    # define load pattern
    #---------------------
    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1)
    ops.load(l1, 0.0, -1.0)
    ops.load(l2, 0.0, -1.0)

    # --------------------------------------------------------------------
    # Start of static analysis (creation of the analysis & analysis itself)
    # --------------------------------------------------------------------

    # Load control with variable load steps
    #                      init Jd min max
    ops.integrator('LoadControl', 1.0,   1, 1.0, 10.0)

    # Convergence test
    #              tolerance maxIter displayCode
    ops.test('EnergyIncr', 1.0e-12,    10,         0)

    # Solution algorithm
    ops.algorithm('Newton')

    # DOF numberer
    ops.numberer('RCM')

    # Cosntraint handler
    ops.constraints('Plain')

    # System of equations solver
    ops.system('ProfileSPD')

    # Type of analysis analysis
    ops.analysis('Static')

    # Perform the analysis
    ops.analyze(10)

    # --------------------------
    # End of static analysis
    # --------------------------

    # -------------------------------------
    # create display for transient analysis
    #--------------------------------------
    #                    windowTitle       xLoc yLoc xPixels yPixels
    # recorder display "Simply Supported Beam" 10     10      800     200    -wipe  
    # prp 20 5.0 1.0                                      # projection reference point (prp) defines the center of projection (viewer eye)
    # vup  0  1 0                                         # view-up vector (vup) 
    # vpn  0  0 1                                         # view-plane normal (vpn)     
    # viewWindow -30 30 -10 10                            # coordiantes of the window relative to prp  
    # display 10 0 5 
    # the 1st arg. is the tag for display mode
                                                        # the 2nd arg. is magnification factor for nodes, the 3rd arg. is magnif. factor of deformed shape

    # ---------------------------------------
    # Create and Perform the dynamic analysis
    # ---------------------------------------
    #define damping
    evals = ops.eigen(1)
    ops.rayleigh(0., 0., 0.,  2*0.02/sqrt(evals[0]))

    # Remove the static analysis & reset the time to 0.0
    ops.wipeAnalysis()
    ops.setTime(0.0)

    # Now remove the loads and let the beam vibrate
    ops.remove('loadPattern', 1)
    uy1 = ops.nodeDisp(9, 2)
    print("uy(9) = ",uy1)

    # Create the transient analysis
    ops.test('EnergyIncr', 1.0e-12, 10, 0)
    ops.algorithm('Newton')
    ops.numberer('RCM')
    ops.constraints('Plain')
    ops.integrator('Newmark', 0.5, 0.25)
    ops.system('BandGeneral')
    ops.analysis('Transient')

    # Perform the transient analysis (50 sec)
    ops.analyze(1500, 0.5)

    uy2 = ops.nodeDisp(9, 2)
    print("uy(9) = ", uy2)

    assert abs(uy1+0.39426414168933876514)<1e-12 and abs(uy2+0.00736847273806807632 )<1e-12

    print("========================================")
