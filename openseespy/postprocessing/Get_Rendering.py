
##########################################################################################
## This script records the Nodes and Elements in order to render the OpenSees model.	##
## As of now, this procedure does not work for 9 and 20 node brick elements, and 		##
## tetrahedron elements.																##
## Modeshape plotter works only for 2D and 3D beam-columnelements.						##
##																						##
## Created By - Anurag Upadhyay															##
## Edit 1: Anurag Upadhyay, 12/31/2019, Added shell and solid elements to plot_model 	##
##																						##
## You can download more examples from https://github.com/u-anurag						##
##########################################################################################


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from openseespy.opensees import *

def plot_model():
	
	nodeList = getNodeTags()
	eleList = getEleTags()
	show_node_tags = 'yes'		# Check if you want to display the node numbers     :: 'yes'  or   'no'
	show_element_tags = 'yes'	# Check if you want to display the element numbers  :: 'yes'  or   'no'
	offset = 0.05				# offset for text

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
			if len(Nodes) == 2:
				# 2D Beam-Column Elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				
				x.append(iNode[0])  # list of x coordinates to define plot view area
				y.append(iNode[1])	# list of y coordinates to define plot view area

				plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)
				
				if show_element_tags == 'yes':
					ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])/2, str(element), **ele_text_style) #label elements
			
			if len(Nodes) == 3:
				# 2D Planer three-node shell elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				
				x.append(iNode[0])  # list of x coordinates to define plot view area
				y.append(iNode[1])	# list of y coordinates to define plot view area

				plt.plot((iNode[0], jNode[0], kNode[0]), (iNode[1], jNode[1], kNode[1]),marker='', **ele_style)
				ax.fill([iNode[0], jNode[0], kNode[0]],[iNode[1], jNode[1], kNode[1]],"b", alpha=.6)

				if show_element_tags == 'yes':
					ax.text((iNode[0]+jNode[0]+kNode[0])/4, (iNode[1]+jNode[1]+kNode[1])/4, 
						str(element), **ele_text_style) #label elements
						
			if len(Nodes) == 4:
				# 2D Planer four-node shell elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])
				
				x.append(iNode[0])  # list of x coordinates to define plot view area
				y.append(iNode[1])	# list of y coordinates to define plot view area

				plt.plot((iNode[0], jNode[0], kNode[0], lNode[0]), (iNode[1], jNode[1], kNode[1], lNode[1]),marker='', **ele_style)
				ax.fill([iNode[0], jNode[0], kNode[0], lNode[0]],[iNode[1], jNode[1], kNode[1], lNode[1]],"b", alpha=.6)

				if show_element_tags == 'yes':
					ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0])/4, (iNode[1]+jNode[1]+kNode[1]+lNode[1])/4, 
						str(element), **ele_text_style) #label elements
			
		if show_node_tags == 'yes':
			for node in nodeList:
				x.append(nodeCoord(node)[0])  # list of x coordinates to define plot view area
				y.append(nodeCoord(node)[1])
				ax.text(nodeCoord(node)[0]*1.02, nodeCoord(node)[1]*1.02, str(node),**node_text_style) #label nodes
			
			ax.scatter(x, y, **node_style)
			
		nodeMins = np.array([min(x),min(y)])
		nodeMaxs = np.array([max(x),max(y)])
		
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		view_range = max(max(x)-min(x), max(y)-min(y))
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
			

	if len(nodeCoord(nodeList[0])) == 3:
		print('3D model')
		x = []
		y = []
		z = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1, projection='3d')
		
		def plotCubeSurf(NodeList):
			# Define procedure to plot a 3D solid element
			aNode = NodeList[0]
			bNode = NodeList[1]
			cNode = NodeList[2]
			dNode = NodeList[3]
			plt.plot((aNode[0], bNode[0], cNode[0], dNode[0], aNode[0]), 
						(aNode[1], bNode[1], cNode[1], dNode[1], aNode[1]),
						(aNode[2], bNode[2], cNode[2], dNode[2], aNode[2]), marker='', **ele_style)

			ax.plot_surface(np.array([[aNode[0], dNode[0]], [bNode[0], cNode[0]]]), 
							np.array([[aNode[1], dNode[1]], [bNode[1], cNode[1]]]), 
							np.array([[aNode[2], dNode[2]], [bNode[2], cNode[2]]]), color='g', alpha=.5)
