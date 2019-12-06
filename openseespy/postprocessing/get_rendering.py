
##########################################################################################
## This script records the Nodes and Elements in order to render the OpenSees model.	##
## As of now, this procedure does not work for 2D/3D shell and solid elements.			##
##																						##
## Created By - Anurag Upadhyay															##
##																						##
## You can download more examples from https://github.com/u-anurag						##
##########################################################################################

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from openseespy.opensees import *

def plot_model():
	import matplotlib.pyplot as plt
	
	nodeList = getNodeTags()
	eleList = getEleTags()
	show_node_tags = 'yes'		# Check if you want to display the node numbers     :: 'yes'  or   'no'
	show_element_tags = 'yes'	# Check if you want to display the element numbers  :: 'yes'  or   'no'
	offset = 0.05				#offset for text

	ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
	node_style = {'color':'black', 'marker':'o', 'facecolor':'black'} 
	node_text_style = {'fontsize':6, 'fontweight':'regular', 'color':'green'} 
	ele_text_style = {'fontsize':6, 'fontweight':'bold', 'color':'darkred'} 

	# Check if the model is 2D or 3D
	if len(nodeCoord(nodeList[0])) == 2:
		print('2D model')
		x = []
		y = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		for element in eleList:
			Nodes = eleNodes(element)
			iNode = nodeCoord(Nodes[0])
			jNode = nodeCoord(Nodes[1])
			
			x.append(iNode[0])  # list of x coordinates to define plot view area
			y.append(iNode[1])	# list of y coordinates to define plot view area

			plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)

			if show_node_tags == 'yes':
				ax.scatter(iNode[0], iNode[1], **node_style)
				ax.text(iNode[0], iNode[1], str(Nodes[0]), **node_text_style ) #label nodes
				if element == eleList[-1]:
					ax.scatter(jNode[0], jNode[1], **node_style)
					ax.text(jNode[0], jNode[1], str(Nodes[0]),  **node_text_style) #label nodes

			if show_element_tags == 'yes':
				ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])/2, str(element), **ele_text_style) #label elements
			
		nodeMins = np.array([min(x),min(y)])
		nodeMaxs = np.array([max(x),max(y)])
		
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		view_range = max(max(x)-min(x), max(y)-min(y))
			

	if len(nodeCoord(nodeList[0])) == 3:
		print('3D model')
		x = []
		y = []
		z = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1, projection='3d')
		for element in eleList:
			Nodes = eleNodes(element)
			iNode = nodeCoord(Nodes[0])
			jNode = nodeCoord(Nodes[1])
			x.append(iNode[0])  # list of x coordinates to define plot view area
			y.append(iNode[1])	# list of y coordinates to define plot view area
			z.append(iNode[2])	# list of z coordinates to define plot view area
			
			plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),(iNode[2], jNode[2]), marker='', **ele_style)
			
			if show_node_tags == 'yes':
				ax.scatter(iNode[0], iNode[1], iNode[2],  **node_style)
				ax.text(iNode[0]*1.05, iNode[1]*1.05, iNode[2]*1.01, str(Nodes[0]),**node_text_style) #label nodes
				if element == eleList[-1]:
					ax.scatter(jNode[0], jNode[1], jNode[2], **node_style)
					ax.text(jNode[0]*1.0, jNode[1]*1.0, jNode[2]*1.0, str(Nodes[0]), **node_text_style) #label nodes
			
			if show_element_tags == 'yes':
				ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])*1.02/2, 
							(iNode[2]+jNode[2])*1.02/2, str(element), **ele_text_style) #label elements
			
		nodeMins = np.array([min(x),min(y),min(z)])
		nodeMaxs = np.array([max(x),max(y),max(z)])
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		view_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z))
		ax.set_xlim(xViewCenter-(view_range/4), xViewCenter+(view_range/4))
		ax.set_ylim(yViewCenter-(view_range/4), yViewCenter+(view_range/4))
		ax.set_zlim(zViewCenter-(view_range/3), zViewCenter+(view_range/3))
	
	plt.axis('off')
	plt.show()

def plot_modeshape(modeNumber):
	import matplotlib.pyplot as plt
	
	# Plot original shape
	# overlap with mode shape with the mode number asked for
	
	nodeList = getNodeTags()
	eleList = getEleTags()
	scale = 200				#offset for text

	ele_style = {'color':'black', 'linewidth':1, 'linestyle':':'} # elements
	Eig_style = {'color':'red', 'linewidth':1, 'linestyle':'-'} # elements
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
			iNode = nodeCoord(Nodes[0])
			jNode = nodeCoord(Nodes[1])
			iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
			jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
			x.append(iNode[0])  # list of x coordinates to define plot view area
			y.append(iNode[1])	# list of y coordinates to define plot view area

			plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)
			plt.plot((iNode[0]+ scale*iNode_Eig[0], jNode[0]+ scale*jNode_Eig[0]), 
						(iNode[1]+ scale*iNode_Eig[1], jNode[1]+ scale*jNode_Eig[1]),marker='', **Eig_style)

		nodeMins = np.array([min(x),min(y)])
		nodeMaxs = np.array([max(x),max(y)])
		
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		view_range = max(max(x)-min(x), max(y)-min(y))
			
	if len(nodeCoord(nodeList[0])) == 3:
		print('3D model')
		x = []
		y = []
		z = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1, projection='3d')
		for element in eleList:
			Nodes = eleNodes(element)
			iNode = nodeCoord(Nodes[0])
			jNode = nodeCoord(Nodes[1])
			iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
			jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
			
			x.append(iNode[0])  # list of x coordinates to define plot view area
			y.append(iNode[1])	# list of y coordinates to define plot view area
			z.append(iNode[2])	# list of z coordinates to define plot view area
			
			plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),(iNode[2], jNode[2]), marker='', **ele_style)
			plt.plot((iNode[0]+ scale*iNode_Eig[0], jNode[0]+ scale*jNode_Eig[0]), 
						(iNode[1]+ scale*iNode_Eig[1], jNode[1]+ scale*jNode_Eig[1]), 
						(iNode[2]+ scale*iNode_Eig[2], jNode[2]+ scale*jNode_Eig[2]),
							marker='', **Eig_style)

		nodeMins = np.array([min(x),min(y),min(z)])
		nodeMaxs = np.array([max(x),max(y),max(z)])
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		view_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z))
		ax.set_xlim(xViewCenter-(view_range/4), xViewCenter+(view_range/4))
		ax.set_ylim(yViewCenter-(view_range/4), yViewCenter+(view_range/4))
		ax.set_zlim(zViewCenter-(view_range/3), zViewCenter+(view_range/3))
			
			
	plt.axis('off')
	plt.show()
