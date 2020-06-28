##########################################################################################
## This script records the Nodes and Elements in order to render the OpenSees model.	##
## As of now, this procedure does not work for 9 and 20 node brick elements, and 		##
## tetrahedron elements.																##
##																						##
##																						##
## Created By - Anurag Upadhyay, University of Utah. 									##
## 																						##
## You can download more examples from https://github.com/u-anurag						##
##########################################################################################

# Check if the script is executed on Jupyter Notebook Ipython. 
# If yes, force inline, interactive backend for Matplotlib.
import sys
import os
import matplotlib

for line in range(0,len(sys.argv)):
    if "ipykernel_launcher.py" in sys.argv[line]:
        matplotlib.use('nbagg')
        break
    else:
        pass

from mpl_toolkits.mplot3d import Axes3D
from math import asin, sqrt
import matplotlib.pyplot as plt
import numpy as np

#### CHANGE THESE BEFORE COMMITTING, call them before calling openseespy here ####
import openseespy.postprocessing.internal_database_functions as idbf
import openseespy.postprocessing.internal_plotting_functions as ipltf
import openseespy.opensees as ops

#####################################################################
####    All the plotting related definitions start here.
####
#####################################################################

def createODB(*argv, Nmodes=0):
	
	"""
	This function creates a directory to save all the output data.
	Expected input arguments : modelName, loadCase, Selective output quantities in future
	Created folders: modelOutputFolder > loadCaseOutputFolder
	For example: createODB(TwoSpanBridge, Pushover, Nmodes=3)
	
	The integrationPoints output works only for nonlinear beam column elements. If a model has a combination 
	of elastic and nonlienar elements, we need to create a method distinguish. 
	
	"""
	
	ModelName = argv[0]
	ODBdir = ModelName+"_ODB"		# ODB Dir name
	if not os.path.exists(ODBdir):
			os.makedirs(ODBdir)

	nodeList = ops.getNodeTags()
	eleList = ops.getEleTags()
	
	if len(ops.nodeCoord(nodeList[0])) == 2:
		dofList = [1, 2]
	if len(ops.nodeCoord(nodeList[0])) == 3:
		dofList = [1, 2, 3]
	
	# Save node and element data in the main Output folder
	idbf._saveNodesandElements(ModelName)
	
	#########################
	## Create mode shape dir
	#########################
	if Nmodes > 0:
		ModeShapeDir = os.path.join(ODBdir,"ModeShapes")
		if not os.path.exists(ModeShapeDir):
			os.makedirs(ModeShapeDir)
			
		## Run eigen analysis internally and get information to print
		Tarray = np.zeros([1,Nmodes])  # To save all the periods of vibration
		ops.wipeAnalysis()
		eigenVal = ops.eigen(Nmodes+1)
	
		for m in range(1,Nmodes+1):
			Tarray[0,m-1]=4*asin(1.0)/(eigenVal[m-1])**0.5
		
		modeTFile = os.path.join(ModeShapeDir, "ModalPeriods.out")
		np.savetxt(modeTFile, Tarray, delimiter = ' ', fmt = '%.5e')   
		
		### Save mode shape data
		for i in range(1,Nmodes+1):
			idbf._saveModeShapeData(ModelName,i)
		
		ops.wipeAnalysis()
		
	# Define standard outout filenames
	if len(argv)>=2:
		LoadCaseName = argv[1]
		LoadCaseDir = os.path.join(ODBdir,LoadCaseName)

		if not os.path.exists(LoadCaseDir):
			os.makedirs(LoadCaseDir)
			
		NodeDispFile = os.path.join(LoadCaseDir,"NodeDisp_All.out")
		EleForceFile = os.path.join(LoadCaseDir,"EleForce_All.out")
		ReactionFile = os.path.join(LoadCaseDir,"Reaction_All.out")
		EleStressFile = os.path.join(LoadCaseDir,"EleStress_All.out")
		EleStrainFile = os.path.join(LoadCaseDir,"EleStrain_All.out")
		EleBasicDefFile = os.path.join(LoadCaseDir,"EleBasicDef_All.out")
		ElePlasticDefFile = os.path.join(LoadCaseDir,"ElePlasticDef_All.out")
		EleIntPointsFile = os.path.join(LoadCaseDir,"EleIntPoints_All.out")
		
		# Save recorders in the ODB folder

		ops.recorder('Node', '-file', NodeDispFile, '-node', *nodeList, '-dof',*dofList, 'disp')
		ops.recorder('Node', '-file', ReactionFile, '-node', *nodeList, '-dof',*dofList, 'reaction')
		ops.recorder('Element', '-file', EleForceFile, '-ele', *eleList, '-dof',*dofList, 'localForce')   
		ops.recorder('Element', '-file', EleBasicDefFile, '-ele', *eleList, '-dof',*dofList, 'basicDeformation')   
		ops.recorder('Element', '-file', ElePlasticDefFile, '-ele', *eleList, '-dof',*dofList, 'plasticDeformation')   
		ops.recorder('Element','-file', EleStressFile, '-ele', *eleList,'stresses')
		ops.recorder('Element','-file', EleStrainFile, '-ele', *eleList,'strains')
		# ops.recorder('Element', '-file', EleIntPointsFile, '-ele', *eleList, 'integrationPoints')   		# Records IP locations only in NL elements
		
	else:
		print("Insufficient arguments: ModelName and LoadCaseName are required.")
		print("Output from any loadCase will not be saved")
		


