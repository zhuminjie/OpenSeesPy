import os
import openseespy.opensees as ops

# ------------------------------
# Start of model generation
# -----------------------------

# remove existing model
ops.wipe()

# set modelbuilder
ops.model('basic', '-ndm', 2, '-ndf', 3)

# geometric
L = 0.146
H = 2*L
H2 = 0.3
b = 0.012
h = 0.005
alpha = 1.4
Hb = 20.0*b/3.0
tw =  3*h

# material
rho = 1000.0
mu = 0.0001
b1 = 0.0
b2 = -9.81
thk = 0.012
kappa = -1.0

rhos = 2500.0
A = thk*thk
E = 1e6
Iz = thk*thk*thk*thk/12.0
bmass = A*Hb*rhos

# analysis
dtmax = 1e-3
dtmin = 1e-6
totaltime = 1.0

filename = 'obstacle'

# recorder
if not os.path.exists(filename):
    os.makedirs(filename)
ops.recorder('PVD', filename, 'disp', 'vel', 'pressure')

# nodes
ops.node(1, 0.0, 0.0)
ops.node(2, L, 0.0)
ops.node(3, L, H, '-ndf', 2)
ops.node(4, 0.0, H)
ops.node(5, 0.0, H2)
ops.node(6, 4*L, 0.0)
ops.node(7, 4*L, H2)
ops.node(8, -tw, H2)
ops.node(9, -tw, -tw)
ops.node(10, 4*L+tw, -tw)
ops.node(11, 4*L+tw, H2)
ops.node(12, 2*L, 0.0)
ops.node(13, 2*L, Hb)

# ids for meshing
wall_id = 1
beam_id = 2
water_bound_id = -1
water_body_id = -2

# transformation
transfTag = 1
ops.geomTransf('Corotational', transfTag)

# section
secTag = 1
ops.section('Elastic', secTag, E, A, Iz)

# beam integration
inteTag = 1
numpts = 2
ops.beamIntegration('Legendre', inteTag, secTag, numpts)

# beam mesh
beamTag = 6
ndf = 3
ops.mesh('line', beamTag, 2, 12, 13, beam_id, ndf, h, 'dispBeamColumn', transfTag, inteTag)

ndmass = bmass/len(ops.getNodeTags('-mesh', beamTag))

for nd in ops.getNodeTags('-mesh', beamTag):
    ops.mass(nd, ndmass, ndmass, 0.0)

# fluid mesh 
fluidTag = 4
ndf = 2
ops.mesh('line', 1, 10, 4,5,8,9,10,11,7,6,12,2, wall_id, ndf, h)
ops.mesh('line', 2, 3, 2,1,4, wall_id, ndf, h)
ops.mesh('line', 3, 3, 2,3,4, water_bound_id, ndf, h)

eleArgs = ['PFEMElementBubble',rho,mu,b1,b2,thk,kappa]
ops.mesh('tri', fluidTag, 2, 2,3, water_body_id, ndf, h, *eleArgs)

# wall mesh
wallTag = 5
ops.mesh('tri', wallTag, 2, 1,2, wall_id, ndf, h)

for nd in ops.getNodeTags('-mesh', wallTag):
    ops.fix(nd, 1,1,1)

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
ops.system('PFEM')

# create analysis object
ops.analysis('PFEM', dtmax, dtmin, b2)

# analysis
while ops.getTime() < totaltime:

    # analysis
    if ops.analyze() < 0:
        break

    ops.remesh(alpha)
