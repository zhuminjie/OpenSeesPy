
##################################################################
## 2D steel frame example.
## 3 story steel building with rigid beam-column connections.  
## This script uses W-section command inOpensees to create steel.. 
## .. beam-column fiber sections. 
##
## By - Anurag Upadhyay, PhD Student, University of Utah.
## Date - 08/06/2018
##################################################################

print("=========================================================")
print("Start 2D Steel Frame Example")

from openseespy.opensees import *

import numpy as np
import matplotlib.pyplot as plt
import os

AnalysisType='Pushover'	;		#  Pushover  Gravity

## ------------------------------
## Start of model generation
## -----------------------------
# remove existing model
wipe()

# set modelbuilder
model('basic', '-ndm', 2, '-ndf', 3)

import math

############################################
### Units and Constants  ###################
############################################

inch = 1;
kip = 1;
sec = 1;

# Dependent units
sq_in = inch*inch;
ksi = kip/sq_in;
ft = 12*inch;

# Constants
g = 386.2*inch/(sec*sec);
pi = math.acos(-1);

#######################################
##### Dimensions 
#######################################

# Dimensions Input
H_story=10.0*ft;
W_bayX=16.0*ft;
W_bayY_ab=5.0*ft+10.0*inch;
W_bayY_bc=8.0*ft+4.0*inch;
W_bayY_cd=5.0*ft+10.0*inch;

# Calculated dimensions
W_structure=W_bayY_ab+W_bayY_bc+W_bayY_cd;

################
### Material
################

# Steel02 Material 

matTag=1;
matConnAx=2;
matConnRot=3;

Fy=60.0*ksi;		# Yield stress 
Es=29000.0*ksi;		# Modulus of Elasticity of Steel 
v=0.2;				# Poisson's ratio
Gs=Es/(1+v);		# Shear modulus
b=0.10;				# Strain hardening ratio
params=[18.0,0.925,0.15]		# R0,cR1,cR2
R0=18.0
cR1=0.925
cR2=0.15
a1=0.05
a2=1.00
a3=0.05
a4=1.0
sigInit=0.0
alpha=0.05

uniaxialMaterial('Steel02', matTag, Fy, Es, b, R0, cR1, cR2, a1, a2, a3, a4, sigInit)

# ##################
# ## Sections
# ##################

colSecTag1=1;
colSecTag2=2;
beamSecTag1=3;
beamSecTag2=4;
beamSecTag3=5;

# COMMAND: section('WFSection2d', secTag, matTag, d, tw, bf, tf, Nfw, Nff)

section('WFSection2d', colSecTag1, matTag, 10.5*inch, 0.26*inch, 5.77*inch, 0.44*inch, 15, 16)		# outer Column
section('WFSection2d', colSecTag2, matTag, 10.5*inch, 0.26*inch, 5.77*inch, 0.44*inch, 15, 16)		# Inner Column

section('WFSection2d', beamSecTag1, matTag, 8.3*inch, 0.44*inch, 8.11*inch, 0.685*inch, 15, 15)		# outer Beam
section('WFSection2d', beamSecTag2, matTag, 8.2*inch, 0.40*inch, 8.01*inch, 0.650*inch, 15, 15)		# Inner Beam
section('WFSection2d', beamSecTag3, matTag, 8.0*inch, 0.40*inch, 7.89*inch, 0.600*inch, 15, 15)		# Inner Beam

# Beam size - W10x26
Abeam=7.61*inch*inch;
IbeamY=144.*(inch**4);			# Inertia along horizontal axis
IbeamZ=14.1*(inch**4);			# inertia along vertical axis

# BRB input data
Acore=2.25*inch;
Aend=10.0*inch;
LR_BRB=0.55;

# ###########################
# ##### Nodes
# ###########################

# Create All main nodes
node(1, 0.0, 0.0)
node(2, W_bayX, 0.0)
node(3, 2*W_bayX, 0.0)

node(11, 0.0, H_story)
node(12, W_bayX, H_story)
node(13, 2*W_bayX, H_story)

node(21, 0.0, 2*H_story)
node(22, W_bayX, 2*H_story)
node(23, 2*W_bayX, 2*H_story)

