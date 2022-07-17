import os
import openseespy.opensees as ops

# ------------------------------
# Start of model generation
# -----------------------------

# remove existing model
ops.wipe()

# set modelbuilder
ops.model('basic', '-ndm', 2, '-ndf', 2)

# geometric
L = 0.146
H = L*2
H2 = 0.3
h = 0.005
alpha = 1.4
tw =  3*h

# material
rho = 1000.0
mu = 0.0001
b1 = 0.0
b2 = -9.81
thk = 0.012
kappa = -1.0

# time steps
dtmax = 1e-3
dtmin = 1e-6
totaltime = 1.0

# filename
filename = 'dambreak'

# recorder
if not os.path.exists(filename):
    os.makedirs(filename)
ops.recorder('PVD', filename, 'disp', 'vel', 'pressure')

# nodes
ops.node(1, 0.0, 0.0)
ops.node(2, L, 0.0)
ops.node(3, L, H)
ops.node(4, 0.0, H)
ops.node(5, 0.0, H2)
ops.node(6, 4*L, 0.0)
ops.node(7, 4*L, H2)
ops.node(8, -tw, H2)
ops.node(9, -tw, -tw)
ops.node(10, 4*L+tw, -tw)
ops.node(11, 4*L+tw, H2)

# ids for meshing
wall_id = 1
water_bound_id = -1
water_body_id = -2

# wall mesh
wall_tag = 3
ndf = 2
ops.mesh('line', 1, 9, 4,5,8,9,10,11,7,6,2, wall_id, ndf, h)
ops.mesh('line', 2, 3, 2,1,4, wall_id, ndf, h)
ops.mesh('tri', wall_tag, 2, 1,2, wall_id, ndf, h)

# fluid mesh 
fluid_tag = 4
ops.mesh('line', 5, 3, 2,3,4, water_bound_id, ndf, h)

eleArgs = ['PFEMElementBubble',rho,mu,b1,b2,thk,kappa]
ops.mesh('tri', fluid_tag, 2, 2,5, water_body_id, ndf, h, *eleArgs)

for nd in ops.getNodeTags('-mesh', wall_tag):
    ops.fix(nd, 1,1)

# save the original modal
ops.record()

# create constraint object
ops.constraints('Plain')

# create numberer object
ops.numberer('Plain')

# create convergence test object
ops.test('PFEM', 1e-5, 1e-5, 1e-5, 1e-5, 1e-15, 1e-15, 20, 3, 1, 2)

# create algorithm object
ops.algorithm('Newton')

# create integrator object
ops.integrator('PFEM')

# create SOE object
ops.system('PFEM', '-umfpack', '-print')

# create analysis object
ops.analysis('PFEM', dtmax, dtmin, b2)

# analysis
while ops.getTime() < totaltime:

    # analysis
    if ops.analyze() < 0:
        break

    ops.remesh(alpha)
    


