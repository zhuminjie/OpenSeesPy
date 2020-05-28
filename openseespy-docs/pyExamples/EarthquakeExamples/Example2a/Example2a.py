# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:12:06 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 

# EQ ground motion with gravity- uniform excitation of structure
# all units are in kip, inch, second
##Note: In this example, all input values for Example 1a are replaced by variables. The objective of this example is to demonstrate the use of variables in defining 
#the OpenSees input and also to run various tests and algorithms at once to increase the chances of convergence
# Example 2a. 2D cantilever column, dynamic eq ground motion
#To run EQ ground-motion analysis (BM68elc.acc needs to be downloaded into the same directory)
#the detailed problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual  (example:2a)
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

#########################################################################################################################################################################
op.model('basic', '-ndm', 2, '-ndf', 3) 

#to create a directory at specified path with name "Data"
os.chdir('C:\\Opensees Python\\OpenseesPy examples')

#this will create the directory with name 'Data' and will update it when we rerun the analysis, otherwise we have to keep deleting the old 'Data' Folder
dir = "C:\\Opensees Python\\OpenseesPy examples\\Data-2a"
if not os.path.exists(dir):
    os.makedirs(dir)

#this will create just 'Data' folder    
#os.mkdir("Data")
    
#detect the current working directory
#path1 = os.getcwd()
#print(path1)

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

ColTransfTag = 1
op.geomTransf('Linear', ColTransfTag)
#A = 3600000000.0
#E = 4227.0
#Iz = 1080000.0

fc = -4.0 # CONCRETE Compressive Strength (+Tension, -Compression)
Ec = 57*math.sqrt(-fc*1000) # Concrete Elastic Modulus (the term in sqr root needs to be in psi

op.element('elasticBeamColumn', 1, 1, 2, ACol, Ec, IzCol, ColTransfTag)

op.recorder('Node', '-file', 'Data-2a/DFree.out','-time', '-node', 2, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-2a/DBase.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-2a/RBase.out','-time', '-node', 1, '-dof', 1,2,3, 'reaction')
#op.recorder('Drift', '-file', 'Data-2a/Drift.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Element', '-file', 'Data-2a/FCol.out','-time', '-ele', 1, 'globalForce')
op.recorder('Element', '-file', 'Data-2a/DCol.out','-time', '-ele', 1, 'deformations')

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