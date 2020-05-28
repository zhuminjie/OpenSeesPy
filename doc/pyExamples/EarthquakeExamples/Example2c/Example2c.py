# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:12:06 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
# Example 2c. 2D cantilever column, dynamic eq ground motion
# EQ ground motion with gravity- uniform excitation of structure
#In this example, the Uniaxial Section of Example 2b is replaced by a fiber section. Inelastic uniaxial materials are used in this example, 
#which are assigned to each fiber, or patch of fibers, in the section.
#In this example the axial and flexural behavior are coupled, a characteristic of the fiber section.
#The nonlinear/inelastic behavior of a fiber section is defined by the stress-strain response of the uniaxial materials used to define it.

#To run EQ ground-motion analysis (BM68elc.acc needs to be downloaded into the same directory)
#the problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual(example: 2c)
# --------------------------------------------------------------------------------------------------
#	OpenSees (Tcl) code by:	Silvia Mazzoni & Frank McKenna, 2006

#
#    ^Y
#    |
#    2       __ 
#    |          | 
#    |          |
#    |          |
#  (1)       LCol
#    |          |
#    |          |
#    |          |
#  =1=      _|_  -------->X
#

# SET UP ----------------------------------------------------------------------------
import openseespy.opensees as op
#import the os module
import os
import math
op.wipe()
#########################################################################################################################################################################
#to create a directory at specified path with name "Data"
os.chdir('C:\\Opensees Python\\OpenseesPy examples')

#this will create the directory with name 'Data' and will update it when we rerun the analysis, otherwise we have to keep deleting the old 'Data' Folder
dir = "C:\\Opensees Python\\OpenseesPy examples\\Data-2c"
if not os.path.exists(dir):
    os.makedirs(dir)
#this will create just 'Data' folder    
#os.mkdir("Data")    
#detect the current working directory
#path1 = os.getcwd()
#print(path1)
#########################################################################################################################################################################

#########################################################################################################################################################################
op.model('basic', '-ndm', 2, '-ndf', 3) 
LCol = 432.0 # column length
Weight = 2000.0 # superstructure weight

# define section geometry
HCol = 60.0 # Column Depth
BCol = 60.0 # Column Width

PCol =Weight  # nodal dead-load weight per column
g = 386.4
Mass =  PCol/g

ACol = HCol*BCol*1000  # cross-sectional area, make stiff
IzCol = (BCol*math.pow(HCol,3))/12 # Column moment of inertia

op.node(1, 0.0, 0.0)
op.node(2, 0.0, LCol)

op.fix(1, 1, 1, 1)

op.mass(2, Mass, 1e-9, 0.0)

ColSecTag = 1			# assign a tag number to the column section
coverCol = 5.0   # Column cover to reinforcing steel NA.
numBarsCol = 16  # number of longitudinal-reinforcement bars in column. (symmetric top & bot)
barAreaCol = 2.25  # area of longitudinal-reinforcement bars

# MATERIAL parameters
IDconcU = 1 			# material ID tag -- unconfined cover concrete (here used for complete section)
IDreinf = 2 				# material ID tag -- reinforcement

# nominal concrete compressive strength
fc = -4.0 				# CONCRETE Compressive Strength (+Tension, -Compression)
Ec = 57*math.sqrt(-fc*1000) # Concrete Elastic Modulus (the term in sqr root needs to be in psi

# unconfined concrete
fc1U = fc			# UNCONFINED concrete (todeschini parabolic model), maximum stress
eps1U = -0.003			# strain at maximum strength of unconfined concrete
fc2U =  0.2*fc1U		# ultimate stress
eps2U = -0.01			# strain at ultimate stress
Lambda = 0.1				# ratio between unloading slope at $eps2 and initial slope $Ec

# tensile-strength properties
ftU = -0.14* fc1U		# tensile strength +tension
Ets = ftU/0.002			# tension softening stiffness

Fy = 66.8			# STEEL yield stress
Es = 29000.0				# modulus of steel
Bs = 0.01				# strain-hardening ratio 
R0 = 18.0				# control the transition from elastic to plastic branches
cR1 = 0.925				# control the transition from elastic to plastic branches
cR2 = 0.15				# control the transition from elastic to plastic branches

op.uniaxialMaterial('Concrete02', IDconcU, fc1U, eps1U, fc2U, eps2U, Lambda, ftU, Ets) # build cover concrete (unconfined)
op.uniaxialMaterial('Steel02', IDreinf, Fy, Es, Bs, R0,cR1,cR2) # build reinforcement material
# FIBER SECTION properties -------------------------------------------------------------
# symmetric section
#                        y
#                        ^
#                        |     
#             ---------------------     --   --
#             |   o     o     o    |     |    -- cover
#             |                       |     |
#             |                       |     |
#    z <--- |          +           |     H
#             |                       |     |
#             |                       |     |
#             |   o     o     o    |     |    -- cover
#             ---------------------     --   --
#             |-------- B --------|
#
# RC section: 

coverY = HCol/2.0	# The distance from the section z-axis to the edge of the cover concrete -- outer edge of cover concrete
coverZ = BCol/2.0	# The distance from the section y-axis to the edge of the cover concrete -- outer edge of cover concrete
coreY = coverY-coverCol
coreZ = coverZ-coverCol
nfY = 16  # number of fibers for concrete in y-direction
nfZ = 4			# number of fibers for concrete in z-direction

