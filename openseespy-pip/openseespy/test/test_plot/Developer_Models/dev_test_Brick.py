# Cantilever Beam Example 8.1
# ---------------------------
# Cantilever beam modeled with three dimensional brick elements 
# Example Location: OpenSees/EXAMPLES/ExamplePython
#
# Written: Andreas Schellenberg (andreas.schellenberg@gmail.com)
# Date: September 2017
# Edited: Anurag Upadhyay, Dec 2019- removed analysis and added mass and commands to visualize model.

import openseespy.opensees as ops
# from openseespy.postprocessing.Get_Rendering import * 

############################################################################
### NOTE TO DEVELOPERS: 
##  1. Test this example for the new command you are developing or 
##     editing.
##  2. Replace the above line with your own Get_Rendering library under 
##     development. For example see below,
############################################################################

from Development_Get_Rendering import *

# ----------------------------
# Start of model generation
# ----------------------------
ops.wipe()

ops.model("BasicBuilder", "-ndm",3, "-ndf",3)

# set default units
ops.defaultUnits("-force", "kip", "-length", "in", "-time", "sec", "-temp", "F")

# Define the material
# -------------------
#                               matTag  E     nu   rho
ops.nDMaterial("ElasticIsotropic", 1, 10000.0, 0.25, 1.27) 

# Define geometry
# ---------------
Brick = "stdBrick"
# Brick = "bbarBrick"
# Brick = "SSPbrick"

nz = 10
nx = 4 
ny = 4

nn = int((nz+1)*(nx+1)*(ny+1))

# mesh generation
#          numX numY numZ startNode startEle eleType eleArgs? coords?
ops.block3D(nx, ny, nz, 1, 1,
            Brick, 1,
            1, -1.0, -1.0,  0.0,
            2,  1.0, -1.0,  0.0,
            3,  1.0,  1.0,  0.0,
            4, -1.0,  1.0,  0.0, 
            5, -1.0, -1.0, 10.0,
            6,  1.0, -1.0, 10.0,
            7,  1.0,  1.0, 10.0,
            8, -1.0,  1.0, 10.0)

# boundary conditions
ops.fixZ(0.0, 1, 1, 1) 

# Assign mass
AllNodes = getNodeTags()
massX = 0.49

for nodes in AllNodes:
	mass(nodes, massX, massX, massX, 0.00001, 0.00001, 0.00001)

# Define point load
# create a Linear time series
ops.timeSeries("Linear", 1)

# create a Plain load pattern
load = 0.10
ops.pattern("Plain", 1, 1, "-fact", 1.0)
ops.load(nn, load, load, 0.0)


########## TEST PLOTTING 
plot_model(node, element)
plot_modeshape(1,20)

# ----------------------- 
# End of model generation
# -----------------------