def readODB(*argv):
	"""
	This function reads saved data from a directory.
	Expected input arguments : modelName, loadCase, Selective output quantities in future
	Created folders: modelOutputFolder > loadCaseOutputFolder
	For example: createODB(TwoSpanBridge, Pushover)
	If only one input argument is provided, no load case data is read.
    	
	The integrationPoints output works only for nonlinear beam column elements. If a model has a combination 
	of elastic and nonlienar elements, we need to create a method distinguish. 
    
	First record all the output data and then read it instantly for plotting.
	"""
    
	ModelName = argv[0]
	ODBdir = ModelName+"_ODB"		# ODB Dir name

	# Read node and element data in the main Output folder
	nodes, elements = idbf._readNodesandElements(ModelName)
	
	# print(nodes)
	# print(elements)
	  	
	if len(argv)>=2:
		LoadCaseName = argv[1]
		LoadCaseDir = os.path.join(ODBdir, LoadCaseName)

		if not os.path.exists(LoadCaseDir):
			print("No database found")
		
		# Define standard outout filenames
		NodeDispFile = os.path.join(LoadCaseDir,"NodeDisp_All.out")
		EleForceFile = os.path.join(LoadCaseDir,"EleForce_All.out")
		ReactionFile = os.path.join(LoadCaseDir,"Reaction_All.out")
		EleStressFile = os.path.join(LoadCaseDir,"EleStress_All.out")
		EleStrainFile = os.path.join(LoadCaseDir,"EleStrain_All.out")
		EleBasicDefFile = os.path.join(LoadCaseDir,"EleBasicDef_All.out")
		ElePlasticDefFile = os.path.join(LoadCaseDir,"ElePlasticDef_All.out")
		EleIntPointsFile = os.path.join(LoadCaseDir,"EleIntPoints_All.out")
		
		# Read recorders in the ODB folder
		# FUTURE: Gives warning if the files are empty. Create a procedure to check if files are empty.
		NodeDisp = np.loadtxt(NodeDispFile,delimiter=' ')
		EleForce = np.loadtxt(EleForceFile,delimiter=' ')   
		Reaction = np.loadtxt(ReactionFile,delimiter=' ')
		# EleStress = np.loadtxt(EleStressFile,delimiter=' ')
		# EleStrain = np.loadtxt(EleStrainFile,delimiter=' ')   
		# EleBasicDef = np.loadtxt(EleBasicDefFile,delimiter=' ')
		# ElePlasticDef = np.loadtxt(ElePlasticDefFile,delimiter=' ')
		return nodes, elements, NodeDisp, Reaction, EleForce
	
	else:
		return nodes, elements


### All the plotting related definitions start here.

ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
node_style = {'color':'black', 'marker':'o', 'facecolor':'black','linewidth':0.} 
node_text_style = {'fontsize':6, 'fontweight':'regular', 'color':'green'} 
ele_text_style = {'fontsize':6, 'fontweight':'bold', 'color':'darkred'} 

WireEle_style = {'color':'black', 'linewidth':1, 'linestyle':':'} # elements
Eig_style = {'color':'red', 'linewidth':1, 'linestyle':'-'} # elements
	
