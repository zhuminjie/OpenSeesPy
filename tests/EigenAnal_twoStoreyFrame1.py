print("==========================================")
print("Start Eigen analysis of a two-storey one-bay frame")
import math
import os
# Eigen analysis of a two-storey one-bay frame; Example 10.5 from "Dynamics of Structures" book by Anil Chopra

# units: in, kips

wipe()

#input
m =  100.0/386.0
numModes = 2

#material
A = 63.41
I = 320.0
E = 29000.0

#geometry
L = 240.
h = 120.

# create data directory
if not os.path.exists('modes/'):
    os.makedirs('modes/')


# define the model
#---------------------------------
#model builder
model('BasicBuilder', '-ndm', 2, '-ndf', 3)					

# nodal coordinates:
node(1,   0.,  0.) 
node(2,   L,  0. )
node(3,   0.,  h )
node(4,   L,  h )
node(5,   0.,   2*h)
node(6,   L,   2*h)

# Single point constraints -- Boundary Conditions
fix(1, 1, 1, 1)
fix(2, 1, 1, 1)

# assign mass
mass(3, m, 0., 0. )
mass(4, m, 0., 0. )
mass(5,  m/2., 0., 0. )
mass(6,  m/2., 0., 0. )

# define geometric transformation:
TransfTag = 1
geomTransf('Linear', TransfTag )

# define elements:
# columns
element('elasticBeamColumn',1, 1, 3, A, E,   2.*I, TransfTag)
element('elasticBeamColumn',2, 3, 5, A, E,  I   ,        TransfTag)
element('elasticBeamColumn',3, 2, 4, A, E,   2.*I, TransfTag)
element('elasticBeamColumn',4, 4, 6, A, E,  I     ,      TransfTag)
# beams
element('elasticBeamColumn',5, 3, 4, A, E,  2*I      ,     TransfTag)
element('elasticBeamColumn',6, 5, 6, A, E,  I       ,    TransfTag)

# record eigenvectors
#----------------------
# for { k 1 } { k <= numModes } { incr k } {
#     recorder Node -file format "modes/mode%i.out" k -nodeRange 1 6 -dof 1 2 3  "eigen k"
# }

# perform eigen analysis
#-----------------------------
lamb = eigen(numModes)

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
period = "modes/Periods.txt"
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
integrator('LoadControl', 0.0, 1, 0.0, 0.0)

# Convergence test
#                     tolerance maxIter displayCode
test('EnergyIncr',    1.0e-10,    100,        0)

# Solution algorithm
algorithm('Newton')

# DOF numberer
numberer('RCM')

# Constraint handler
constraints('Transformation')


# System of equations solver
system('ProfileSPD')

analysis('Static')
res = analyze(1)
if res < 0:
    print("Modal analysis failed")


# get values of eigenvectors for translational DOFs
#---------------------------------------------------
f11 = nodeEigenvector(3, 1, 1)
f21 = nodeEigenvector(5, 1, 1)
f12 = nodeEigenvector(3, 2, 1)
f22 = nodeEigenvector(5, 2, 1)
print("eigenvector 1: ",  [f11/f21, f21/f21])
print("eigenvector 2: ",  [f12/f22, f22/f22])

if abs(T[0]-0.628538768190688)<1e-12 and abs(T[1]-0.2359388635361575)<1e-12 and abs(f11/f21-0.3869004256389493)<1e-12 and abs(f21/f21-1.0)<1e-12 and abs(f12/f22+1.2923221761110006)<1e-12 and abs(f22/f22-1.0)<1e-12:
    print("Passed!")
else:
    print("Failed!")

print("==========================================")
