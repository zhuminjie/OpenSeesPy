
# Converted to openseespy by: Anurag Upadhyay, University of Utah.
# Units: N and m to follow the originally published code.

from openseespy.postprocessing.Get_Rendering import * 
from openseespy.opensees import *

import numpy as np
import matplotlib.pyplot as plt
import os
import math

pi = 3.1415

AnalysisType = "Pushover" # Cyclic   Pushover   Gravity

wipe()

model('basic','-ndm',3,'-ndf',6)

###################################
## Define Material
###################################

# Define PSUMAT and convert it to plane stress material
nDMaterial('PlaneStressUserMaterial',1,40,7,20.7e6,2.07e6,-4.14e6,-0.002,-0.01,0.001,0.3)
nDMaterial('PlateFromPlaneStress',4,1,1.25e10)

# Define material for rebar
uniaxialMaterial('Steel02',7,379e6,202.7e9,0.01,18.5,0.925,0.15)
uniaxialMaterial('Steel02',8,392e6,200.6e9,0.01,18.5,0.925,0.15)

# Convert rebar material to plane stress/plate rebar 
# Angle 0 is for vertical rebar and 90 is for horizontal rebar
nDMaterial('PlateRebar',9,7,90.0)
nDMaterial('PlateRebar',10,8,90.0)
nDMaterial('PlateRebar',11,8,0.0)

# Define LayeredShell sections. Section 1 is used for the special boundary elements and section 2 is used for the unconfined interior wall portion
section('LayeredShell',1,10,4,0.0125,11,0.0002403,11,0.0003676,4,0.024696,4,0.024696,4,0.024696,4,0.024696,11,0.0003676,11,0.0002403,4,0.0125)
section('LayeredShell',2,8,4,0.0125,11,0.0002403,10,0.0002356,4,0.0495241,4,0.0495241,10,0.0002356,11,0.0002403,4,0.0125)

# ##################
# NODES
# ##################
#define nodes
node(1,0.0,0,0)
node(2,0.2,0,0)
node(3,0.5,0,0)
node(4,0.8,0,0)
node(5,1.0,0,0)

node(6,0.0,0.2,0)
node(7,0.2,0.2,0)
node(8,0.5,0.2,0)
node(9,0.8,0.2,0)
node(10,1.0,0.2,0)

node(11,0.0,0.4,0)
node(12,0.2,0.4,0)
node(13,0.5,0.4,0)
node(14,0.8,0.4,0)
node(15,1.0,0.4,0)

node(16,0.0,0.6,0)
node(17,0.2,0.6,0)
node(18,0.5,0.6,0)
node(19,0.8,0.6,0)
node(20,1.0,0.6,0)

node(21,0.0,0.8,0)
node(22,0.2,0.8,0)
node(23,0.5,0.8,0)
node(24,0.8,0.8,0)
node(25,1.0,0.8,0)
                 
node(26,0.0,1.0,0)
node(27,0.2,1.0,0)
node(28,0.5,1.0,0)
node(29,0.8,1.0,0)
node(30,1.0,1.0,0)

node(31,0.0,1.2,0)
node(32,0.2,1.2,0)
node(33,0.5,1.2,0)
node(34,0.8,1.2,0)
node(35,1.0,1.2,0)
                 
node(36,0.0,1.4,0)
node(37,0.2,1.4,0)
node(38,0.5,1.4,0)
node(39,0.8,1.4,0)
node(40,1.0,1.4,0)

node(41,0.0,1.6,0)
node(42,0.2,1.6,0)
node(43,0.5,1.6,0)
node(44,0.8,1.6,0)
node(45,1.0,1.6,0)
                 
node(46,0.0,1.8,0)
node(47,0.2,1.8,0)
node(48,0.5,1.8,0)
node(49,0.8,1.8,0)
node(50,1.0,1.8,0)
                
node(51,0.0,2.0,0)
node(52,0.2,2.0,0)
node(53,0.5,2.0,0)
node(54,0.8,2.0,0)
node(55,1.0,2.0,0)

##########################
# ELEMENTS 
##########################

ShellType = "ShellNLDKGQ"
# ShellType = "ShellMITC4"

element(ShellType,1,1,2,7,6,1)
element(ShellType,2,2,3,8,7,2)
element(ShellType,3,3,4,9,8,2)
element(ShellType,4,4,5,10,9,1)

