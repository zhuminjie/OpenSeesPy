# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:13:55 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland
#                         Email: pchi893@aucklanduni.ac.nz    
# Example 3. 2D Cantilever -- Build Model
# In this script Inelastic fiber section using nonlinearBeamColumn elements and uniaxial inelastic sections are created and gravity loading is applied. This can be used for static
#pushover or dynamic earthquake input further.

#units are introduced and the separation of the model-building and the analysis portions of the input file. This example uses 2D cantilever column.   
#The same analysis file can be used on different model-building files (elastic or inelastic elements).
##the problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual  (example: 3)
# and (http://opensees.berkeley.edu/wiki/index.php/OpenSees_Example_3._Cantilever_Column_with_units)
# --------------------------------------------------------------------------------------------------
#	OpenSees (Tcl) code by:	Silvia Mazzoni & Frank McKenna, 2006
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
import os
import math
op.wipe()
#########################################################################################################################################################################
#to create a directory at specified path with name "Data"
os.chdir('C:\\Opensees Python\\OpenseesPy examples')

#this will create the directory with name 'Data' and will update it when we rerun the analysis, otherwise we have to keep deleting the old 'Data' Folder
dir = "C:\\Opensees Python\\OpenseesPy examples\\Data-3-inelastic"
if not os.path.exists(dir):
    os.makedirs(dir)
#this will create just 'Data' folder    
#os.mkdir("Data")    
#detect the current working directory
#path1 = os.getcwd()
#print(path1)
#########################################################################################################################################################################
#All results in Inch, Kip and Sec
# Define ELEMENTS & SECTIONS 
inch = 1.0
kip = 1.0
sec = 1.0
LunitTXT = 'inch'
FunitTXT = 'kip'
TunitTXT = 'sec'
ft = 12*inch
ksi = kip/math.pow(inch,2)
psi = ksi/1000
lbf = psi*inch*inch
pcf = lbf/math.pow(ft,3)
inch2 = inch*inch
inch4 = math.pow(inch,4)
cm = inch/2.54
PI = 2 * math.asin(1.0)
g = 32.2 * ft/math.pow(sec,2)
Ubig = 1e10
Usmall = 1/Ubig


op.model('basic', '-ndm', 2, '-ndf', 3) 
LCol = 36.0*ft   # column length
Weight = 2000.0*kip   # superstructure weight

# define section geometry
HCol = 5.0*ft # Column Depth
BCol = 5.0*ft # Column Width

PCol =Weight  # nodal dead-load weight per column
#g = 386.4
Mass =  PCol/g

ACol = HCol*BCol # cross-sectional area
IzCol = (BCol*math.pow(HCol,3))/12 # Column moment of inertia

op.node(1, 0.0, 0.0)
op.node(2, 0.0, LCol)

op.fix(1, 1, 1, 1)
IDctrlNode = 2
IDctrlDOF = 1
op.mass(2, Mass, 1e-9, 0.0)

ColSecTag = 1			# assign a tag number to the column section
coverCol = 5.0*inch   # Column cover to reinforcing steel NA.
numBarsCol = 20  # number of longitudinal-reinforcement bars in column. (symmetric top & bot)
barAreaCol = 2.25*inch2  # area of longitudinal-reinforcement bars

# MATERIAL parameters
IDconcU = 1 			# material ID tag -- unconfined cover concrete (here used for complete section)
IDreinf = 2 				# material ID tag -- reinforcement

# nominal concrete compressive strength
fc = -4.0*ksi 				# CONCRETE Compressive Strength (+Tension, -Compression)
Ec = 57*ksi*math.sqrt(-fc/psi) # Concrete Elastic Modulus (the term in sqr root needs to be in psi

# unconfined concrete
fc1U = fc			# UNCONFINED concrete (todeschini parabolic model), maximum stress
eps1U = -0.003			# strain at maximum strength of unconfined concrete
fc2U =  0.2*fc1U		# ultimate stress
eps2U = -0.01			# strain at ultimate stress
Lambda = 0.1				# ratio between unloading slope at $eps2 and initial slope $Ec

# tensile-strength properties
ftU = -0.14* fc1U		# tensile strength +tension
Ets = ftU/0.002			# tension softening stiffness

Fy = 66.8*ksi			# STEEL yield stress
Es = 29000.0*ksi				# modulus of steel
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

op.element('nonlinearBeamColumn', eleTag, 1, 2, numIntgrPts, ColSecTag, ColTransfTag)

op.recorder('Node', '-file', 'Data-3-inelastic/DFree.out','-time', '-node', 2, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-3-inelastic/DBase.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-3-inelastic/RBase.out','-time', '-node', 1, '-dof', 1,2,3, 'reaction')
#op.recorder('Drift', '-file', 'Data-3-inelastic/Drift.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Element', '-file', 'Data-3-inelastic/FCol.out','-time', '-ele', 1, 'globalForce')
op.recorder('Element', '-file', 'Data-3-inelastic/ForceColSec1.out','-time', '-ele', 1, 'section', 1, 'force')
#op.recorder('Element', '-file', 'Data-3-inelastic/DCol.out','-time', '-ele', 1, 'deformations')

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
print('Model Built')


















