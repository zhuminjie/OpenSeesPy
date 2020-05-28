# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:13:55 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
#
# Example4. 2D Portal Frame--  Build Model
# nonlinearBeamColumn element, inelastic fiber section 
#This is an example to show what all the Examples until example 3 has done, Example 4 adds the use of previously-created scripts. 
# In this script Inelastic fiber section using nonlinearBeamColumn elements and uniaxial inelastic sections are created and gravity loading is applied. This can be used for static
#pushover or dynamic earthquake input further.
#The same analysis file can be used on different model-building files (elastic or inelastic elements).  
#the problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual  (example: 4)       
# --------------------------------------------------------------------------------------------------
#	OpenSees (Tcl) code by:	Silvia Mazzoni & Frank McKenna, 2006
#
#    ^Y
#    |
#    3_________(3)________4       __ 
#    |                                    |          | 
#    |                                    |          |
#    |                                    |          |
#  (1)                                 (2)       LCol
#    |                                    |          |
#    |                                    |          |
#    |                                    |          |
#  =1=                               =2=      _|_  -------->X
#    |----------LBeam------------|
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
dir = "C:\\Opensees Python\\OpenseesPy examples\\Data-4-inelasticFiber"
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
LBeam = 42.0*ft
Weight = 2000.0*kip   # superstructure weight

# define section geometry
HCol = 5.0*ft # Column Depth
BCol = 5.0*ft # Column Width
HBeam = 8.0*ft
BBeam = 5.0*ft

# calculated parameters
PCol =Weight/2  # nodal dead-load weight per column
#g = 386.4
Mass =  PCol/g
MCol = ((Weight/LBeam)*math.pow(LBeam,2))/12

# calculated geometry parameters
ACol = HCol*BCol # cross-sectional area
ABeam = HBeam*BBeam
IzCol = (BCol*math.pow(HCol,3))/12 # Column moment of inertia
IzBeam =  (BBeam*math.pow(HBeam,3))/12 # Beam moment of inertia

op.node(1, 0.0, 0.0)
op.node(2, LBeam, 0.0)
op.node(3, 0.0, LCol)
op.node(4, LBeam, LCol)

op.fix(1, 1, 1, 0)
op.fix(2, 1, 1, 0)

IDctrlNode = 2
IDctrlDOF = 1

op.mass(3, Mass, 0.0, 0.0)
op.mass(4, Mass, 0.0, 0.0)

ColSecTag = 1			# assign a tag number to the column section
BeamSecTag = 2    # assign a tag number to the beam section
	
coverCol = 6.0*inch   # Column cover to reinforcing steel NA.
numBarsCol = 10  # number of longitudinal-reinforcement bars in column. (symmetric top & bot)
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
eps2U = -0.05			# strain at ultimate stress
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

# BEAM section:
op.section('Elastic', BeamSecTag,Ec,ABeam,IzBeam)	# elastic beam section)


ColTransfTag = 1
BeamTransfTag = 2
op.geomTransf('Linear', ColTransfTag)
op.geomTransf('Linear', BeamTransfTag)

numIntgrPts = 5


op.element('nonlinearBeamColumn', 1, 1, 3, numIntgrPts, ColSecTag, ColTransfTag)
op.element('nonlinearBeamColumn', 2, 2, 4, numIntgrPts, ColSecTag, ColTransfTag)

op.element('nonlinearBeamColumn', 3, 3, 4, numIntgrPts, BeamSecTag, BeamTransfTag)

op.recorder('Node', '-file', 'Data-4-inelasticFiber/DFree.out','-time', '-node', 3,4, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-4-inelasticFiber/DBase.out','-time', '-node', 1,2, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-4-inelasticFiber/RBase.out','-time', '-node', 1,2, '-dof', 1,2,3, 'reaction')
#op.recorder('Drift', '-file', 'Data-4-inelasticFiber/Drift.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Element', '-file', 'Data-4-inelasticFiber/FCol.out','-time', '-ele', 1,2, 'globalForce')
op.recorder('Element', '-file', 'Data-4-inelasticFiber/FBeam.out','-time', '-ele', 3, 'globalForce')
op.recorder('Element', '-file', 'Data-4-inelasticFiber/ForceColSec1.out','-time', '-ele', 1,2, 'section', 1, 'force')
op.recorder('Element', '-file', 'Data-4-inelasticFiber/DefoColSec1.out','-time', '-ele', 1,2, 'section', 1, 'deformation')
#op.recorder('Element', '-file', 'Data-4-inelasticFiber/DCol.out','-time', '-ele', 1, 'deformations')

#defining gravity loads
WzBeam = Weight/LBeam
op.timeSeries('Linear', 1)
op.pattern('Plain', 1, 1)
op.eleLoad('-ele', 3, '-type', '-beamUniform', -WzBeam, 0.0, 0.0)

#op.load(2, 0.0, -PCol, 0.0)

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


















