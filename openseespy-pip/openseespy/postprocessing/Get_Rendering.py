##########################################################################################
## *Only user functions are to be included in this file. For helper/internal functions	##
## go to internal_database_functions.py and internal_plotting_functions.                ##
## *As of now, this procedure does not work for 9 and 20 node brick elements, and       ##
## tetrahedron elements.																##
##																						##
##																						##
## Created By - Anurag Upadhyay, University of Utah. https://github.com/u-anurag		##
##            - Christian Slotboom, University of British Columbia.                     ##
##              https://github.com/cslotboom	                                        ##
## 																						##
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
from math import asin
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from matplotlib.widgets import Slider


#### CHANGE THESE BEFORE COMMITTING, call them before calling openseespy here ####
import openseespy.postprocessing.internal_database_functions as idbf
import openseespy.postprocessing.internal_plotting_functions as ipltf
import openseespy.opensees as ops

#####################################################################
####    All the plotting related definitions start here.
####
#####################################################################

def createODB(*argv, Nmodes=0, deltaT=0.0, recorders=[]):
	
	"""
	This function creates a directory to save all the output data.

	Command: createODB("ModelName",<"LoadCase Name">, <Nmodes=Nmodes(int)>, <recorders=*recorder(list)>)
	
	ModelName    : (string) Name of the model. The main output folder will be named "ModelName_ODB" in the current directory.
	LoadCase Name: (string), Optional. Name of the load case forder to be created inside the ModelName_ODB folder. If not provided,
					no load case data will be read.
	Nmodes		 : (int) Optional key argument to save modeshape data. Default is 0, no modeshape data is saved.
	
	deltaT		 : (float) Optional time interval for recording. will record when next step is deltaT greater than last recorder step. 
					(default: records at every time step)
	
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
# 		EleIntPointsFile = os.path.join(LoadCaseDir,"EleIntPoints_All.out")
		
		# Save recorders in the ODB folder
		ops.recorder('Node', '-file', NodeDispFile,  '-time', '-dT', deltaT, '-node', *nodeList, '-dof',*dofList, 'disp')
		ops.recorder('Node', '-file', ReactionFile,  '-time', '-dT', deltaT, '-node', *nodeList, '-dof',*dofList, 'reaction')
		
		if 'localForce' in recorders:
			ops.recorder('Element', '-file', EleForceFile,  '-time', '-dT', deltaT, '-ele', *eleList, '-dof',*dofList, 'localForce')   
		
		if 'basicDeformation' in recorders:
			ops.recorder('Element', '-file', EleBasicDefFile,  '-time', '-dT', deltaT, '-ele', *eleList, '-dof',*dofList, 'basicDeformation')

		if 'plasticDeformation' in recorders:
			ops.recorder('Element', '-file', ElePlasticDefFile,  '-time', '-dT', deltaT, '-ele', *eleList, '-dof',*dofList, 'plasticDeformation')  

		if 'stresses' in recorders:
			ops.recorder('Element','-file', EleStressFile,  '-time', '-dT', deltaT, '-ele', *eleList,'stresses')
		
		if 'strains' in recorders:
			ops.recorder('Element','-file', EleStrainFile,  '-time', '-dT', deltaT, '-ele', *eleList,'strains')
		
		# ops.recorder('Element', '-file', EleIntPointsFile, '-time', '-dT', deltaT, '-ele', *eleList, 'integrationPoints')   		# Records IP locations only in NL elements
		
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
		# EleStressFile = os.path.join(LoadCaseDir,"EleStress_All.out")
		# EleStrainFile = os.path.join(LoadCaseDir,"EleStrain_All.out")
		# EleBasicDefFile = os.path.join(LoadCaseDir,"EleBasicDef_All.out")
		# ElePlasticDefFile = os.path.join(LoadCaseDir,"ElePlasticDef_All.out")
		# EleIntPointsFile = os.path.join(LoadCaseDir,"EleIntPoints_All.out")
		
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


def saveFiberData2D(ModelName, LoadCaseName, eleNumber, sectionNumber, deltaT = 0.0):
    """
    Model : string
        The name of the input model database.    
    LoadCase : string
        The name of the input loadcase.    
    element : int
        The input element to be recorded
    section : int
        The section in the input element to be recorded.
    deltaT : float, optional
        The time step to be plotted. The program will find the closed time 
        step to the input value. The default is -1.    
    """
    
    #TODO Allow for inputing more than one element/section?
    
	# Consider making these optional arguements
    FibreName = "FiberData"
    ftype = '.out'
    
    ODBdir = ModelName+"_ODB"		# ODB Dir name
    FibreFileName = FibreName  + '_ele_' + str(eleNumber) + '_section_' + str(sectionNumber) + ftype
    FiberDir = os.path.join(ODBdir, LoadCaseName, FibreFileName)
	
    ops.recorder('Element' , '-file', FiberDir, '-time', '-dT', deltaT, '-ele', eleNumber, 'section', str(sectionNumber), 'fiberData')


### All the plotting related definitions start here.

ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
node_style = {'color':'black', 'marker':'o', 'facecolor':'black','linewidth':0.}
node_style_animation = {'color':'black', 'marker':'o','markersize':2., 'linewidth':0.} 

node_text_style = {'fontsize':8, 'fontweight':'regular', 'color':'green'} 
ele_text_style = {'fontsize':8, 'fontweight':'bold', 'color':'darkred'} 

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

	# Process inputs to allow for backwards compatibility
	if len(argv)>0:
		if any(nodeArg in argv for nodeArg in ["nodes","Nodes","node","Node"]):
			show_node_tags = 'yes'
		if any(eleArg in argv for eleArg in ["elements", "Elements", "element", "Element"]):
			show_element_tags = 'yes'
		if show_node_tags == "no" and show_element_tags == "no":
			raise Exception("Wrong input arguments. Command should be plot_model(<'node'>,<'element'>,Model='model_name')")

	# TODO make this a function?
	# Check if their is an output database or not.
	if Model == "none":
		print("No Model_ODB specified, trying to get data from the active model.")
		try:
			nodeArray, elementArray = idbf._getNodesandElements()
		except:
			raise Exception("No Model_ODB specified. No active model found.")
	else:
		print("Reading data from the "+Model+"_ODB.")
		try:
			nodeArray, elementArray = idbf._readNodesandElements(Model)
		except:
			raise Exception("No Model_ODB found. No active model found.")
		
	nodetags = nodeArray[:,0]
	
	
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
				
				ipltf._plotTri2D(iNode, jNode, kNode, ax, show_element_tags, eleTag, ele_style, fillSurface='yes')
						
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
				
        
	ipltf._setStandardViewport(fig, ax, nodeArray[:,1:], len(nodecoords(nodetags[0])))
	plt.axis('on')
	plt.show()
	return fig, ax


def plot_modeshape(*argv,overlap="yes",Model="none"):
	"""
	Command: plot_modeshape(modeNumber,<scale>, <Model="modelName">)
	
	modeNumber : (int) Mode number to be plotted.
	scale      : (int) Optional input to change the scale factor of the deformed shape. Default is 10.
	overlap    : (str) Optional keyword argument to turn overlap off. Default value is "yes"
	Model      : (str) Optional input for the name of the model used in createODB() to read the modeshape data from.
	                   The default is "none" and the mode shape is plotted from the active model.
	
	"""
	modeNumber = argv[0]
	if len(argv) == 1:
		print("No scale factor specified to plot modeshape, using dafault 10.")
		print("Input arguments are plot_modeshape(modeNumber, scaleFactor, overlap='yes')")
		scale = 10
	elif len(argv) == 2:
		scale = argv[1]
	else:
		raise Exception("Wrong input arguments. Command should be plot_model(ModeNumber,<ScaleFactor>,<Model='model_name'>)")
		
	if Model == "none":
		print("No Model_ODB specified to plot modeshapes")
		ops.wipeAnalysis()
		eigenVal = ops.eigen(modeNumber+1)
		Tn=4*asin(1.0)/(eigenVal[modeNumber-1])**0.5
		nodeArray, elementArray = idbf._getNodesandElements()
		Mode_nodeArray = idbf._getModeShapeData(modeNumber)		# DOES NOT GIVE MODAL PERIOD
		ops.wipeAnalysis()
	else:
		print("Reading modeshape data from "+str(Model)+"_ODB")
		nodeArray, elementArray = idbf._readNodesandElements(Model)
		Mode_nodeArray, Periods = idbf._readModeShapeData(Model,modeNumber)
		Tn = Periods[modeNumber-1]
				
	DeflectedNodeCoordArray = nodeArray[:,1:]+ scale*Mode_nodeArray[:,1:]
	nodetags = nodeArray[:,0]
	show_element_tags = 'no'	# No node or element tags are to be displayed on modeshape plots.

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
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				
				iNode_final = nodecoordsEigen(Nodes[0])
				jNode_final = nodecoordsEigen(Nodes[1])
				kNode_final = nodecoordsEigen(Nodes[2])

				if overlap == "yes":
					ipltf._plotTri2D(iNode, jNode, kNode, iNode, ax, show_element_tags, eleTag, "wire", fillSurface='no')
				
				ipltf._plotTri2D(iNode_final, jNode_final, kNode_final, iNode_final, ax, show_element_tags, eleTag, "solid", fillSurface='yes')
				
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
				iNode = nodecoords(Nodes[0])
				jNode = nodecoords(Nodes[1])
				kNode = nodecoords(Nodes[2])
				lNode = nodecoords(Nodes[3])
				iiNode = nodecoords(Nodes[4])
				jjNode = nodecoords(Nodes[5])
				kkNode = nodecoords(Nodes[6])
				llNode = nodecoords(Nodes[7])
				
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
								
		ax.text2D(0.10, 0.95, "Mode "+str(modeNumber), transform=ax.transAxes)
		ax.text2D(0.10, 0.90, "T = "+str("%.3f" % Tn)+" s", transform=ax.transAxes)

				
	ipltf._setStandardViewport(fig, ax, DeflectedNodeCoordArray, len(nodecoords(nodetags[0])))
	plt.axis('on')
	plt.show()
	return fig, ax
	

def plot_deformedshape(Model="none", LoadCase="none", tstep = -1, scale = 10, overlap='no'):
	"""
	Command: plot_deformedshape(Model="modelName", LoadCase="loadCase name", <tstep = time (float)>, <scale = scaleFactor (float)>, <overlap='yes'>)
	
	Keyword arguments are used to make the command clear.
	
	Model   : Name of the model used in createODB() to read the displacement data from.
	LoadCase: Name of the load case used in createODB().
	tstep   : Optional value of the time stamp in the dynamic analysis. If no specific value is provided, the last step is used.
	scale   : Optional input to change the scale factor of the deformed shape. Default is 10.
	overlap : Optional input to plot the deformed shape overlapped with the wire frame of the original shape.
	
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
			jj = (np.abs(timeSteps - tstep)).argmin()			# index closest to the time step requested.
			if timeSteps[-1] < tstep:
				print("XX Warining: Time-Step has exceeded maximum analysis time step XX")
			printLine = "Deformation at time: " + str(round(timeSteps[jj], 2))
		
		DeflectedNodeCoordArray = nodeArray[:,1:]+ scale*Disp_nodeArray[int(jj),:,:]
		nodetags = nodeArray[:,0]
		
		show_element_tags = 'no'			# Set show tags to "no" to plot deformed shapes.

		
		def nodecoords(nodetag):
			# Returns an array of node coordinates: works like nodeCoord() in opensees.
			i, = np.where(nodeArray[:,0] == float(nodetag))
			return nodeArray[int(i),1:]

        # TODO C: Can we just return DeflectedNodeCoordArray here instead of summing?
		def nodecoordsFinal(nodetag):
			# Returns an array of final deformed node coordinates
			i, = np.where(nodeArray[:,0] == float(nodetag))				# Original coordinates
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
					iNode = nodecoords(Nodes[0])
					jNode = nodecoords(Nodes[1])
					kNode = nodecoords(Nodes[2])
					
					iNode_final = nodecoordsFinal(Nodes[0])
					jNode_final = nodecoordsFinal(Nodes[1])
					kNode_final = nodecoordsFinal(Nodes[2])

					if overlap == "yes":
						ipltf._plotTri2D(iNode, jNode, kNode, iNode, ax, show_element_tags, eleTag, "wire", fillSurface='no')
					
					ipltf._plotTri2D(iNode_final, jNode_final, kNode_final, iNode_final, ax, show_element_tags, eleTag, "solid", fillSurface='yes')
					
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
					            
			ax.text(0.1, 0.90, printLine, transform=ax.transAxes)
		
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
					iNode = nodecoords(Nodes[0])
					jNode = nodecoords(Nodes[1])
					kNode = nodecoords(Nodes[2])
					lNode = nodecoords(Nodes[3])
					iiNode = nodecoords(Nodes[4])
					jjNode = nodecoords(Nodes[5])
					kkNode = nodecoords(Nodes[6])
					llNode = nodecoords(Nodes[7])
					
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
									
			ax.text2D(0.1, 0.90, printLine, transform=ax.transAxes)
		ipltf._setStandardViewport(fig, ax, DeflectedNodeCoordArray, len(nodecoords(nodetags[0])))					
		plt.axis('on')
		plt.show()
		
		return fig, ax


