
##############################################################

from openseespy.opensees import *
from openseespy.postprocessing.Get_Rendering import * 

import numpy as np
from math import asin, sqrt

wipe()

AnalysisType = "Gravity" # Gravity  Pushover

model('Basic', '-ndm', 3, '-ndf', 6)

# units kip, ft
numBayX = 5
numBayY = 5
numFloor = 11

bayWidthX = 120.0
bayWidthY = 120.0
storyHeights = [162.0, 162.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0]

E = 29500.0
massX = 0.49
M = 0.
coordTransf = "Linear"  # Linear, PDelta, Corotational
massType = "-lMass"  # -lMass, -cMass

nodeTag = 1

# add the nodes
#  - floor at a time
zLoc = 0.
for k in range(0, numFloor + 1):
	xLoc = 0. 
	for i in range(0, numBayX + 1):
		yLoc = 0.
		for j in range(0, numBayY + 1):
			node(nodeTag, xLoc, yLoc, zLoc)
			mass(nodeTag, massX, massX, 0.01, 1.0e-10, 1.0e-10, 1.0e-10)
			if k == 0:
				fix(nodeTag, 1, 1, 1, 1, 1, 1)
				
			yLoc += bayWidthY
			nodeTag += 1
			
		xLoc += bayWidthX

	if k < numFloor:
		storyHeight = storyHeights[k]
	
	zLoc += storyHeight

geomTransf(coordTransf, 1, 1, 0, 0)
geomTransf(coordTransf, 2, 0, 0, 1)

eleTag = 1
nodeTag1 = 1

# Add column elements
for k in range(0, numFloor):
	for i in range(0, numBayX+1):
		for j in range(0, numBayY+1):
			nodeTag2 = nodeTag1 + (numBayX+1)*(numBayY+1)
			iNode = nodeCoord(nodeTag1)
			jNode = nodeCoord(nodeTag2)
			element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 50., E, 1000., 1000., 2150., 2150., 1, '-mass', M, massType)
			eleTag += 1
			nodeTag1 += 1

nodeTag1 = 1+ (numBayX+1)*(numBayY+1)
#add beam elements
for j in range(1, numFloor + 1):
	#eleTag = 100*j
	for i in range(0, numBayX):
		for k in range(0, numBayY+1):
			nodeTag2 = nodeTag1 + (numBayY+1)
			iNode = nodeCoord(nodeTag1)
			jNode = nodeCoord(nodeTag2)
			element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 50., E, 1000., 1000., 2150., 2150., 2, '-mass', M, massType)
			eleTag += 1
			nodeTag1 += 1
		
	nodeTag1 += (numBayY+1)

nodeTag1 = 1+ (numBayX+1)*(numBayY+1)

#add beam elements
for j in range(1, numFloor + 1):
	#eleTag = 110*j
	for i in range(0, numBayY+1):
		for k in range(0, numBayX):
			nodeTag2 = nodeTag1 + 1
			iNode = nodeCoord(nodeTag1)
			jNode = nodeCoord(nodeTag2)
			element('elasticBeamColumn', eleTag, nodeTag1, nodeTag2, 50., E, 1000., 1000., 2150., 2150., 2, '-mass', M, massType)
			eleTag += 1
			nodeTag1 += 1
		nodeTag1 += 1

# calculate eigenvalues & print results
numEigen = 7

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
analyze(NstepsGrav)
loadConst('-time', 0.0)

wipeAnalysis()

plot_model()
plot_modeshape(1, 2000)

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

	# Perform pushover analysis
	analyze(NstepsPush)
	

	print("Pushover analysis complete")
