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

def createODB(*argv, Nmodes=0, recorders=[]):
	
	"""
	This function creates a directory to save all the output data.

	Command: createODB("ModelName",<"LoadCase Name">, <Nmodes=Nmodes(int)>, <recorders=*recorder(list)>)
	
	ModelName    : (string) Name of the model. The main output folder will be named "ModelName_ODB" in the current directory.
	LoadCase Name: (string), Optional. Name of the load case forder to be created inside the ModelName_ODB folder. If not provided,
					no load case data will be read.
	Nmodes		 : (int) Optional key argument to save modeshape data. Default is 0, no modeshape data is saved.
	
	recorders	 : (string) A list of additional quantities a users would like to record in the output database.
					The arguments for these additional inputs match the standard OpenSees arguments to avoid any confusion.
					'localForce','basicDeformation', 'plasticDeformation','stresses','strains'
					The recorders for node displacement and reactions are saved by default to help plot the deformed shape.
	
	Example: createODB(TwoSpanBridge, Pushover, Nmodes=3, recorders=['stresses', 'strains'])
	
	Future: The integrationPoints output works only for nonlinear beam column elements. If a model has a combination 
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
		ops.recorder('Node', '-file', NodeDispFile,  '-time', '-node', *nodeList, '-dof',*dofList, 'disp')
		ops.recorder('Node', '-file', ReactionFile,  '-time', '-node', *nodeList, '-dof',*dofList, 'reaction')
		
		if 'localForce' in recorders:
			ops.recorder('Element', '-file', EleForceFile,  '-time', '-ele', *eleList, '-dof',*dofList, 'localForce')   
		
		if 'basicDeformation' in recorders:
			ops.recorder('Element', '-file', EleBasicDefFile,  '-time', '-ele', *eleList, '-dof',*dofList, 'basicDeformation')

		if 'plasticDeformation' in recorders:
			ops.recorder('Element', '-file', ElePlasticDefFile,  '-time', '-ele', *eleList, '-dof',*dofList, 'plasticDeformation')  

		if 'stresses' in recorders:
			ops.recorder('Element','-file', EleStressFile,  '-time', '-ele', *eleList,'stresses')
		
		if 'strains' in recorders:
			ops.recorder('Element','-file', EleStrainFile,  '-time', '-ele', *eleList,'strains')
		
		# ops.recorder('Element', '-file', EleIntPointsFile, '-time', '-ele', *eleList, 'integrationPoints')   		# Records IP locations only in NL elements
		
	else:
		print("Insufficient arguments: ModelName and LoadCaseName are required.")
		print("Output from any loadCase will not be saved")
		


def readODB(*argv):
	
	"""
	This function reads saved data from a directory.
	
	Command: readODB("ModelName",<"LoadCase Name">)
	
	ModelName    : (string) Name of the model. The main output folder will be named "ModelName_ODB" in the current directory.
	LoadCase Name: (string), Optional. Name of the load case forder to be created inside the ModelName_ODB folder. If not provided,
					no load case data will be read.
    
	"""
    
	ModelName = argv[0]
	ODBdir = ModelName+"_ODB"		# ODB Dir name

	# Read node and element data in the main Output folder
	nodes, elements = idbf._readNodesandElements(ModelName)
	
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
	Command: plot_model(<"nodes">,<"elements">,<Model="ModelName">)

	nodes	: String, Optional, takes user input to show node tags on the model
	elements: String, Optional, takes user input to show element tags on the model
	Model	: Optional input for the name of the model used in createODB() to read the modeshape data from.
	              The default is "none" and the mode shape is plotted from the active model.
	
	Matplotlib rendering is faster when tags are not displayed.
	
	"""

	##  Default values
	show_node_tags = 'no'
	show_element_tags = 'no'

	if len(argv)>0:
		if any(nodeArg in argv for nodeArg in ["nodes","Nodes","node","Node"]):
			show_node_tags = 'yes'
		if any(eleArg in argv for eleArg in ["elements", "Elements", "element", "Element"]):
			show_element_tags = 'yes'
		if show_node_tags == "no" and show_element_tags == "no":
			raise Exception("Wrong input arguments. Command should be plot_model(<'node'>,<'element'>,Model='model_name')")

	if Model == "none":
		print("No Model_ODB specified, getting data from the active model.")
		nodeArray, elementArray = idbf.getNodesandElements()
	else:
		print("Reading data from the "+Model+"_ODB.")
		nodeArray, elementArray = idbf._readNodesandElements(Model)
		
	nodetags = nodeArray[:,0]
	offset = 0.05				# offset for text
	
	
	def nodecoords(nodetag):
		"""
		Returns an array of node coordinates: works like nodeCoord() in opensees.
		"""
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
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')

	plt.axis('on')
	plt.show()
	return fig