def plot_model(*argv,Model="none"):
	""" 
	Expected input arguments are "nodes", "elements" and Model="model name" to read the ODB.
	The default Model is "None". If a specific model name is given, the data will be read from the 
	previously created output database.
	"""
	### Options to display node and element tags. Matplotlib rendering is faster when tags are not displayed.
	##  Default values
	show_node_tags = 'no'
	show_element_tags = 'no'
	
	if len(argv)>0 and any(nodeArg in argv for nodeArg in ["nodes","Nodes","node","Node"]):
		show_node_tags = 'yes'
		
	if len(argv)>0 and any(eleArg in argv for eleArg in ["elements", "Elements", "element", "Element"]):
		show_element_tags = 'yes'
	
	if Model == "none":
		print("No Model_ODB specified")
		nodeArray, elementArray = idbf.getNodesandElements()
	else:
		print("Reading data from the Model_ODB")
		nodeArray, elementArray = idbf._readNodesandElements(Model)
		
	nodetags = nodeArray[:,0]
	offset = 0.05				# offset for text
	
	
	def nodecoords(nodetag):
		# Returns an array of node coordinates: works like nodeCoord() in opensees.
		i, = np.where(nodeArray[:,0] == float(nodetag))
		return nodeArray[int(i),1:]

	# Check if the model is 2D or 3D
	if len(nodecoords(nodetags[0])) == 2:
		print('2D model')
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		
		for ele in elementArray:
			eleTag = int(ele[0])
			Nodes =ele[1:]
			
			if len(Nodes) == 2:
				# 2D beam-column elements
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				
				ipltf._plotBeam2D(iNode, jNode, ax, show_element_tags, eleTag, "solid")
				
			if len(Nodes) == 3:
				# 2D Planer three-node shell elements
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				
				ipltf._plotTri2D(iNode, jNode, kNode, lNode, ax, show_element_tags, eleTag, ele_style, fillSurface='yes')
						
			if len(Nodes) == 4:
				# 2D Planer four-node shell elements
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				lNode = nodecoords(Nodes[3])
				
				ipltf._plotQuad2D(iNode, jNode, kNode, lNode, ax, show_element_tags, eleTag, ele_style, fillSurface='yes')

			
		if show_node_tags == 'yes':
			for node in nodetags:
				ax.text(nodecoords(node)[0]*1.02, nodecoords(node)[1]*1.02, str(int(node)),**node_text_style) #label nodes
			
			ax.scatter(nodeArray[:,1], nodeArray[:,2], **node_style)
			
	
		nodeMins = np.array([min(nodeArray[:,1]),min(nodeArray[:,2])])
		nodeMaxs = np.array([max(nodeArray[:,1]),max(nodeArray[:,2])])
		
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		view_range = max(max(nodeArray[:,1])-min(nodeArray[:,1]), max(nodeArray[:,2])-min(nodeArray[:,2]))
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		
		
	else:
		print('3D model')
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1, projection='3d')
		
		for ele in elementArray:
			eleTag = int(ele[0])
			Nodes =ele[1:]
			
			if len(Nodes) == 2:
				# 3D beam-column elements
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				
				ipltf._plotBeam3D(iNode, jNode, ax, show_element_tags, eleTag, "solid")
				
			if len(Nodes) == 4:
				# 3D four-node Quad/shell element
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				lNode = nodecoords(Nodes[3])
				
				ipltf._plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, eleTag, ele_style, fillSurface='yes')
				
			if len(Nodes) == 8:
				# 3D eight-node Brick element
				# Nodes in CCW on bottom (0-3) and top (4-7) faces resp
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				lNode = nodecoords(Nodes[3])
				iiNode = nodecoords(Nodes[4])
				jjNode = nodecoords(Nodes[5])
				kkNode = nodecoords(Nodes[6])
				llNode = nodecoords(Nodes[7])
				
				ipltf._plotCubeVol(iNode, jNode, kNode, lNode, iiNode, jjNode, kkNode, llNode, ax, show_element_tags, eleTag, 'solid', fillSurface='yes')
				
		if show_node_tags == 'yes':
			for node in nodetags:
				ax.text(nodecoords(node)[0]*1.02, nodecoords(node)[1]*1.02, nodecoords(node)[2]*1.02, str(int(node)),**node_text_style) #label nodes
				
			ax.scatter(nodeArray[:,1], nodeArray[:,2], nodeArray[:,3], **node_style)								# show nodes
				
		
		nodeMins = np.array([min(nodeArray[:,1]),min(nodeArray[:,2]),min(nodeArray[:,3])])
		nodeMaxs = np.array([max(nodeArray[:,1]),max(nodeArray[:,2]),max(nodeArray[:,3])])
		
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		
		view_range = max(max(nodeArray[:,1])-min(nodeArray[:,1]), max(nodeArray[:,2])-min(nodeArray[:,2]), max(nodeArray[:,3])-min(nodeArray[:,3]))

		ax.set_xlim(xViewCenter-(view_range/2), xViewCenter+(view_range/2))
		ax.set_ylim(yViewCenter-(view_range/2), yViewCenter+(view_range/2))
		ax.set_zlim(zViewCenter-(view_range/2), zViewCenter+(view_range/2))
		print(xViewCenter-(view_range/2), xViewCenter+(view_range/2))
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')

	plt.axis('on')
	plt.show()
	

