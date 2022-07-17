import os
import os.path
import openseespy.opensees as ops

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Units: kips, in, sec  
#
# Written: GLF/MHS/fmk
# Date: January 2001

def test_RCFramePushover():

    ops.wipe()
    # ----------------------------------------------------
    # Start of Model Generation & Initial Gravity Analysis
    # ----------------------------------------------------

    # Do operations of Example3.1 by sourcing in the tcl file
    exec(open('RCFrameGravity.py','r').read())
    print("Gravity Analysis Completed")

    # Set the gravity loads to be constant & reset the time in the domain
    ops.loadConst('-time', 0.0)

    # ----------------------------------------------------
    # End of Model Generation & Initial Gravity Analysis
    # ----------------------------------------------------


    # ----------------------------------------------------
    # Start of additional modelling for lateral loads
    # ----------------------------------------------------

    # Define lateral loads
    # --------------------

    # Set some parameters
    H = 10.0		# Reference lateral load

    # Set lateral load pattern with a Linear TimeSeries
    ops.pattern('Plain', 2, 1)

    # Create nodal loads at nodes 3 & 4
    #    nd    FX  FY  MZ 
    ops.load( 3, H, 0.0, 0.0) 
    ops.load( 4, H, 0.0, 0.0) 

    # ----------------------------------------------------
    # End of additional modelling for lateral loads
    # ----------------------------------------------------



    # ----------------------------------------------------
    # Start of modifications to analysis for push over
    # ----------------------------------------------------

    # Set some parameters
    dU = 0.1	        # Displacement increment

    # Change the integration scheme to be displacement control
    #                             node dof init Jd min max
    ops.integrator('DisplacementControl',  3,   1,   dU,  1, dU, dU)

    # ----------------------------------------------------
    # End of modifications to analysis for push over
    # ----------------------------------------------------


    # ------------------------------
    # Start of recorder generation
    # ------------------------------

    # Stop the old recorders by destroying them
    # remove recorders

    # Create a recorder to monitor nodal displacements
    #recorder Node -file node32.out -time -node 3 4 -dof 1 2 3 disp

    # Create a recorder to monitor element forces in columns
    #recorder EnvelopeElement -file ele32.out -time -ele 1 2 forces

    # --------------------------------
    # End of recorder generation
    # ---------------------------------


    # ------------------------------
    # Finally perform the analysis
    # ------------------------------

    # Set some parameters
    maxU = 15.0	        # Max displacement
    currentDisp = 0.0
    ok = 0

    ops.test('NormDispIncr', 1.0e-12,  1000) 
    ops.algorithm('ModifiedNewton', '-initial')

    while ok==0 and currentDisp<maxU:

        ok = ops.analyze(1)

        # if the analysis fails try initial tangent iteration
        if ok != 0:
            print("modified newton failed")
            break
        # print "regular newton failed .. lets try an initail stiffness for this step"
        # test('NormDispIncr', 1.0e-12,  1000) 
        # # algorithm('ModifiedNewton', '-initial')
        # ok = analyze(1)
        # if ok == 0:
            #     print "that worked .. back to regular newton"
            
        # test('NormDispIncr', 1.0e-12,  10) 
        # algorithm('Newton')

        currentDisp = ops.nodeDisp(3,1)

    assert ok == 0