def plot_modeshape(*argv,Model="none"):
	"""
	Command: plot_modeshape(modeNumber,<scale>, <Model="modelName">)
	
	modeNumber : Mode number to be plotted.
	scale      : Optional input to change the scale factor of the deformed shape. Default is 200.
	Model      : Optional input for the name of the model used in createODB() to read the modeshape data from.
	              The default is "none" and the mode shape is plotted from the active model.
	
	"""
	modeNumber = argv[0]
	if len(argv) == 1:
		print("No scale factor specified to plot modeshape, using dafault 200.")
		print("Input arguments are plot_modeshape(modeNumber, scaleFactor, overlap='yes')")
		scale = 200
	elif len(argv) == 2:
		scale = argv[1]
	else:
		raise Exception("Wrong input arguments. Command should be plot_model(ModeNumber,<ScaleFactor>,<Model='model_name'>)")
		
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
		"""
		Returns an array of node coordinates: works like nodeCoord() in opensees.
		"""
		i, = np.where(nodeArray[:,0] == float(nodetag))
		return nodeArray[int(i),1:]
		
	def nodecoordsEigen(nodetag):
		"""
		Returns an array of final deformed node coordinates
		"""
		i, = np.where(nodeArray[:,0] == float(nodetag))				# index for Original coordinates
		ii, = np.where(Mode_nodeArray[:,0] == float(nodetag))		# index for Mode shape coordinates
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
	return fig
	