def animate_deformedshape( Model = 'none', LoadCase = 'none', dt = 0, tStart = 0, tEnd = 0, scale = 10, fps = 24, 
                          FrameInterval = 0, timeScale = 1, Movie='none'):
    """
    This defines the animation of an opensees model, given input data.
    
    For big models it's unlikely that the animation will actually run at the 
    desired fps in "real time". Matplotlib just isn't built for high fps 
    animation.
    Parameters
    ----------
    Model : string
        The name of the input model database.    
    LoadCase : string
        The name of the input loadcase.    
    dt : 1D array
        The time step between frames in the input file. The input file should
        have approximately the same number of time between each step or the
        animation will appear to speed up or slow down.
    tStart: float, optional
        The start time for animation. It can be approximate value and the program 
        will find the closest matching time step.
    tEnd: float, optional
        The end time for animation. It can be approximate value and the program 
        will find the closest matching time step.
    NodeFileName : Str
        Name of the input node information file.
    ElementFileName : Str
        Name of the input element connectivity file.
    scale :  float, optional
        The scale on the xy/xyz displacements. The default is 1.
    fps : TYPE, optional
        The frames per second to be displayed. These values are dubious at best
        The default is 24.
    FrameInterval : float, optional
        The time interval between frames to be used. The default is 0.
    timeScale : TYPE, optional
        DESCRIPTION. The default is 1.
    Movie : str, optional 
        Name of the movie file if the user wants to save the animation as .mp4 file.
    Returns
    -------
    TYPE
        Earthquake animation.
    """
    
    if (Model == 'none') or ( LoadCase == 'none') or ( dt == 0):
        raise Exception('Invalid inputs given. Please specify a model database, a load case, and a timestep')
    
    
    # Read Disp From ODB
    #TODO error handeling?
    time, Disp = idbf._readNodeDispData(Model,LoadCase)
    
    nodes, elements = idbf._readNodesandElements(Model)
    Disp = Disp*scale
    
    # Reshape array
    Ntime = len(Disp[:,0])
    ndm = len(nodes[0,1:])
    Nnodes = int((len(Disp[0,:]))/ndm)
    
    # Get nodes and elements
    ndm = len(nodes[0,1:])
    Nnodes = len(nodes[:,0])
    Nele = len(elements)
    
    nodeLabels = nodes[:, 0]       

    # initialize figure
    fig, ax = ipltf._initializeFig(nodes[:,1:], ndm, Disp)    
    plt.subplots_adjust(bottom=.15) # Add extra space bellow graph
    
	# Adjust plot area.   
    ipltf._setStandardViewport(fig, ax, nodes[:,1:], ndm, Disp)
         
       
    # ========================================================================
    # Initialize Plots
    # ========================================================================
    
    initialDisp = nodes[:, 1:] + Disp[0,:,:]
    
    # Add Text
    if ndm == 2:
        time_text = ax.text(0.95, 0.01, '', verticalalignment='bottom', 
                            horizontalalignment='right', transform=ax.transAxes, color='blue')
        
        EQObjects = ipltf._plotEle_2D(nodes, elements, initialDisp, fig, ax, show_element_tags = 'no')
        [EqfigLines, EqfigSurfaces, EqfigText] = EQObjects 
        EqfigNodes, = ax.plot(Disp[0,:,0],Disp[0,:,1], **node_style_animation)  
                    
    if ndm == 3:
        time_text = ax.text2D(0.95, 0.01, '', verticalalignment='bottom', 
                            horizontalalignment='right', transform=ax.transAxes, color='blue')
        EQObjects = ipltf._plotEle_3D(nodes, elements, initialDisp, fig, ax, show_element_tags = 'no')
        [EqfigLines, EqfigSurfaces, EqfigText] = EQObjects 
        EqfigNodes, = ax.plot(Disp[0,:,0], Disp[0,:,1], Disp[0,:,2], **node_style_animation)  

    # ========================================================================
    # Animation
    # ========================================================================
   
    # scale on displacement
    dtInput  = dt
    dtFrames  = 1/fps
    Ntime = len(Disp[:,0])
    Frames = np.arange(0,Ntime)
    framesTime = Frames*dt

    # If the interval is zero
    if FrameInterval == 0:
        FrameInterval = dtFrames*1000/timeScale
    else: 
        pass    
        
    FrameStart = Frames[0]
    FrameEnd = Frames[-1]
	
    if tStart != 0:
        jj = (np.abs(time - tStart)).argmin()
        FrameStart = Frames[jj]
	
    if tEnd != 0:
        if time[-1] < tEnd:
            print("XX Warining: tEnd has exceeded maximum analysis time step XX")
            print("XX tEnd has been set to final analysis time step XX")
        elif tEnd <= tStart:
            print("XX Input Warning: tEnd should be greater than tStart XX")
            print("XX tEnd has been set to final analysis time step XX")
        else:
            kk = (np.abs(time - tEnd)).argmin()
            FrameEnd = Frames[kk]

    aniFrames = FrameEnd-FrameStart  # Number of frames to be animated
	
    # Slider Location and size relative to plot
    # [x, y, xsize, ysize]
    axSlider = plt.axes([0.25, .03, 0.50, 0.02])
    plotSlider = Slider(axSlider, 'Time', framesTime[FrameStart], framesTime[FrameEnd], valinit=framesTime[FrameStart])
    
    # Animation controls
    global is_paused
    is_paused = False # True if user has taken control of the animation   
    
    def on_click(event):
        # Check where the click happened
        (xm,ym),(xM,yM) = plotSlider.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # Toggle on off based on clicking
            global is_paused
            if is_paused == True:
                is_paused=False
            elif is_paused == False:
                is_paused=True
                
    def animate2D_slider(Time):
        """
        The slider value is liked with the plot - we update the plot by updating
        the slider.
        """
        global is_paused
        is_paused=True
        # Convert time to frame
        TimeStep = (np.abs(framesTime - Time)).argmin()
               
        # The current node coordinants in (x,y) or (x,y,z)
        CurrentNodeCoords =  nodes[:,1:] + Disp[TimeStep,:,:]
        # Update Plots
        
        # update node locations
        EqfigNodes.set_xdata(CurrentNodeCoords[:,0]) 
        EqfigNodes.set_ydata(CurrentNodeCoords[:,1])
           
        # Get new node mapping
        # I don't like doing this loop every time - there has to be a faster way
        xy_labels = {}
        for jj in range(Nnodes):
            xy_labels[nodeLabels[jj]] = CurrentNodeCoords[jj,:]
        
        # Define the surface
        SurfCounter = 0
        
        # update element locations
        for jj in range(Nele):
            # Get the node number for the first and second node connected by the element
            TempNodes = elements[jj][1:]
            # This is the xy coordinates of each node in the group
            TempNodeCoords = [xy_labels[node] for node in TempNodes] 
            coords_x = [xy[0] for xy in TempNodeCoords]
            coords_y = [xy[1] for xy in TempNodeCoords]
            
            # Update element lines    
            EqfigLines[jj].set_xdata(coords_x)
            EqfigLines[jj].set_ydata(coords_y)
            # print('loop start')
            # Update the surface if necessary
            if 2 < len(TempNodes):
                tempxy = np.column_stack([coords_x, coords_y])
                EqfigSurfaces[SurfCounter].xy = tempxy
                SurfCounter += 1
       
        # update time Text
        # time_text.set_text("Time= "+'%.2f' % time[TimeStep]+ " s")
        
        # redraw canvas while idle
        fig.canvas.draw_idle()    
            
        return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText

    def animate3D_slider(Time):
        
        
        global is_paused
        is_paused=True
        TimeStep = (np.abs(framesTime - Time)).argmin()
        
        # this is the most performance critical area of code
        
        # The current node coordinants in (x,y) or (x,y,z)
        CurrentNodeCoords =  nodes[:,1:] + Disp[TimeStep,:,:]
        # Update Plots
        
        # update node locations
        EqfigNodes.set_data_3d(CurrentNodeCoords[:,0], CurrentNodeCoords[:,1], CurrentNodeCoords[:,2])
               
        # Get new node mapping
        # I don't like doing this loop every time - there has to be a faster way
        xyz_labels = {}
        for jj in range(Nnodes):
            xyz_labels[nodeLabels[jj]] = CurrentNodeCoords[jj,:]        
    
        SurfCounter = 0
            
        # update element locations
        for jj in range(Nele):
            # Get the node number for the first and second node connected by the element
            TempNodes = elements[jj][1:]
            # This is the xy coordinates of each node in the group
            TempNodeCoords = [xyz_labels[node] for node in TempNodes] 
            coords_x = [xyz[0] for xyz in TempNodeCoords]
            coords_y = [xyz[1] for xyz in TempNodeCoords]
            coords_z = [xyz[2] for xyz in TempNodeCoords]
            
            # Update element Plot    
            EqfigLines[jj].set_data_3d(coords_x, coords_y, coords_z)
            
            if len(TempNodes) > 2:
                # Update 3D surfaces
                tempVec = np.zeros([4,4])
                tempVec[0,:] = coords_x
                tempVec[1,:] = coords_y
                tempVec[2,:] = coords_z
                tempVec[3,:] = EqfigSurfaces[SurfCounter]._vec[3,:]
                EqfigSurfaces[SurfCounter]._vec = tempVec
                SurfCounter += 1
                
        # update time Text
        # time_text.set_text("Time= "+'%.3f' % time[TimeStep]+ " s")
        
        # redraw canvas while idle
        fig.canvas.draw_idle()   

        return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText

    def update_plot(ii):
        # If the control is manual, we don't change the plot    
        global is_paused
        if is_paused:
            return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText
       
        # Find the close timeStep and plot that
        CurrentTime = plotSlider.val
        CurrentFrame = (np.abs(framesTime - CurrentTime)).argmin()

        CurrentFrame += 1
        if CurrentFrame >= FrameEnd:
            CurrentFrame = FrameStart
        
        # Update the slider
        plotSlider.set_val(framesTime[CurrentFrame])
        
        is_paused = False # the above line called update_slider, so we need to reset this
        return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText

    if ndm == 2:
        plotSlider.on_changed(animate2D_slider)
    elif ndm == 3:
        plotSlider.on_changed(animate3D_slider)
    
    # assign click control
    fig.canvas.mpl_connect('button_press_event', on_click)

    ani = animation.FuncAnimation(fig, update_plot, aniFrames, interval = FrameInterval)
	
    if Movie != "none":
        MovefileName = Movie + '.mp4'
        ODBdir = Model+"_ODB"		# ODB Dir name
        Movfile = os.path.join(ODBdir, LoadCase, MovefileName)
        print("Saving the animation movie as "+MovefileName+" in "+ODBdir+"->"+LoadCase+" folder")
        ani.save(Movfile, writer='ffmpeg')

    plt.show()
    return ani