element(ShellType,5,6,7,12,11,1)
element(ShellType,6,7,8,13,12,2)
element(ShellType,7,8,9,14,13,2)
element(ShellType,8,9,10,15,14,1)

element(ShellType,9,11,12,17,16,1)
element(ShellType,10,12,13,18,17,2)
element(ShellType,11,13,14,19,18,2)
element(ShellType,12,14,15,20,19,1)

element(ShellType,13,16,17,22,21,1)
element(ShellType,14,17,18,23,22,2)
element(ShellType,15,18,19,24,23,2)
element(ShellType,16,19,20,25,24,1)

element(ShellType,17,21,22,27,26,1)
element(ShellType,18,22,23,28,27,2)
element(ShellType,19,23,24,29,28,2)
element(ShellType,20,24,25,30,29,1)

element(ShellType,21,26,27,32,31,1)
element(ShellType,22,27,28,33,32,2)
element(ShellType,23,28,29,34,33,2)
element(ShellType,24,29,30,35,34,1)

element(ShellType,25,31,32,37,36,1)
element(ShellType,26,32,33,38,37,2)
element(ShellType,27,33,34,39,38,2)
element(ShellType,28,34,35,40,39,1)

element(ShellType,29,36,37,42,41,1)
element(ShellType,30,37,38,43,42,2)
element(ShellType,31,38,39,44,43,2)
element(ShellType,32,39,40,45,44,1)

element(ShellType,33,41,42,47,46,1)
element(ShellType,34,42,43,48,47,2)
element(ShellType,35,43,44,49,48,2)
element(ShellType,36,44,45,50,49,1)

element(ShellType,37,46,47,52,51,1)
element(ShellType,38,47,48,53,52,2)
element(ShellType,39,48,49,54,53,2)
element(ShellType,40,49,50,55,54,1)

# P-delta columns

element('truss',41,1,6,223.53e-6,7)
element('truss',42,6,11,223.53e-6,7)
element('truss',43,11,16,223.53e-6,7)
element('truss',44,16,21,223.53e-6,7)
element('truss',45,21,26,223.53e-6,7)
element('truss',46,26,31,223.53e-6,7)
element('truss',47,31,36,223.53e-6,7)
element('truss',48,36,41,223.53e-6,7)
element('truss',49,41,46,223.53e-6,7)
element('truss',50,46,51,223.53e-6,7)

element('truss',51,2,7,223.53e-6,7)
element('truss',52,7,12,223.53e-6,7)
element('truss',53,12,17,223.53e-6,7)
element('truss',54,17,22,223.53e-6,7)
element('truss',55,22,27,223.53e-6,7)
element('truss',56,27,32,223.53e-6,7)
element('truss',57,32,37,223.53e-6,7)
element('truss',58,37,42,223.53e-6,7)
element('truss',59,42,47,223.53e-6,7)
element('truss',60,47,52,223.53e-6,7)

element('truss',61,4,9,223.53e-6,7)
element('truss',62,9,14,223.53e-6,7)
element('truss',63,14,19,223.53e-6,7)
element('truss',64,19,24,223.53e-6,7)
element('truss',65,24,29,223.53e-6,7)
element('truss',66,29,34,223.53e-6,7)
element('truss',67,34,39,223.53e-6,7)
element('truss',68,39,44,223.53e-6,7)
element('truss',69,44,49,223.53e-6,7)
element('truss',70,49,54,223.53e-6,7)

element('truss',71,5,10,223.53e-6,7)
element('truss',72,10,15,223.53e-6,7)
element('truss',73,15,20,223.53e-6,7)
element('truss',74,20,25,223.53e-6,7)
element('truss',75,25,30,223.53e-6,7)
element('truss',76,30,35,223.53e-6,7)
element('truss',77,35,40,223.53e-6,7)
element('truss',78,40,45,223.53e-6,7)
element('truss',79,45,50,223.53e-6,7)
element('truss',80,50,55,223.53e-6,7)

# Fix all bottom nodes
fixY(0.0,1,1,1,1,1,1)

# plot_model()

recorder('Node','-file','ReactionPY.txt','-time','-node',1,2,3,4,5,'-dof',1,'reaction')

############################
# Gravity Analysis
############################

print("running gravity")