def plot_deformedshape(Model="none", LoadCase="none", tstep = -1, scale = 200, overlap='no'):
	"""
	Command: plot_deformedshape(Model="modelName", LoadCase="loadCase name", <tstep = time (float)>, <scale = scaleFactor (float)>, <overlap='yes'>)
	
	Model   : Name of the model used in createODB() to read the displacement data from.
	LoadCase: Name of the load case used in createODB().
	tstep   : Optional value of the time stamp in the dynamic analysis. If no specific value is provided, the last step is used.
	scale   : Optional input to change the scale factor of the deformed shape.
	overlap : Optional input to plot the deformed shape overlapped with the original shape.
	
	Future Work: Add option to plot deformed shape based on "time" and "step number" separately.
	
	"""

	if Model == "none" or LoadCase=="none":
		print("No output database specified to plot the deformed shape.")
		print("Command should be plot_deformedshape(Model='modelname',loadCase='loadcase',<tstep=time>,<scale=int>)")
		print("Not plotting deformed shape. Exiting now.")
		
	else:
		print("Reading displacement data from "+str(Model)+"_ODB/"+LoadCase)
		nodeArray, elementArray = idbf._readNodesandElements(Model)
		timeSteps, Disp_nodeArray = idbf._readNodeDispData(Model,LoadCase)
		
		if tstep == -1:
			jj = len(timeSteps)-1
			printLine = "Final deformed shape"
		else:
			jj, = np.where(timeSteps == float(tstep))			# index of the time step requested.
			printLine = "Deformed shape at time: "+str(tstep)+" sec."
		
		DeflectedNodeCoordArray = nodeArray[:,1:]+ scale*Disp_nodeArray[int(jj),:,:]
		nodetags = nodeArray[:,0]
		
		# overlap='yes'						# overlap the modeshape with a wireframe of original shape, set default "yes" for now.
		show_node_tags = 'no'				# Set show tags to "no" to plot modeshape.
		show_element_tags = 'no'

		
		def nodecoords(nodetag):
			# Returns an array of node coordinates: works like nodeCoord() in opensees.
			i, = np.where(nodeArray[:,0] == float(nodetag))
			return nodeArray[int(i),1:]
			
		def nodecoordsFinal(nodetag):
			# Returns an array of final deformed node coordinates
			i, = np.where(nodeArray[:,0] == float(nodetag))				# Original coordinates
			# ii, = np.where(Disp_nodeArray[:,0] == float(nodetag))		# deflected coordinates
			return nodeArray[int(i),1:] + scale*Disp_nodeArray[int(jj),int(i),:]

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
					
					iNode_final = nodecoordsFinal(Nodes[0])
					jNode_final = nodecoordsFinal(Nodes[1])
					
					if overlap == "yes":
						ipltf._plotBeam2D(iNode, jNode, ax, show_element_tags, eleTag, "wire")
					
					ipltf._plotBeam2D(iNode_final, jNode_final, ax, show_element_tags, eleTag, "solid")
					
				if len(Nodes) == 3:
					## 2D Planer three-node shell elements
					iNode = nodeCoord(Nodes[0])
					jNode = nodeCoord(Nodes[1])
					kNode = nodeCoord(Nodes[2])
					
					iNode_final = nodecoordsFinal(Nodes[0])
					jNode_final = nodecoordsFinal(Nodes[1])
					kNode_final = nodecoordsFinal(Nodes[2])

					if overlap == "yes":
						ipltf._plotTri2D(iNode, jNode, kNode, lNode, ax, show_element_tags, eleTag, "wire", fillSurface='no')
					
					ipltf._plotTri2D(iNode_final, jNode_final, kNode_final, lNode_final, ax, show_element_tags, eleTag, "solid", fillSurface='yes')
					
				if len(Nodes) == 4:
					## 2D four-node Quad/shell element
					iNode = nodecoords(Nodes[0])
					jNode = nodecoords(Nodes[1])
					kNode = nodecoords(Nodes[2])
					lNode = nodecoords(Nodes[3])
					
					iNode_final = nodecoordsFinal(Nodes[0])
					jNode_final = nodecoordsFinal(Nodes[1])
					kNode_final = nodecoordsFinal(Nodes[2])
					lNode_final = nodecoordsFinal(Nodes[3])
					
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
					
					iNode_final = nodecoordsFinal(Nodes[0])
					jNode_final = nodecoordsFinal(Nodes[1])
					
					if overlap == "yes":
						ipltf._plotBeam3D(iNode, jNode, ax, show_element_tags, eleTag, "wire")
					
					ipltf._plotBeam3D(iNode_final, jNode_final, ax, show_element_tags, eleTag, "solid")
					
				if len(Nodes) == 4:
					## 3D four-node Quad/shell element
					iNode = nodecoords(Nodes[0])
					jNode = nodecoords(Nodes[1])
					kNode = nodecoords(Nodes[2])
					lNode = nodecoords(Nodes[3])
					
					iNode_final = nodecoordsFinal(Nodes[0])
					jNode_final = nodecoordsFinal(Nodes[1])
					kNode_final = nodecoordsFinal(Nodes[2])
					lNode_final = nodecoordsFinal(Nodes[3])
					
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
					
					iNode_final = nodecoordsFinal(Nodes[0])
					jNode_final = nodecoordsFinal(Nodes[1])
					kNode_final = nodecoordsFinal(Nodes[2])
					lNode_final = nodecoordsFinal(Nodes[3])
					iiNode_final = nodecoordsFinal(Nodes[4])
					jjNode_final = nodecoordsFinal(Nodes[5])
					kkNode_final = nodecoordsFinal(Nodes[6])
					llNode_final = nodecoordsFinal(Nodes[7])
					
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
			ax.text2D(0.10, 0.90, printLine, transform=ax.transAxes)
					
		plt.axis('on')
		plt.show()
		
		return fig