def plot_fiberResponse2D(Model, LoadCase, element, section, LocalAxis = 'y', InputType = 'stress', tstep = -1):
    """
    

    Parameters
    ----------
    Model : string
        The name of the input model database.    
    LoadCase : string
        The name of the input loadcase.    
    element : int
        The input element to be plotted
    section : TYPE
        The section in the input element to be plotted.
    LocalAxis : TYPE, optional
        The local axis to be plotted on the figures x axis. 
        The default is 'y', 'z' is also possible.
    InputType : TYPE, optional
        The quantity to be plotted. The default is 'stress', 'strain' is 
        also possible
    tstep : TYPE, optional
        The time step to be plotted. The program will find the closed time 
        step to the input value. The default is -1.

    """
    
    
    
    # Catch invalid input types
    if InputType not in ['stress', 'strain']:
        raise Exception('Invalid input type. Valid Entries are "stress" and "strain"')
    
    # Catch invalid Direction types
    if LocalAxis not in ['z', 'y']:
        raise Exception('Invalid LocalAxis type. Valid Entries are "z" and "y"')
        

    if InputType == 'stress':
        responseIndex = 3
        axisYlabel = "Fiber Stress"
    if InputType == 'strain':
        responseIndex = 4
        axisYlabel = "Fiber Strain"
    
    if LocalAxis == 'z':
        axisIndex = 1
        axisXlabel = "Local z value"
    if LocalAxis == 'y':
        axisIndex = 0
        axisXlabel = "Local y value"
    
    timeSteps, fiberData  = idbf._readFiberData2D(Model, LoadCase, element, section)
    
    # find the appropriate time step
    if tstep == -1:
        LoadStep = -1
        printLine = "Final deformed shape"
    else:
        LoadStep = (np.abs(timeSteps - tstep)).argmin()			# index closest to the time step requested.
        if timeSteps[-1] < tstep:
            print("XX Warining: Time-Step has exceeded maximum analysis time step XX")
        printLine = 'Fibre '+  InputType + " at time: " + str(round(timeSteps[LoadStep], 2))
            

    fiberYPosition = fiberData[LoadStep,axisIndex::5]
    fiberResponse  = fiberData[LoadStep, responseIndex::5]
    
    # Sort indexes so they appear in an appropraiate location
    sortedIndexes = np.argsort(fiberYPosition)
    fibrePositionSorted = fiberYPosition[sortedIndexes]
    fibreResponseSorted = fiberResponse[sortedIndexes]
    
    
    fig, ax = plt.subplots()
    Xline = ax.plot([fibrePositionSorted[0],fibrePositionSorted[-1]],[0, 0], c ='black', linewidth = 0.5)
    line = ax.plot(fibrePositionSorted, fibreResponseSorted)
    
    xyinput = np.array([fibrePositionSorted,fibreResponseSorted]).T
    ipltf._setStandardViewport(fig, ax, xyinput, 2)
    
    ax.set_ylabel(axisYlabel)  
    ax.set_xlabel(axisXlabel)    
        
    plt.show()
    return fig, ax
    