op.section('Fiber', ColSecTag)
op.patch('quad', IDconcU, nfZ, nfY, -coverY,coverZ, -coverY,-coverZ, coverY,-coverZ, coverY,coverZ) # Define the concrete patch
op.layer('straight', IDreinf, numBarsCol, barAreaCol, -coreY,coreZ,-coreY,-coreZ)
op.layer('straight', IDreinf, numBarsCol, barAreaCol, coreY,coreZ, coreY,-coreZ)
ColTransfTag = 1
op.geomTransf('Linear', ColTransfTag)
numIntgrPts = 5
eleTag = 1

#import InelasticFiberSection

op.element('nonlinearBeamColumn', eleTag, 1, 2, numIntgrPts, ColSecTag, ColTransfTag)

op.recorder('Node', '-file', 'Data-2c/DFree.out','-time', '-node', 2, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-2c/DBase.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-2c/RBase.out','-time', '-node', 1, '-dof', 1,2,3, 'reaction')
#op.recorder('Drift', '-file', 'Data-2c/Drift.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Element', '-file', 'Data-2c/FCol.out','-time', '-ele', 1, 'globalForce')
op.recorder('Element', '-file', 'Data-2c/ForceColSec1.out','-time', '-ele', 1, 'section', 1, 'force')
#op.recorder('Element', '-file', 'Data-2c/DCol.out','-time', '-ele', 1, 'deformations')

#defining gravity loads
op.timeSeries('Linear', 1)
op.pattern('Plain', 1, 1)
op.load(2, 0.0, -PCol, 0.0)

Tol = 1e-8 # convergence tolerance for test
NstepGravity = 10
DGravity = 1/NstepGravity
op.integrator('LoadControl', DGravity) # determine the next time step for an analysis
op.numberer('Plain') # renumber dof's to minimize band-width (optimization), if you want to
op.system('BandGeneral') # how to store and solve the system of equations in the analysis
op.constraints('Plain') # how it handles boundary conditions
op.test('NormDispIncr', Tol, 6) # determine if convergence has been achieved at the end of an iteration step
op.algorithm('Newton') # use Newton's solution algorithm: updates tangent stiffness at every iteration
op.analysis('Static') # define type of analysis static or transient
op.analyze(NstepGravity) # apply gravity

op.loadConst('-time', 0.0) #maintain constant gravity loads and reset time to zero
 
#applying Dynamic Ground motion analysis
GMdirection = 1
GMfile = 'BM68elc.acc'
GMfact = 1.0



Lambda = op.eigen('-fullGenLapack', 1) # eigenvalue mode 1
import math
Omega = math.pow(Lambda, 0.5)
betaKcomm = 2 * (0.02/Omega)

xDamp = 0.02				# 2% damping ratio
alphaM = 0.0				# M-prop. damping; D = alphaM*M	
betaKcurr = 0.0		# K-proportional damping;      +beatKcurr*KCurrent
betaKinit = 0.0 # initial-stiffness proportional damping      +beatKinit*Kini

op.rayleigh(alphaM,betaKcurr, betaKinit, betaKcomm) # RAYLEIGH damping

# Uniform EXCITATION: acceleration input
IDloadTag = 400			# load tag
dt = 0.01			# time step for input ground motion
GMfatt = 1.0			# data in input file is in g Unifts -- ACCELERATION TH
maxNumIter = 10
op.timeSeries('Path', 2, '-dt', dt, '-filePath', GMfile, '-factor', GMfact)
op.pattern('UniformExcitation', IDloadTag, GMdirection, '-accel', 2) 

op.wipeAnalysis()
op.constraints('Transformation')
op.numberer('Plain')
op.system('BandGeneral')
op.test('EnergyIncr', Tol, maxNumIter)
op.algorithm('ModifiedNewton')

NewmarkGamma = 0.5
NewmarkBeta = 0.25
op.integrator('Newmark', NewmarkGamma, NewmarkBeta)
op.analysis('Transient')

DtAnalysis = 0.01
TmaxAnalysis = 10.0

Nsteps =  int(TmaxAnalysis/ DtAnalysis)

ok = op.analyze(Nsteps, DtAnalysis)

tCurrent = op.getTime()

# for gravity analysis, load control is fine, 0.1 is the load factor increment (http://opensees.berkeley.edu/wiki/index.php/Load_Control)

test = {1:'NormDispIncr', 2: 'RelativeEnergyIncr', 4: 'RelativeNormUnbalance',5: 'RelativeNormDispIncr', 6: 'NormUnbalance'}
algorithm = {1:'KrylovNewton', 2: 'SecantNewton' , 4: 'RaphsonNewton',5: 'PeriodicNewton', 6: 'BFGS', 7: 'Broyden', 8: 'NewtonLineSearch'}

for i in test:
    for j in algorithm:

        if ok != 0:
            if j < 4:
                op.algorithm(algorithm[j], '-initial')
                
            else:
                op.algorithm(algorithm[j])
                
            op.test(test[i], Tol, 1000)
            ok = op.analyze(Nsteps, DtAnalysis)                            
            print(test[i], algorithm[j], ok)             
            if ok == 0:
                break
        else:
            continue

u2 = op.nodeDisp(2, 1)
print("u2 = ", u2)

op.wipe()