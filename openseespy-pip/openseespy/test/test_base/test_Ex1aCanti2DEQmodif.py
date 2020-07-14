import openseespy.opensees as ops
print("=========================================================")
print("Start cantilever 2D EQ ground motion with gravity example")

# --------------------------------------------------------------------------------------------------
# Example 1. cantilever 2D
# EQ ground motion with gravity
# all units are in kip, inch, second
# elasticBeamColumn ELEMENT
#		Silvia Mazzoni & Frank McKenna, 2006
#
#    ^Y
#    |
#    2       __ 
#    |         | 
#    |         | 
#    |         | 
#  (1)      36'
#    |         | 
#    |         | 
#    |         | 
#  =1=    ----  -------->X
#
def test_Ex1aCanti2DEQmodif():
    # SET UP ----------------------------------------------------------------------------
    ops.wipe()						       # clear opensees model
    ops.model('basic', '-ndm', 2, '-ndf', 3)	       # 2 dimensions, 3 dof per node
    # file mkdir data 				   # create data directory

    # define GEOMETRY -------------------------------------------------------------
    # nodal coordinates:
    ops.node(1, 0., 0.)					   # node#, X Y
    ops.node(2, 0., 432.)

    # Single point constraints -- Boundary Conditions
    ops.fix(1, 1, 1, 1) 			           # node DX DY RZ

    # nodal masses:
    ops.mass(2, 5.18, 0., 0.)			   # node#, Mx My Mz, Mass=Weight/g.

    # Define ELEMENTS -------------------------------------------------------------
    # define geometric transformation: performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global-coordinate system
    ops.geomTransf('Linear', 1)  		       # associate a tag to transformation

    # connectivity:
    ops.element('elasticBeamColumn', 1, 1, 2, 3600.0, 3225.0,1080000.0, 1)	

    # define GRAVITY -------------------------------------------------------------
    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1,)
    ops.load(2, 0., -2000., 0.)			    # node#, FX FY MZ --  superstructure-weight

    ops.constraints('Plain')  				# how it handles boundary conditions
    ops.numberer('Plain')			    # renumber dof's to minimize band-width (optimization), if you want to
    ops.system('BandGeneral')		    # how to store and solve the system of equations in the analysis
    ops.algorithm('Linear')                 # use Linear algorithm for linear analysis
    ops.integrator('LoadControl', 0.1)			# determine the next time step for an analysis, # apply gravity in 10 steps
    ops.analysis('Static')					    # define type of analysis static or transient
    ops.analyze(10)					        # perform gravity analysis
    ops.loadConst('-time', 0.0)				# hold gravity constant and restart time

    # DYNAMIC ground-motion analysis -------------------------------------------------------------
    # create load pattern
    G = 386.0
    ops.timeSeries('Path', 2, '-dt', 0.005, '-filePath', 'A10000.dat', '-factor', G) # define acceleration vector from file (dt=0.005 is associated with the input file gm)
    ops.pattern('UniformExcitation', 2, 1, '-accel', 2)		         # define where and how (pattern tag, dof) acceleration is applied

    # set damping based on first eigen mode
    evals = ops.eigen('-fullGenLapack', 1)
    freq = evals[0]**0.5
    dampRatio = 0.02
    ops.rayleigh(0., 0., 0., 2*dampRatio/freq)

    # display displacement shape of the column
    # recorder display "Displaced shape" 10 10 500 500 -wipe
    # prp 200. 50. 1
    # vup  0  1 0
    # vpn  0  0 1
    # display 1 5 40 

    # create the analysis
    ops.wipeAnalysis()			     # clear previously-define analysis parameters
    ops.constraints('Plain')    	 # how it handles boundary conditions
    ops.numberer('Plain')    # renumber dof's to minimize band-width (optimization), if you want to
    ops.system('BandGeneral') # how to store and solve the system of equations in the analysis
    ops.algorithm('Linear')	 # use Linear algorithm for linear analysis
    ops.integrator('Newmark', 0.5, 0.25)    # determine the next time step for an analysis
    ops.analysis('Transient')   # define type of analysis: time-dependent
    ops.analyze(3995, 0.01)	 # apply 3995 0.01-sec time steps in analysis

    u2 = ops.nodeDisp(2, 2)
    print("u2 = ", u2)


    assert abs(u2+0.07441860465116277579) < 1e-12
    ops.wipe()

    print("=========================================")