def animate_fiberResponse2D(Model, LoadCase, element, section,LocalAxis = 'y', InputType = 'stress', skipStart = 0, 
                            skipEnd = 0, rFactor=1, outputFrames=0, fps = 24, Xbound = [], Ybound = []):
    """
    Parameters
    ----------
    Model : string
        The name of the input model database.    
    LoadCase : string
        The name of the input loadcase.    
    element : int
        The input element to be plotted
    section : TYPE
        The section in the input element to be plotted.
    LocalAxis : string, optional
        The local axis to be plotted on the figures x axis. 
        The default is 'y', 'z' is also possible.
    InputType : string, optional
        The quantity 
    skipStart : int, optional
        If specified, this many datapoints will be skipped from the analysis
        data set, before reductions.
        The default is 0, or no reduction
    skipEnd : int, optional
        If specified, this many frames will be skipped at the end of the 
        analysis dataset, before reduction. The default is 0, or no reduction.
    rFactor : int, optional
        If specified, only every "x" frames will be plotted. e.g. x = 2, every 
        other frame is shown.
        The default is 1.
    outputFrames : int, optional
        The number of frames to be included after all other reductions. If the
        reduced number of frames is less than this value, no change is made.
        The default is 0.
    fps : int, optional
        Number of animation frames to be displayed per second. The default is 24.
    Xbound : [xmin, xmax], optional
        The domain of the chart. The default is 1.1 the max and min values.
    Ybound : [ymin, ymax], optional
        The range of the chart. The default is 1.1 the max and min values.

    
    """
    
    # Catch invalid input types
    if InputType not in ['stress', 'strain']:
        raise Exception('Invalid input type. Valid Entries are "stress" and "strain"')
    
    # Catch invalid Direction types
    if LocalAxis not in ['z', 'y']:
        raise Exception('Invalid LocalAxis type. Valid Entries are "z" and "y"')
        

    if InputType == 'stress':
        responseIndex = 3
        axisYlabel = "Fiber Stress"
    if InputType == 'strain':
        responseIndex = 4
        axisYlabel = "Fiber Strain"
    
    if LocalAxis == 'z':
        axisIndex = 1
        axisXlabel = "Local z value"
    if LocalAxis == 'y':
        axisIndex = 0
        axisXlabel = "Local y value"
    
    timeSteps, fiberData  = idbf._readFiberData2D(Model, LoadCase, element, section)
                

    fiberYPosition = fiberData[:,axisIndex::5]
    fiberResponse  = fiberData[:, responseIndex::5]
    
    # Sort indexes so they appear in an appropraiate location
    sortedIndexes = np.argsort(fiberYPosition[0,:])
    fibrePositionSorted = fiberYPosition[:,sortedIndexes]
    fibreResponseSorted = fiberResponse[:,sortedIndexes]    
    
    
    # If end data is not being skipped, use the full vector length.
    if skipEnd ==0:
        skipEnd = len(fiberYPosition)    
    
    # Set up bounds based on data from 
    if Xbound == []:
        xmin = 1.1*np.min(fibrePositionSorted)
        xmax = 1.1*np.max(fibrePositionSorted)
    else:
        xmin = Xbound[0]       
        xmax = Xbound[1]
    
    if Ybound == []:
        ymin = 1.1*np.min(fibreResponseSorted)  
        ymax = 1.1*np.max(fibreResponseSorted)        
    else:
        ymin = Ybound[0]       
        ymax = Ybound[1]          
    
    # Remove unecessary data
    xinputs = fibrePositionSorted[skipStart:skipEnd, :]
    yinputs = fibreResponseSorted[skipStart:skipEnd, :]

    # Reduce the data if the user specifies
    if rFactor != 1:
        xinputs = xinputs[::rFactor, :]
        yinputs = yinputs[::rFactor, :]    
        timeSteps = timeSteps[::rFactor]
    
    # If the Frames isn't specified, use the length of the reduced vector.
    if outputFrames == 0:
        outputFrames = len(xinputs[:, 0])
    else:
        outputFrames = min(outputFrames,len(xinputs[:, 0]))
    
    # Get the final output frames. X doesn't change
    xinputs = xinputs[:outputFrames, :]
    yinputs = yinputs[:outputFrames, :]    
    xinput = xinputs[0,:]
    
    # Initialize the plot
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=.15) # Add extra space bellow graph
    
    line, = ax.plot(xinput, yinputs[0,:])
    Xline = ax.plot([fibrePositionSorted[0,0],fibrePositionSorted[0,-1]], [0, 0], c ='black', linewidth = 0.5)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
        
    ax.set_ylabel(axisYlabel)  
    ax.set_xlabel(axisXlabel)    

    Frames = np.arange(0, outputFrames)
    FrameStart = int(Frames[0])
    FrameEnd = int(Frames[-1])
    
    # Slider Location and size relative to plot
    # [x, y, xsize, ysize]
    axSlider = plt.axes([0.25, .03, 0.50, 0.02])
    plotSlider = Slider(axSlider, 'Time', timeSteps[FrameStart], timeSteps[FrameEnd], valinit=timeSteps[FrameStart])

    # Animation controls
    global is_paused
    is_paused = False # True if user has taken control of the animation   
    
    def on_click(event):
        # Check where the click happened
        (xm,ym),(xM,yM) = plotSlider.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # Toggle on/off based on click
            global is_paused
            if is_paused == True:
                is_paused=False
            elif is_paused == False:
                is_paused=True       
    
    # Define the update function
    def update_line_slider(Time):
        global is_paused
        is_paused=True

        TimeStep = (np.abs(timeSteps - Time)).argmin()
        # Get the current data        
        y = yinputs[TimeStep,:]
        
        # Update the background line
        line.set_data(xinput, y)
        fig.canvas.draw_idle()    
        
        return line,
    
    
    def update_plot(ii):
    
        # If the control is manual, we don't change the plot    
        global is_paused
        if is_paused:
            return line,
       
        # Find the close timeStep and plot that
        # CurrentFrame = int(np.floor(plotSlider.val))

        # Find the close timeStep and plot that
        CurrentTime = plotSlider.val
        CurrentFrame = (np.abs(timeSteps - CurrentTime)).argmin()

        CurrentFrame += 1
        if CurrentFrame >= FrameEnd:
            CurrentFrame = FrameStart
        
        # Update the slider
        plotSlider.set_val(timeSteps[CurrentFrame])        
        
        # Update the slider
        is_paused = False # the above line called update_slider, so we need to reset this
        return line,  
    
    
    plotSlider.on_changed(update_line_slider)
    
    # assign click control
    fig.canvas.mpl_connect('button_press_event', on_click)    
    
    interval = 1000/fps
    
    line_ani = animation.FuncAnimation(fig, update_plot, outputFrames, 
                                       # fargs=(xinput, yinputs, line), 
                                       interval=interval)
									   
    plt.show()
    return line_ani

