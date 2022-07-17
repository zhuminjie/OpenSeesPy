print("=========================================================")
print("Start cantilever 2D EQ ground motion with gravity example")

from openseespy.opensees import *


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

# SET UP ----------------------------------------------------------------------------
wipe()						       # clear opensees model
model('basic', '-ndm', 2, '-ndf', 3)	       # 2 dimensions, 3 dof per node
# file mkdir data 				   # create data directory

# define GEOMETRY -------------------------------------------------------------
# nodal coordinates:
node(1, 0., 0.)					   # node#, X Y
node(2, 0., 432.)

# Single point constraints -- Boundary Conditions
fix(1, 1, 1, 1) 			           # node DX DY RZ

# nodal masses:
mass(2, 5.18, 0., 0.)			   # node#, Mx My Mz, Mass=Weight/g.

# Define ELEMENTS -------------------------------------------------------------
# define geometric transformation: performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global-coordinate system
geomTransf('Linear', 1)  		       # associate a tag to transformation

# connectivity:
element('elasticBeamColumn', 1, 1, 2, 3600.0, 3225.0,1080000.0, 1)	

# define GRAVITY -------------------------------------------------------------
timeSeries('Linear', 1)
pattern('Plain', 1, 1,)
load(2, 0., -2000., 0.)			    # node#, FX FY MZ --  superstructure-weight

constraints('Plain')  				# how it handles boundary conditions
numberer('Plain')			    # renumber dof's to minimize band-width (optimization), if you want to
system('BandGeneral')		    # how to store and solve the system of equations in the analysis
algorithm('Linear')                 # use Linear algorithm for linear analysis
integrator('LoadControl', 0.1)			# determine the next time step for an analysis, # apply gravity in 10 steps
analysis('Static')					    # define type of analysis static or transient
analyze(10)					        # perform gravity analysis
loadConst('-time', 0.0)				# hold gravity constant and restart time

# DYNAMIC ground-motion analysis -------------------------------------------------------------
# create load pattern
G = 386.0
timeSeries('Path', 2, '-dt', 0.005, '-filePath', 'A10000.dat', '-factor', G) # define acceleration vector from file (dt=0.005 is associated with the input file gm)
pattern('UniformExcitation', 2, 1, '-accel', 2)		         # define where and how (pattern tag, dof) acceleration is applied

# set damping based on first eigen mode
freq = eigen('-fullGenLapack', 1)**0.5
dampRatio = 0.02
rayleigh(0., 0., 0., 2*dampRatio/freq)

# create the analysis
wipeAnalysis()			     # clear previously-define analysis parameters
constraints('Plain')    	 # how it handles boundary conditions
numberer('Plain')    # renumber dof's to minimize band-width (optimization), if you want to
system('BandGeneral') # how to store and solve the system of equations in the analysis
algorithm('Linear')	 # use Linear algorithm for linear analysis
integrator('Newmark', 0.5, 0.25)    # determine the next time step for an analysis
analysis('Transient')   # define type of analysis: time-dependent
analyze(3995, 0.01)	 # apply 3995 0.01-sec time steps in analysis

u2 = nodeDisp(2, 2)
print("u2 = ", u2)


if abs(u2+0.07441860465116277579) < 1e-12:
    print("Passed!")
else:
    print("Failed!")

wipe()

print("=========================================")