def plot_modeshape(*argv,Model="none"):
	"""
	Expected input argv : modeNumber, scale,  Model name to read ODB. To be added: overlap='yes' or 'no'
	The default Model is "None". If a specific model name is given, the data will be read from the 
	previously created output database.
	"""
	modeNumber = argv[0]
	if len(argv) < 2:
		print("No scale factor specified to plot modeshape, using dafault 200.")
		print("Input arguments are plot_modeshape(modeNumber, scaleFactor, overlap='yes')")
		scale = 200
	else:
		scale = argv[1]
		
	if Model == "none":
		print("No Model_ODB specified to plot modeshapes")
		ops.wipeAnalysis()
		eigenVal = ops.eigen(modeNumber+1)
		Tn=4*asin(1.0)/(eigenVal[modeNumber-1])**0.5
		nodeArray, elementArray = idbf.getNodesandElements()
		Mode_nodeArray = idbf.getModeShapeData(modeNumber)		# DOES NOT GIVE MODAL PERIOD
		ops.wipeAnalysis()
	else:
		print("Reading modeshape data from "+str(Model)+"_ODB")
		nodeArray, elementArray = idbf._readNodesandElements(Model)
		Mode_nodeArray, Periods = idbf._readModeShapeData(Model,modeNumber)
		Tn = Periods[modeNumber-1]
		
	DeflectedNodeCoordArray = nodeArray[:,1:]+ scale*Mode_nodeArray[:,1:]
	nodetags = nodeArray[:,0]
	overlap='yes'		# overlap the modeshape with a wireframe of original shape, set default "yes" for now.
	show_node_tags = 'no'				# Set show tags to "no" to plot modeshape.
	show_element_tags = 'no'

	def nodecoords(nodetag):
		# Returns an array of node coordinates: works like nodeCoord() in opensees.
		i, = np.where(nodeArray[:,0] == float(nodetag))
		return nodeArray[int(i),1:]
		
	def nodecoordsEigen(nodetag):
		# Returns an array of final deformed node coordinates
		i, = np.where(nodeArray[:,0] == float(nodetag))				# Original coordinates
		ii, = np.where(Mode_nodeArray[:,0] == float(nodetag))		# Mode shape coordinates
		return nodeArray[int(i),1:] + scale*Mode_nodeArray[int(ii),1:]

	# Check if the model is 2D or 3D
	if len(nodecoords(nodetags[0])) == 2:
		print('2D model')
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		
		for ele in elementArray:
			eleTag = int(ele[0])
			Nodes =ele[1:]
			
			if len(Nodes) == 2:
				# 3D beam-column elements
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				
				iNode_final = nodecoordsEigen(Nodes[0])
				jNode_final = nodecoordsEigen(Nodes[1])
				
				if overlap == "yes":
					ipltf._plotBeam2D(iNode, jNode, ax, show_element_tags, eleTag, "wire")
				
				ipltf._plotBeam2D(iNode_final, jNode_final, ax, show_element_tags, eleTag, "solid")
				
			if len(Nodes) == 3:
				## 2D Planer three-node shell elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				
				iNode_final = nodecoordsEigen(Nodes[0])
				jNode_final = nodecoordsEigen(Nodes[1])
				kNode_final = nodecoordsEigen(Nodes[2])

				if overlap == "yes":
					ipltf._plotTri2D(iNode, jNode, kNode, lNode, ax, show_element_tags, eleTag, "wire", fillSurface='no')
				
				ipltf._plotTri2D(iNode_final, jNode_final, kNode_final, lNode_final, ax, show_element_tags, eleTag, "solid", fillSurface='yes')
				
			if len(Nodes) == 4:
				## 2D four-node Quad/shell element
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				lNode = nodecoords(Nodes[3])
				
				iNode_final = nodecoordsEigen(Nodes[0])
				jNode_final = nodecoordsEigen(Nodes[1])
				kNode_final = nodecoordsEigen(Nodes[2])
				lNode_final = nodecoordsEigen(Nodes[3])
				
				if overlap == "yes":
					ipltf._plotQuad2D(iNode, jNode, kNode, lNode, ax, show_element_tags, eleTag, "wire", fillSurface='no')
					
				ipltf._plotQuad2D(iNode_final, jNode_final, kNode_final, lNode_final, ax, show_element_tags, eleTag, "solid", fillSurface='yes')
				
		nodeMins = np.array([min(DeflectedNodeCoordArray[:,0]),min(DeflectedNodeCoordArray[:,1])])
		nodeMaxs = np.array([max(DeflectedNodeCoordArray[:,0]),max(DeflectedNodeCoordArray[:,1])])
		
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		view_range = max(max(DeflectedNodeCoordArray[:,0])-min(DeflectedNodeCoordArray[:,0]), max(DeflectedNodeCoordArray[:,1])-min(DeflectedNodeCoordArray[:,1]))
		
		ax.set_xlim(xViewCenter-(1.1*view_range/1), xViewCenter+(1.1*view_range/1))
		ax.set_ylim(yViewCenter-(1.1*view_range/1), yViewCenter+(1.1*view_range/1))
		
		ax.text(0.05, 0.95, "Mode "+str(modeNumber), transform=ax.transAxes)
		ax.text(0.05, 0.90, "T = "+str("%.3f" % Tn)+" s", transform=ax.transAxes)

	
	else:
		print('3D model')
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1, projection='3d')
		
		for ele in elementArray:
			eleTag = int(ele[0])
			Nodes =ele[1:]
			
			if len(Nodes) == 2:
				## 3D beam-column elements
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				
				iNode_final = nodecoordsEigen(Nodes[0])
				jNode_final = nodecoordsEigen(Nodes[1])
				
				if overlap == "yes":
					ipltf._plotBeam3D(iNode, jNode, ax, show_element_tags, eleTag, "wire")
				
				ipltf._plotBeam3D(iNode_final, jNode_final, ax, show_element_tags, eleTag, "solid")
				
			if len(Nodes) == 4:
				## 3D four-node Quad/shell element
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				lNode = nodecoords(Nodes[3])
				
				iNode_final = nodecoordsEigen(Nodes[0])
				jNode_final = nodecoordsEigen(Nodes[1])
				kNode_final = nodecoordsEigen(Nodes[2])
				lNode_final = nodecoordsEigen(Nodes[3])
				
				if overlap == "yes":
					ipltf._plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, eleTag, "wire", fillSurface='no')
					
				ipltf._plotQuad3D(iNode_final, jNode_final, kNode_final, lNode_final, ax, show_element_tags, eleTag, "solid", fillSurface='yes')

			if len(Nodes) == 8:
				## 3D eight-node Brick element
				## Nodes in CCW on bottom (0-3) and top (4-7) faces resp
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])
				iiNode = nodeCoord(Nodes[4])
				jjNode = nodeCoord(Nodes[5])
				kkNode = nodeCoord(Nodes[6])
				llNode = nodeCoord(Nodes[7])
				
				iNode_final = nodecoordsEigen(Nodes[0])
				jNode_final = nodecoordsEigen(Nodes[1])
				kNode_final = nodecoordsEigen(Nodes[2])
				lNode_final = nodecoordsEigen(Nodes[3])
				iiNode_final = nodecoordsEigen(Nodes[4])
				jjNode_final = nodecoordsEigen(Nodes[5])
				kkNode_final = nodecoordsEigen(Nodes[6])
				llNode_final = nodecoordsEigen(Nodes[7])
				
				if overlap == "yes":
					ipltf._plotCubeVol(iNode, jNode, kNode, lNode, iiNode, jjNode, kkNode, llNode, ax, show_element_tags, eleTag, "wire", fillSurface='no') # plot undeformed shape

				ipltf._plotCubeVol(iNode_final, jNode_final, kNode_final, lNode_final, iiNode_final, jjNode_final, kkNode_final, llNode_final, 
								ax, show_element_tags, eleTag, "solid", fillSurface='yes')
								
		nodeMins = np.array([min(DeflectedNodeCoordArray[:,0]),min(DeflectedNodeCoordArray[:,1]),min(DeflectedNodeCoordArray[:,2])])
		nodeMaxs = np.array([max(DeflectedNodeCoordArray[:,0]),max(DeflectedNodeCoordArray[:,1]),max(DeflectedNodeCoordArray[:,2])])
				
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		
		view_range = max(max(DeflectedNodeCoordArray[:,0])-min(DeflectedNodeCoordArray[:,0]), 
							max(DeflectedNodeCoordArray[:,1])-min(DeflectedNodeCoordArray[:,1]), 
							max(DeflectedNodeCoordArray[:,2])-min(DeflectedNodeCoordArray[:,2]))

		ax.set_xlim(xViewCenter-(view_range/2), xViewCenter+(view_range/2))
		ax.set_ylim(yViewCenter-(view_range/2), yViewCenter+(view_range/2))
		ax.set_zlim(zViewCenter-(view_range/2), zViewCenter+(view_range/2))
		ax.text2D(0.10, 0.95, "Mode "+str(modeNumber), transform=ax.transAxes)
		ax.text2D(0.10, 0.90, "T = "+str("%.3f" % Tn)+" s", transform=ax.transAxes)
				
	plt.axis('on')
	plt.show()
	
	