node(31, 0.0, 3*H_story)
node(32, W_bayX, 3*H_story)
node(33, 2*W_bayX, 3*H_story)

# Beam Connection nodes

node(1101, 0.0, H_story)
node(1201, W_bayX, H_story)
node(1202, W_bayX, H_story)
node(1301, 2*W_bayX, H_story)

node(2101, 0.0, 2*H_story)
node(2201, W_bayX, 2*H_story)
node(2202, W_bayX, 2*H_story)
node(2301, 2*W_bayX, 2*H_story)

node(3101, 0.0, 3*H_story)
node(3201, W_bayX, 3*H_story)
node(3202, W_bayX, 3*H_story)
node(3301, 2*W_bayX, 3*H_story)

# ###############
#  Constraints
# ###############

fix(1, 1, 1, 1)
fix(2, 1, 1, 1)
fix(3, 1, 1, 1)

# #######################
# ### Elements 
# #######################

# ### Assign beam-integration tags

ColIntTag1=1;
ColIntTag2=2;
BeamIntTag1=3;
BeamIntTag2=4;
BeamIntTag3=5;

beamIntegration('Lobatto', ColIntTag1, colSecTag1, 4)
beamIntegration('Lobatto', ColIntTag2, colSecTag2, 4)
beamIntegration('Lobatto', BeamIntTag1, beamSecTag1, 4)
beamIntegration('Lobatto', BeamIntTag2, beamSecTag2, 4)
beamIntegration('Lobatto', BeamIntTag3, beamSecTag3, 4)

# Assign geometric transformation

ColTransfTag=1
BeamTranfTag=2

geomTransf('PDelta', ColTransfTag)
geomTransf('Linear', BeamTranfTag)


# Assign Elements  ##############

# ## Add non-linear column elements
element('forceBeamColumn', 1, 1, 11, ColTransfTag, ColIntTag1, '-mass', 0.0)
element('forceBeamColumn', 2, 2, 12, ColTransfTag, ColIntTag2, '-mass', 0.0)
element('forceBeamColumn', 3, 3, 13, ColTransfTag, ColIntTag1, '-mass', 0.0)

element('forceBeamColumn', 11, 11, 21, ColTransfTag, ColIntTag1, '-mass', 0.0)
element('forceBeamColumn', 12, 12, 22, ColTransfTag, ColIntTag2, '-mass', 0.0)
element('forceBeamColumn', 13, 13, 23, ColTransfTag, ColIntTag1, '-mass', 0.0)

element('forceBeamColumn', 21, 21, 31, ColTransfTag, ColIntTag1, '-mass', 0.0)
element('forceBeamColumn', 22, 22, 32, ColTransfTag, ColIntTag2, '-mass', 0.0)
element('forceBeamColumn', 23, 23, 33, ColTransfTag, ColIntTag1, '-mass', 0.0)

#

#  ### Add linear main beam elements, along x-axis
#element('elasticBeamColumn', 101, 1101, 1201, Abeam, Es, Gs, Jbeam, IbeamY, IbeamZ, beamTransfTag, '-mass', 0.0)

element('forceBeamColumn', 101, 1101, 1201, BeamTranfTag, BeamIntTag1, '-mass', 0.0)
element('forceBeamColumn', 102, 1202, 1301, BeamTranfTag, BeamIntTag1, '-mass', 0.0)

element('forceBeamColumn', 201, 2101, 2201, BeamTranfTag, BeamIntTag2, '-mass', 0.0)
element('forceBeamColumn', 202, 2202, 2301, BeamTranfTag, BeamIntTag2, '-mass', 0.0)

element('forceBeamColumn', 301, 3101, 3201, BeamTranfTag, BeamIntTag3, '-mass', 0.0)
element('forceBeamColumn', 302, 3202, 3301, BeamTranfTag, BeamIntTag3, '-mass', 0.0)

# Assign constraints between beam end nodes and column nodes (RIgid beam column connections)
equalDOF(11, 1101, 1,2,3)
equalDOF(12, 1201, 1,2,3)
equalDOF(12, 1202, 1,2,3)
equalDOF(13, 1301, 1,2,3)