#

		for element in eleList:
			Nodes = eleNodes(element)
			if len(Nodes) == 2:
				# 3D beam-column elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				x.append(iNode[0])  # list of x coordinates to define plot view area
				y.append(iNode[1])	# list of y coordinates to define plot view area
				z.append(iNode[2])	# list of z coordinates to define plot view area
				
				plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),(iNode[2], jNode[2]), marker='', **ele_style)
				
				if show_element_tags == 'yes':
					ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])*1.02/2, 
							(iNode[2]+jNode[2])*1.02/2, str(element), **ele_text_style) #label elements
			
			if len(Nodes) == 4:
				# 3D four-node Quad/shell element
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])
			
				plt.plot((iNode[0], jNode[0], kNode[0], lNode[0], iNode[0]), 
							(iNode[1], jNode[1], kNode[1], lNode[1], iNode[1]),
							(iNode[2], jNode[2], kNode[2], lNode[2], iNode[2]), marker='', **ele_style)
				
				ax.plot_surface(np.array([[iNode[0], lNode[0]], [jNode[0], kNode[0]]]), 
								np.array([[iNode[1], lNode[1]], [jNode[1], kNode[1]]]), 
								np.array([[iNode[2], lNode[2]], [jNode[2], kNode[2]]]), color='g', alpha=.6)
				
				if show_element_tags == 'yes':
					ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0])*1.05/4, (iNode[1]+jNode[1]+kNode[1]+lNode[1])*1.05/4, 
								(iNode[2]+jNode[2]+kNode[2]+lNode[2])*1.05/4, str(element), **ele_text_style) #label elements
			
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
				
				plotCubeSurf([iNode, jNode, kNode, lNode])
				plotCubeSurf([iNode, jNode, jjNode, iiNode])
				plotCubeSurf([iiNode, jjNode, kkNode, llNode])
				plotCubeSurf([lNode, kNode, kkNode, llNode])
				plotCubeSurf([jNode, kNode, kkNode, jjNode])
				plotCubeSurf([iNode, lNode, llNode, iiNode])

				if show_element_tags == 'yes':
					ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0]+iiNode[0]+jjNode[0]+kkNode[0]+llNode[0])/8, 
							(iNode[1]+jNode[1]+kNode[1]+lNode[1]+iiNode[1]+jjNode[1]+kkNode[1]+llNode[1])/8, 
							(iNode[2]+jNode[2]+kNode[2]+lNode[2]+iiNode[2]+jjNode[2]+kkNode[2]+llNode[2])/8, 
							str(element), **ele_text_style) #label elements
			
		if show_node_tags == 'yes':
			for node in nodeList:
				x.append(nodeCoord(node)[0])  # list of x coordinates to define plot view area
				y.append(nodeCoord(node)[1])
				z.append(nodeCoord(node)[2])
				ax.text(nodeCoord(node)[0]*1.02, nodeCoord(node)[1]*1.02, nodeCoord(node)[2]*1.02, str(node),**node_text_style) #label nodes
			
			ax.scatter(x, y, z, **node_style)
			
		
		nodeMins = np.array([min(x),min(y),min(z)])
		nodeMaxs = np.array([max(x),max(y),max(z)])
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		view_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z))
		ax.set_xlim(xViewCenter-(view_range/4), xViewCenter+(view_range/4))
		ax.set_ylim(yViewCenter-(view_range/4), yViewCenter+(view_range/4))
		ax.set_zlim(zViewCenter-(view_range/3), zViewCenter+(view_range/3))
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
	
	plt.axis('on')
	plt.show()

def plot_modeshape(modeNumber):
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
