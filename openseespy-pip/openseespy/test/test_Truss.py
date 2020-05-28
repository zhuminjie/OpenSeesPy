import openseespy.opensees as ops

# ------------------------------
# Start of model generation
# -----------------------------

def test_Truss():

    # remove existing model
    ops.wipe()

    # set modelbuilder
    ops.model('basic', '-ndm', 2, '-ndf', 2)

    # create nodes
    ops.node(1, 0.0, 0.0)
    ops.node(2, 144.0,  0.0)
    ops.node(3, 168.0,  0.0)
    ops.node(4,  72.0, 96.0)

    # set boundary condition
    ops.fix(1, 1, 1)
    ops.fix(2, 1, 1)
    ops.fix(3, 1, 1)

    # define materials
    ops.uniaxialMaterial("Elastic", 1, 3000.0)

    # define elements
    ops.element("Truss",1,1,4,10.0,1)
    ops.element("Truss",2,2,4,5.0,1)
    ops.element("Truss",3,3,4,5.0,1)

    # create TimeSeries
    ops.timeSeries("Linear", 1)

    # create a plain load pattern
    ops.pattern("Plain", 1, 1)

    # Create the nodal load - command: load nodeID xForce yForce
    ops.load(4, 100.0, -50.0)

    # ------------------------------
    # Start of analysis generation
    # ------------------------------

    # create SOE
    ops.system("BandSPD")

    # create DOF number
    ops.numberer("Plain")

    # create constraint handler
    ops.constraints("Plain")

    # create integrator
    ops.integrator("LoadControl", 1.0)

    # create algorithm
    ops.algorithm("Linear")

    # create analysis object
    ops.analysis("Static")

    # perform the analysis
    ops.analyze(1)

    ux = ops.nodeDisp(4,1)
    uy = ops.nodeDisp(4,2)

    assert abs(ux-0.53009277713228375450)<1e-12 and abs(uy+0.17789363846931768864)<1e-12

