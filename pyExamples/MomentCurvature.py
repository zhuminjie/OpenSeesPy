from openseespy.opensees import *

def MomentCurvature(secTag, axialLoad, maxK, numIncr=100):
    
    # Define two nodes at (0,0)
    node(1, 0.0, 0.0)
    node(2, 0.0, 0.0)

    # Fix all degrees of freedom except axial and bending
    fix(1, 1, 1, 1)
    fix(2, 0, 1, 0)
    
    # Define element
    #                             tag ndI ndJ  secTag
    element('zeroLengthSection',  1,   1,   2,  secTag)

    # Define constant axial load
    timeSeries('Constant', 1)
    pattern('Plain', 1, 1)
    load(2, axialLoad, 0.0, 0.0)

    # Define analysis parameters
    integrator('LoadControl', 0.0)
    system('SparseGeneral', '-piv')
    test('NormUnbalance', 1e-9, 10)
    numberer('Plain')
    constraints('Plain')
    algorithm('Newton')
    analysis('Static')

    # Do one analysis for constant axial load
    analyze(1)

    # Define reference moment
    timeSeries('Linear', 2)
    pattern('Plain',2, 2)
    load(2, 0.0, 0.0, 1.0)

    # Compute curvature increment
    dK = maxK / numIncr

    # Use displacement control at node 2 for section analysis
    integrator('DisplacementControl', 2,3,dK,1,dK,dK)

    # Do the section analysis
    analyze(numIncr)


wipe()
print("Start MomentCurvature.py example")

# Define model builder
# --------------------
model('basic','-ndm',2,'-ndf',3)

# Define materials for nonlinear columns
# ------------------------------------------
# CONCRETE                  tag   f'c        ec0   f'cu        ecu
# Core concrete (confined)
uniaxialMaterial('Concrete01',1, -6.0,  -0.004,  -5.0,  -0.014)

# Cover concrete (unconfined)
uniaxialMaterial('Concrete01',2, -5.0,  -0.002,  0.0,  -0.006)

# STEEL
# Reinforcing steel 
fy = 60.0      # Yield stress
E = 30000.0    # Young's modulus

#                        tag  fy E0    b
uniaxialMaterial('Steel01', 3, fy, E, 0.01)

# Define cross-section for nonlinear columns
# ------------------------------------------

# set some paramaters
colWidth = 15
colDepth = 24 

cover = 1.5
As = 0.60;     # area of no. 7 bars

# some variables derived from the parameters
y1 = colDepth/2.0
z1 = colWidth/2.0


section('Fiber', 1)

# Create the concrete core fibers
patch('rect',1,10,1 ,cover-y1, cover-z1, y1-cover, z1-cover)

# Create the concrete cover fibers (top, bottom, left, right)
patch('rect',2,10,1 ,-y1, z1-cover, y1, z1)
patch('rect',2,10,1 ,-y1, -z1, y1, cover-z1)
patch('rect',2,2,1 ,-y1, cover-z1, cover-y1, z1-cover)
patch('rect',2,2,1 ,y1-cover, cover-z1, y1, z1-cover)

# Create the reinforcing fibers (left, middle, right)
layer('straight', 3, 3, As, y1-cover, z1-cover, y1-cover, cover-z1)
layer('straight', 3, 2, As, 0.0     , z1-cover, 0.0      , cover-z1)
layer('straight', 3, 3, As, cover-y1, z1-cover, cover-y1, cover-z1)

# Estimate yield curvature
# (Assuming no axial load and only top and bottom steel)
# d -- from cover to rebar
d = colDepth-cover
# steel yield strain
epsy = fy/E
Ky = epsy/(0.7*d)

# Print estimate to standard output
print("Estimated yield curvature: ", Ky)

# Set axial load 
P = -180.0

# Target ductility for analysis
mu = 15.0

# Number of analysis increments
numIncr = 100

# Call the section analysis procedure
MomentCurvature(1, P, Ky*mu, numIncr)

results = open('results.out','a+')

u = nodeDisp(2,3)
if abs(u-0.00190476190476190541)<1e-12:
    results.write('PASSED : MomentCurvature.py\n');
    print("Passed!")
else:
    results.write('FAILED : MomentCurvature.py\n');
    print("Failed!")

results.close()

print("==========================")
