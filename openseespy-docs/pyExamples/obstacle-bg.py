import os
import openseespy.opensees as ops


print("=======================================================")
print("Starting Dambreak with Obstacle Background Mesh example")

# ------------------------------
# Start of model generation
# -----------------------------

# wipe all previous objects
ops.wipe()

# create a model with fluid
ops.model('basic', '-ndm', 2, '-ndf', 3)

# geometric
L = 0.146
H = L * 2
H2 = 0.3
b = 0.012
h = L / 40
Hb = 20.0 * b / 3.0

# number of particles per cell in each direction
numx = 3.0
numy = 3.0

# fluid properties
rho = 1000.0
mu = 0.0001
b1 = 0.0
b2 = -9.81
thk = 0.012
kappa = -1.0

# elastis structural material
rhos = 2500.0
A = thk * thk
E = 1e6
Iz = thk * thk * thk * thk / 12.0
bmass = A * Hb * rhos

# nonlinear structural material
E0 = 1e6
Fy = 5e4
hardening = 0.02

nonlinear = False

# analysis
dtmax = 1e-3
dtmin = 1e-3
totaltime = 1.0

if nonlinear:
    filename = 'obstaclenonlinear-bg'
else:
    filename = 'obstacle-bg'

# recorder
ops.recorder('BgPVD', filename, 'disp', 'vel', 'pressure', '-dT', 1e-3)
if not os.path.exists(filename):
    os.makedirs(filename)

# fluid mesh
ndf = 3

# total number of particles in each direction
nx = round(L / h * numx)
ny = round(H / h * numy)

# create particles
eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, thk, kappa]
partArgs = ['quad', 0.0, 0.0, L, 0.0, L, H, 0.0, H, nx, ny]
parttag = 1
ops.mesh('part', parttag, *partArgs, *eleArgs, '-vel', 0.0, 0.0)

# wall mesh
ops.node(1, 2 * L, 0.0)
ops.node(2, 2 * L, Hb)
ops.node(3, 0.0, H)
ops.node(4, 0.0, 0.0)
ops.node(5, 4 * L, 0.0)
ops.node(6, 4 * L, H)

sid = 1
walltag = 4
ops.mesh('line', walltag, 5, 3, 4, 1, 5, 6, sid, ndf, h)

wallNodes = ops.getNodeTags('-mesh', walltag)
for nd in wallNodes:
    ops.fix(nd, 1, 1, 1)

# structural mesh

# transformation
transfTag = 1
ops.geomTransf('Corotational', transfTag)

# section
secTag = 1
if nonlinear:
    matTag = 1
    ops.uniaxialMaterial('Steel01', matTag, Fy, E0, hardening)
    numfiber = 5
    ops.section('Fiber', secTag)
    ops.patch('rect', matTag, numfiber, numfiber, 0.0, 0.0, thk, thk)
else:
    ops.section('Elastic', secTag, E, A, Iz)

# beam integration
inteTag = 1
numpts = 2
ops.beamIntegration('Legendre', inteTag, secTag, numpts)

coltag = 3
eleArgs = ['dispBeamColumn', transfTag, inteTag]
ops.mesh('line', coltag, 2, 1, 2, sid, ndf, h, *eleArgs)

# mass
sNodes = ops.getNodeTags('-mesh', coltag)
bmass = bmass / len(sNodes)
for nd in sNodes:
    ops.mass(int(nd), bmass, bmass, 0.0)


# background mesh
lower = [-h, -h]
upper = [5 * L, 3 * L]

ops.mesh('bg', h, *lower, *upper,
     '-structure', sid, len(sNodes), *sNodes,
     '-structure', sid, len(wallNodes), *wallNodes)

print('num nodes =', len(ops.getNodeTags()))
print('num particles =', nx * ny)

# create constraint object
ops.constraints('Plain')

# create numberer object
ops.numberer('Plain')

# create convergence test object
ops.test('PFEM', 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 100, 3, 1, 2)

# create algorithm object
ops.algorithm('Newton')

# create integrator object
ops.integrator('PFEM', 0.5, 0.25)

# create SOE object
ops.system('PFEM')
# system('PFEM', '-mumps') Linux version can use mumps

# create analysis object
ops.analysis('PFEM', dtmax, dtmin, b2)

# analysis
while ops.getTime() < totaltime:

    # analysis
    if ops.analyze() < 0:
        break

    ops.remesh()

print("==========================================")