## ANURAG TO CHANGE THE FOLLOWING PROCEDURE to streamline it with reading data from ODB.

def plot_deformedshape(filename = 'nodeDisp.txt', tstep = -1, scale = 200):
	# Expected input argv : filename contains the displacements of all nodes in the same order they are returned by getNodeTags().
	# First column in filename is time. 
	# tstep is the number of the step of the analysis to be ploted (starting from 1), 
	# and scale is the scale factor for the deformed shape.
	
	overlap = "yes" 					# An option to select if overlap with original geometry.
	show_node_tags = 'no'				# Set show tags to "no" to plot modeshape.
	show_element_tags = 'no'

	nodeList = getNodeTags()
	eleList = getEleTags()
	nodeDispArray = np.loadtxt(filename)
	if len(nodeDispArray[0, :]) == len(nodeList) * len(nodeCoord(nodeList[0])):
		tarray = np.zeros((len(nodeDispArray), 1))
		nodeDispArray = np.append(tarray, nodeDispArray, axis = 1) 
  
	if tstep == -1:
		tstep = len(nodeDispArray)
		ele_style = {'color':'black', 'linewidth':1, 'linestyle':':'} # elements
		Disp_style = {'color':'red', 'linewidth':1, 'linestyle':'-'} # elements
		node_style = {'color':'black', 'marker':'.', 'linestyle':''} 

	# Check if the model is 2D or 3D
	if len(nodeCoord(nodeList[0])) == 2:
		print('2D model')
		x = []
		y = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		for element in eleList:
			Nodes = eleNodes(element)
			if len(Nodes) == 2:
				# 3D Beam-Column Elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				iNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[0])*2 + 1: nodeList.index(Nodes[0])*2 + 3]
				jNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[1])*2 + 1: nodeList.index(Nodes[1])*2 + 3]

				# Get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Disp[0], iNode[1]+ scale*iNode_Disp[1]]
				jNode_final = [jNode[0]+ scale*jNode_Disp[0], jNode[1]+ scale*jNode_Disp[1]]

				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area

				if overlap == "yes":
					plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)
				
				plt.plot((iNode_final[0], jNode_final[0]), 
							(iNode_final[1], jNode_final[1]),marker='', **Disp_style)

			if len(Nodes) == 3:
				# 2D Planer three-node shell elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])

				iNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[0])*2 + 1: nodeList.index(Nodes[0])*2 + 3]
				jNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[1])*2 + 1: nodeList.index(Nodes[1])*2 + 3]
				kNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[2])*2 + 1: nodeList.index(Nodes[2])*2 + 3]				# Get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Disp[0], iNode[1]+ scale*iNode_Disp[1]]
				jNode_final = [jNode[0]+ scale*jNode_Disp[0], jNode[1]+ scale*jNode_Disp[1]]
				kNode_final = [kNode[0]+ scale*kNode_Disp[0], kNode[1]+ scale*kNode_Disp[1]]

				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area

				if overlap == "yes":
					ipltf._plotTri2D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, "wire", fillSurface='no')

				ipltf._plotTri2D(iNode_final, jNode_final, kNode_final, lNode_final, ax, show_element_tags, element, "solid", fillSurface='yes')

			if len(Nodes) == 4:
				# 2D Planer four-node shell elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])

				iNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[0])*2 + 1: nodeList.index(Nodes[0])*2 + 3]
				jNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[1])*2 + 1: nodeList.index(Nodes[1])*2 + 3]
				kNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[2])*2 + 1: nodeList.index(Nodes[2])*2 + 3]
				lNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[3])*2 + 1: nodeList.index(Nodes[3])*2 + 3]

				# Get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Disp[0], iNode[1]+ scale*iNode_Disp[1]]
				jNode_final = [jNode[0]+ scale*jNode_Disp[0], jNode[1]+ scale*jNode_Disp[1]]
				kNode_final = [kNode[0]+ scale*kNode_Disp[0], kNode[1]+ scale*kNode_Disp[1]]
				lNode_final = [lNode[0]+ scale*lNode_Disp[0], lNode[1]+ scale*lNode_Disp[1]]

				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area

				if overlap == "yes":
					ipltf._plotQuad2D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, "wire", fillSurface='no')
				
				ipltf._plotQuad2D(iNode_final, jNode_final, kNode_final, lNode_final, ax, show_element_tags, element, "solid", fillSurface='yes')
	
		nodeMins = np.array([min(x),min(y)])
		nodeMaxs = np.array([max(x),max(y)])

		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		view_range = max(max(x)-min(x), max(y)-min(y))
		ax.set_xlim(xViewCenter-(1.1*view_range/1), xViewCenter+(1.1*view_range/1))
		ax.set_ylim(yViewCenter-(1.1*view_range/1), yViewCenter+(1.1*view_range/1))
		ax.text(0.05, 0.95, "Deformed shape ", transform=ax.transAxes)

	if len(nodeCoord(nodeList[0])) == 3:
		print('3D model')
		x = []
		y = []
		z = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1, projection='3d')
		for element in eleList:
			Nodes = eleNodes(element)
			if len(Nodes) == 2:
				# 3D beam-column elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])

				iNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[0])*3 + 1: nodeList.index(Nodes[0])*3 + 4]
				jNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[1])*3 + 1: nodeList.index(Nodes[1])*3 + 4]
				# Add original and deformed shape to get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Disp[0], iNode[1]+ scale*iNode_Disp[1], iNode[2]+ scale*iNode_Disp[2]]
				jNode_final = [jNode[0]+ scale*jNode_Disp[0], jNode[1]+ scale*jNode_Disp[1], jNode[2]+ scale*jNode_Disp[2]]

				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area
				z.append(iNode_final[2])	# list of z coordinates to define plot view area

				if overlap == "yes":
					ipltf._plotBeam3D(iNode, jNode, ax, show_element_tags, element, "wire")
				
				ipltf._plotBeam3D(iNode_final, jNode_final, ax, show_element_tags, element, "solid")
				
			if len(Nodes) == 4:
				# 3D four-node Quad/shell element
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])

				iNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[0])*3 + 1: nodeList.index(Nodes[0])*3 + 4]
				jNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[1])*3 + 1: nodeList.index(Nodes[1])*3 + 4]
				kNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[2])*3 + 1: nodeList.index(Nodes[2])*3 + 4]
				lNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[3])*3 + 1: nodeList.index(Nodes[3])*3 + 4]

				# Add original and mode shape to get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Disp[0], iNode[1]+ scale*iNode_Disp[1], iNode[2]+ scale*iNode_Disp[2]]
				jNode_final = [jNode[0]+ scale*jNode_Disp[0], jNode[1]+ scale*jNode_Disp[1], jNode[2]+ scale*jNode_Disp[2]]
				kNode_final = [kNode[0]+ scale*kNode_Disp[0], kNode[1]+ scale*kNode_Disp[1], kNode[2]+ scale*kNode_Disp[2]]
				lNode_final = [lNode[0]+ scale*lNode_Disp[0], lNode[1]+ scale*lNode_Disp[1], lNode[2]+ scale*lNode_Disp[2]]

				if overlap == "yes":
					ipltf._plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, "wire", fillSurface='no')
					
				ipltf._plotQuad3D(iNode_final, jNode_final, kNode_final, lNode_final, ax, show_element_tags, element, "solid", fillSurface='yes')


			if len(Nodes) == 8:
				# 3D eight-node Brick element
				# Nodes in CCW on bottom (0-3) and top (4-7) faces resp
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])
				iiNode = nodeCoord(Nodes[4])
				jjNode = nodeCoord(Nodes[5])
				kkNode = nodeCoord(Nodes[6])
				llNode = nodeCoord(Nodes[7])

				iNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[0])*3 + 1: nodeList.index(Nodes[0])*3 + 4]
				jNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[1])*3 + 1: nodeList.index(Nodes[1])*3 + 4]
				kNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[2])*3 + 1: nodeList.index(Nodes[2])*3 + 4]
				lNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[3])*3 + 1: nodeList.index(Nodes[3])*3 + 4]
				iiNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[4])*3 + 1: nodeList.index(Nodes[4])*3 + 4]
				jjNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[5])*3 + 1: nodeList.index(Nodes[5])*3 + 4]
				kkNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[6])*3 + 1: nodeList.index(Nodes[6])*3 + 4]
				llNode_Disp = nodeDispArray[tstep - 1, nodeList.index(Nodes[7])*3 + 1: nodeList.index(Nodes[7])*3 + 4]

				# Add original and mode shape to get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Disp[0], iNode[1]+ scale*iNode_Disp[1], iNode[2]+ scale*iNode_Disp[2]]
				jNode_final = [jNode[0]+ scale*jNode_Disp[0], jNode[1]+ scale*jNode_Disp[1], jNode[2]+ scale*jNode_Disp[2]]
				kNode_final = [kNode[0]+ scale*kNode_Disp[0], kNode[1]+ scale*kNode_Disp[1], kNode[2]+ scale*kNode_Disp[2]]
				lNode_final = [lNode[0]+ scale*lNode_Disp[0], lNode[1]+ scale*lNode_Disp[1], lNode[2]+ scale*lNode_Disp[2]]
				iiNode_final = [iiNode[0]+ scale*iiNode_Disp[0], iiNode[1]+ scale*iiNode_Disp[1], iiNode[2]+ scale*iiNode_Disp[2]]
				jjNode_final = [jjNode[0]+ scale*jjNode_Disp[0], jjNode[1]+ scale*jjNode_Disp[1], jjNode[2]+ scale*jjNode_Disp[2]]
				kkNode_final = [kkNode[0]+ scale*kkNode_Disp[0], kkNode[1]+ scale*kkNode_Disp[1], kkNode[2]+ scale*kkNode_Disp[2]]
				llNode_final = [llNode[0]+ scale*llNode_Disp[0], llNode[1]+ scale*llNode_Disp[1], llNode[2]+ scale*llNode_Disp[2]]

				if overlap == "yes":
					ipltf._plotCubeVol(iNode, jNode, kNode, lNode, iiNode, jjNode, kkNode, llNode, ax, show_element_tags, element, "wire", fillSurface='no') # plot undeformed shape

				ipltf._plotCubeVol(iNode_final, jNode_final, kNode_final, lNode_final, iiNode_final, jjNode_final, kkNode_final, llNode_final, 
								ax, show_element_tags, element, "solid", fillSurface='yes')
								
		nodeMins = np.array([min(x),min(y),min(z)])
		nodeMaxs = np.array([max(x),max(y),max(z)])
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		view_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z))
		ax.set_xlim(xViewCenter-(view_range/4), xViewCenter+(view_range/4))
		ax.set_ylim(yViewCenter-(view_range/4), yViewCenter+(view_range/4))
		ax.set_zlim(zViewCenter-(view_range/3), zViewCenter+(view_range/3))
		ax.text2D(0.10, 0.95, "Deformed shape", transform=ax.transAxes)
		ax.text2D(0.10, 0.90, "Step: "+str(tstep), transform=ax.transAxes)
    

	plt.axis('off')
	plt.show()
	return fig