equalDOF(21, 2101, 1,2,3)
equalDOF(22, 2201, 1,2,3)
equalDOF(22, 2202, 1,2,3)
equalDOF(23, 2301, 1,2,3)

equalDOF(31, 3101, 1,2,3)
equalDOF(32, 3201, 1,2,3)
equalDOF(32, 3202, 1,2,3)
equalDOF(33, 3301, 1,2,3)


################
## Gravity Load 
################
# create TimeSeries
timeSeries("Linear", 1)

# create a plain load pattern
pattern("Plain", 1, 1)

# Create the nodal load
load(11, 0.0, -5.0*kip, 0.0)
load(12, 0.0, -6.0*kip, 0.0)
load(13, 0.0, -5.0*kip, 0.0)

load(21, 0., -5.*kip, 0.0)
load(22, 0., -6.*kip,0.0)
load(23, 0., -5.*kip, 0.0)

load(31, 0., -5.*kip, 0.0)
load(32, 0., -6.*kip, 0.0)
load(33, 0., -5.*kip, 0.0)


# ------------------------------
# Start of analysis generation
# ------------------------------

NstepsGrav = 10

system("BandGEN")
numberer("Plain")
constraints("Plain")
integrator("LoadControl", 1.0/NstepsGrav)
algorithm("Newton")
test('NormUnbalance',1e-8, 10)
analysis("Static")


# perform the analysis
data = np.zeros((NstepsGrav+1,2))
for j in range(NstepsGrav):
    analyze(1)
    data[j+1,0] = nodeDisp(31,2)
    data[j+1,1] = getLoadFactor(1)*5

loadConst('-time', 0.0)
	 
print("Gravity analysis complete")

wipeAnalysis()

###############################
### PUSHOVER ANALYSIS
###############################

if(AnalysisType=="Pushover"):
	
	print("<<<< Running Pushover Analysis >>>>")

	# Create load pattern for pushover analysis
	# create a plain load pattern
	pattern("Plain", 2, 1)

	load(11, 1.61, 0.0, 0.0)
	load(21, 3.22, 0.0, 0.0)
	load(31, 4.83, 0.0, 0.0)
	
	ControlNode=31
	ControlDOF=1
	MaxDisp=0.15*H_story
	DispIncr=0.1
	NstepsPush=int(MaxDisp/DispIncr)
	
	system("ProfileSPD")
	numberer("Plain")
	constraints("Plain")
	integrator("DisplacementControl", ControlNode, ControlDOF, DispIncr)
	algorithm("Newton")
	test('NormUnbalance',1e-8, 10)
	analysis("Static")
	
	PushDataDir = r'PushoverOut'
	if not os.path.exists(PushDataDir):
		os.makedirs(PushDataDir)
	recorder('Node', '-file', "PushoverOut/Node2React.out", '-closeOnWrite', '-node', 2, '-dof',1, 'reaction')
	recorder('Node', '-file', "PushoverOut/Node31Disp.out", '-closeOnWrite', '-node', 31, '-dof',1, 'disp')
	recorder('Element', '-file', "PushoverOut/BeamStress.out", '-closeOnWrite', '-ele', 102, 'section', '4', 'fiber','1', 'stressStrain')

	# analyze(NstepsPush)

	# Perform pushover analysis
	dataPush = np.zeros((NstepsPush+1,5))
	for j in range(NstepsPush):
		analyze(1)
		dataPush[j+1,0] = nodeDisp(31,1)
		reactions()
		dataPush[j+1,1] = nodeReaction(1, 1) + nodeReaction(2, 1) + nodeReaction(3, 1)
		
	plt.plot(dataPush[:,0], -dataPush[:,1])
	plt.xlim(0, MaxDisp)
	plt.xticks(np.linspace(0,MaxDisp,5,endpoint=True)) 
	plt.yticks(np.linspace(0, -int(dataPush[NstepsPush,1]),10,endpoint=True)) 
	plt.grid(linestyle='dotted') 
	plt.xlabel('Top Displacement (inch)')
	plt.ylabel('Base Shear (kip)')
	plt.show()
	
	
	print("Pushover analysis complete")