timeSeries("Linear", 1)					# create TimeSeries for gravity analysis
pattern('Plain',1,1)
load(53,0,-246000.0,0.0,0.0,0.0,0.0)	# apply vertical load

recorder('Node','-file','Disp.txt','-time','-node',53,'-dof',1,'disp')

constraints('Plain')
numberer('RCM')
system('BandGeneral')
test('NormDispIncr',1.0e-4,200)
algorithm('BFGS','-count',100)
integrator('LoadControl',0.1)
analysis('Static')
analyze(10)

print("gravity analysis complete...")

loadConst('-time',0.0)					# Keep the gravity loads for further analysis

wipeAnalysis()

###############################
### Cyclic ANALYSIS
###############################

if(AnalysisType=="Cyclic"):
	
	# This is a load controlled analysis. The input load file "RCshearwall_Load_input.txt" should be in the 
	# .. same folder as the model file.
	
	print("<<<< Running Cyclic Analysis >>>>")
	
	timeSeries('Path',2,'-dt',0.1,'-filePath','RCshearwall_Load_input.txt')
	pattern('Plain',2,2)
	sp(53,1,1)								# construct a single-point constraint object added to the LoadPattern.

	constraints('Penalty',1e20,1e20)
	numberer('RCM')
	system('BandGeneral')
	test('NormDispIncr',1e-05, 100, 1)
	algorithm('KrylovNewton')
	integrator('LoadControl',0.1)
	analysis('Static')
	analyze(700)


#######################
# PUSHOVER ANALYSIS
#######################

if(AnalysisType=="Pushover"):
	
	print("<<<< Running Pushover Analysis >>>>")

	# create a plain load pattern for pushover analysis
	pattern("Plain", 2, 1)
	
	ControlNode=53
	ControlDOF=1
	MaxDisp= 0.020
	DispIncr=0.00001
	NstepsPush=int(MaxDisp/DispIncr)
	
	load(ControlNode, 1.00, 0.0, 0.0, 0.0, 0.0, 0.0)	# Apply a unit reference load in DOF=1
	
	system("BandGeneral")
	numberer("RCM")
	constraints('Penalty',1e20,1e20)
	integrator("DisplacementControl", ControlNode, ControlDOF, DispIncr)
	algorithm('KrylovNewton')
	test('NormDispIncr',1e-05, 1000, 2)
	analysis("Static")
	
	# Create a folder to put the output
	PushDataDir = r'PushoverOut'
	if not os.path.exists(PushDataDir):
		os.makedirs(PushDataDir)
	recorder('Node', '-file', "PushoverOut/React.out", '-closeOnWrite', '-node', 1, 2, 3, 4, 5, '-dof',1, 'reaction')
	recorder('Node', '-file', "PushoverOut/Disp.out", '-closeOnWrite', '-node', ControlNode, '-dof',1, 'disp')

	# Perform pushover analysis
	dataPush = np.zeros((NstepsPush+1,5))
	for j in range(NstepsPush):
		analyze(1)
		dataPush[j+1,0] = nodeDisp(ControlNode,1)*1000		# Convert to mm
		dataPush[j+1,1] = -getLoadFactor(2)*0.001			# Convert to kN
		
	# Read test output data to plot
	Test = np.loadtxt("RCshearwall_TestOutput.txt", delimiter="\t", unpack="False")
	
	## Set parameters for the plot
	plt.rcParams.update({'font.size': 7})
	plt.figure(figsize=(4,3), dpi=100)
	plt.rc('font', family='serif')
	plt.plot(Test[0,:], Test[1,:], color="black", linewidth=0.8, linestyle="--", label='Test')
	plt.plot(dataPush[:,0], -dataPush[:,1], color="red", linewidth=1.2, linestyle="-", label='Pushover')
	plt.axhline(0, color='black', linewidth=0.4)
	plt.axvline(0, color='black', linewidth=0.4)
	plt.xlim(-25, 25)
	plt.xticks(np.linspace(-20,20,11,endpoint=True)) 
	plt.grid(linestyle='dotted') 
	plt.xlabel('Displacement (mm)')
	plt.ylabel('Base Shear (kN)')
	plt.legend()
	plt.savefig("PushoverOut/RCshearwall_PushoverCurve.png",dpi=1200)
	plt.show()
	
	
	print("Pushover analysis complete")