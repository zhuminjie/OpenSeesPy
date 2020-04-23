
##########################################################################################
## This script records the Nodes and Elements in order to render the OpenSees model.	##
## As of now, this procedure does not work for 9 and 20 node brick elements, and 		##
## tetrahedron elements.																##
##																						##
##																						##
## Created By - Anurag Upadhyay															##
## Edit 1: Anurag Upadhyay, 12/31/2019, Added shell and solid elements to plot_model	##
## Edit 2: Anurag Upadhyay, 03/21/2020, Added check for Jupyter Notebook; mode shape..	##
## plotter for 2D and 3D shell, and brick elements; User specified scale factor to ...	##
## plot mode shapes; display mode period on the plot.									##
##																						##
## You can download more examples from https://github.com/u-anurag						##
##########################################################################################

# Check if the script is executed on Jupyter Notebook Ipython. If yes, force inline, interactive ...
# ... backend for Matplotlib.
import sys
import matplotlib

for line in range(0,len(sys.argv)):
    if "ipykernel_launcher.py" in sys.argv[line]:
        matplotlib.use('nbagg')
        break
    else:
        pass

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from math import asin, sqrt

from openseespy.opensees import *

def plot_model(*argv):
	#Options to display node and element tags, THe following procedure is to keep the backward compatibility.
	if len(argv)== 1:
		if argv[0]=="nodes" or argv[0]=="Nodes" or argv[0]=="node" or argv[0]=="Node":
			show_node_tags = 'yes'
			show_element_tags = 'no'
		
		elif argv[0]=="elements" or argv[0]=="Elements" or argv[0]=="element" or argv[0]=="Element":
			show_node_tags = 'no'
			show_element_tags = 'yes'
		
		else:
			print("Incorrect arguments; correct arguments are plot_model(nodes,elements)")
			print("Setting show node tags and element tags as default")
			show_node_tags = 'yes'
			show_element_tags = 'yes'
		
	elif len(argv)== 2:
		if "nodes" or "Nodes" in argv:
			show_node_tags = 'yes'
		else:
			pass
			
		if "elements" or "Elements" in argv:
			show_element_tags = 'yes'
		else:
			pass
	
	else:
		print("Setting show node tags and element tags as default")
		show_node_tags = 'yes'
		show_element_tags = 'yes'
	
	nodeList = getNodeTags()
	eleList = getEleTags()
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

def plot_modeshape(*argv):
	# Expected input argv : modeNumber, scale

	modeNumber = argv[0]
	if len(argv) < 2:
		print("No scale factor specified to plot modeshape, using default 200.")
		print("Input arguments are plot_modeshape(modeNumber, scaleFactor)")
		scale = 200
	else:
		scale = argv[1]
	
	# Run eigen analysis and get information to print
	wipeAnalysis()
	eigenVal = eigen(modeNumber+1)
	Tn=4*asin(1.0)/(eigenVal[modeNumber-1])**0.5
	
	nodeList = getNodeTags()
	eleList = getEleTags()
	# scale = 200				#offset for text

	ele_style = {'color':'black', 'linewidth':1, 'linestyle':':'} # elements
	Eig_style = {'color':'red', 'linewidth':1, 'linestyle':'-'} # elements
	node_style = {'color':'black', 'marker':'.', 'linestyle':''} 

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
				iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
				jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
				
				# Get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Eig[0], iNode[1]+ scale*iNode_Eig[1]]
				jNode_final = [jNode[0]+ scale*jNode_Eig[0], jNode[1]+ scale*jNode_Eig[1]]
				
				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area

				plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)
				plt.plot((iNode_final[0], jNode_final[0]), 
							(iNode_final[1], jNode_final[1]),marker='', **Eig_style)

			if len(Nodes) == 3:
				# 2D Planer three-node shell elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
				jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
				kNode_Eig = nodeEigenvector(Nodes[2], modeNumber)

				# Get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Eig[0], iNode[1]+ scale*iNode_Eig[1]]
				jNode_final = [jNode[0]+ scale*jNode_Eig[0], jNode[1]+ scale*jNode_Eig[1]]
				kNode_final = [kNode[0]+ scale*kNode_Eig[0], kNode[1]+ scale*kNode_Eig[1]]
				
				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area

				plt.plot((iNode[0], jNode[0], kNode[0]), (iNode[1], jNode[1], kNode[1]),marker='', **ele_style)

				plt.plot((iNode_final[0], jNode_final[0], kNode_final[0]), (iNode_final[1], jNode_final[1], kNode_final[1]),marker='', **Eig_style)
				ax.fill([iNode_final[0], jNode_final[0], kNode_final[0]],[iNode_final[1], jNode_final[1], kNode_final[1]],"b", alpha=.6)

						
			if len(Nodes) == 4:
				# 2D Planer four-node shell elements
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])
				iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
				jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
				kNode_Eig = nodeEigenvector(Nodes[2], modeNumber)
				lNode_Eig = nodeEigenvector(Nodes[3], modeNumber)
				
				# Get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Eig[0], iNode[1]+ scale*iNode_Eig[1]]
				jNode_final = [jNode[0]+ scale*jNode_Eig[0], jNode[1]+ scale*jNode_Eig[1]]
				kNode_final = [kNode[0]+ scale*kNode_Eig[0], kNode[1]+ scale*kNode_Eig[1]]
				lNode_final = [lNode[0]+ scale*lNode_Eig[0], lNode[1]+ scale*lNode_Eig[1]]
				
				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area

				plt.plot((iNode[0], jNode[0], kNode[0], lNode[0]), (iNode[1], jNode[1], kNode[1], lNode[1]),marker='', **ele_style)
				plt.plot((iNode_final[0], jNode_final[0], kNode_final[0], lNode_final[0]), (iNode_final[1], jNode_final[1], kNode_final[1], lNode_final[1]),marker='', **Eig_style)
				ax.fill([iNode_final[0], jNode_final[0], kNode_final[0], lNode_final[0]],[iNode_final[1], jNode_final[1], kNode_final[1], lNode_final[1]],"b", alpha=.6)
	
				
		nodeMins = np.array([min(x),min(y)])
		nodeMaxs = np.array([max(x),max(y)])
		
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		view_range = max(max(x)-min(x), max(y)-min(y))
		ax.set_xlim(xViewCenter-(1.1*view_range/1), xViewCenter+(1.1*view_range/1))
		ax.set_ylim(yViewCenter-(1.1*view_range/1), yViewCenter+(1.1*view_range/1))
		ax.text(0.05, 0.95, "Mode "+str(modeNumber), transform=ax.transAxes)
		ax.text(0.05, 0.90, "T = "+str("%.3f" % Tn)+" s", transform=ax.transAxes)
			
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
				iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
				jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
				
				# Add original and mode shape to get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Eig[0], iNode[1]+ scale*iNode_Eig[1], iNode[2]+ scale*iNode_Eig[2]]
				jNode_final = [jNode[0]+ scale*jNode_Eig[0], jNode[1]+ scale*jNode_Eig[1], jNode[2]+ scale*jNode_Eig[2]]
				
				x.append(iNode_final[0])  # list of x coordinates to define plot view area
				y.append(iNode_final[1])	# list of y coordinates to define plot view area
				z.append(iNode_final[2])	# list of z coordinates to define plot view area
				
				plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),(iNode[2], jNode[2]), marker='', **ele_style)
				plt.plot((iNode_final[0], jNode_final[0]), (iNode_final[1], jNode_final[1]),(iNode_final[2], jNode_final[2]), 
					marker='', **Eig_style)

				# plt.plot((iNode[0]+ scale*iNode_Eig[0], jNode[0]+ scale*jNode_Eig[0]), 
							# (iNode[1]+ scale*iNode_Eig[1], jNode[1]+ scale*jNode_Eig[1]), 
							# (iNode[2]+ scale*iNode_Eig[2], jNode[2]+ scale*jNode_Eig[2]),
								# marker='', **Eig_style)

			if len(Nodes) == 4:
				# 3D four-node Quad/shell element
				iNode = nodeCoord(Nodes[0])
				jNode = nodeCoord(Nodes[1])
				kNode = nodeCoord(Nodes[2])
				lNode = nodeCoord(Nodes[3])
				iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
				jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
				kNode_Eig = nodeEigenvector(Nodes[2], modeNumber)
				lNode_Eig = nodeEigenvector(Nodes[3], modeNumber)
				
				# Add original and mode shape to get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Eig[0], iNode[1]+ scale*iNode_Eig[1], iNode[2]+ scale*iNode_Eig[2]]
				jNode_final = [jNode[0]+ scale*jNode_Eig[0], jNode[1]+ scale*jNode_Eig[1], jNode[2]+ scale*jNode_Eig[2]]
				kNode_final = [kNode[0]+ scale*kNode_Eig[0], kNode[1]+ scale*kNode_Eig[1], kNode[2]+ scale*kNode_Eig[2]]
				lNode_final = [lNode[0]+ scale*lNode_Eig[0], lNode[1]+ scale*lNode_Eig[1], lNode[2]+ scale*lNode_Eig[2]]
				
				
				plt.plot((iNode[0], jNode[0], kNode[0], lNode[0], iNode[0]), 
							(iNode[1], jNode[1], kNode[1], lNode[1], iNode[1]),
							(iNode[2], jNode[2], kNode[2], lNode[2], iNode[2]), marker='', **ele_style)
				
				plt.plot((iNode_final[0], jNode_final[0], kNode_final[0], lNode_final[0], iNode_final[0]), 
							(iNode_final[1], jNode_final[1], kNode_final[1], lNode_final[1], iNode_final[1]),
							(iNode_final[2], jNode_final[2], kNode_final[2], lNode_final[2], iNode_final[2]), 
								marker='', **Eig_style)
				# Plot surfaces on the mode shape
				ax.plot_surface(np.array([[iNode_final[0], lNode_final[0]], [jNode_final[0], kNode_final[0]]]), 
								np.array([[iNode_final[1], lNode_final[1]], [jNode_final[1], kNode_final[1]]]), 
								np.array([[iNode_final[2], lNode_final[2]], [jNode_final[2], kNode_final[2]]]), 
									color='g', alpha=.6)
						
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
				
				iNode_Eig = nodeEigenvector(Nodes[0], modeNumber)
				jNode_Eig = nodeEigenvector(Nodes[1], modeNumber)
				kNode_Eig = nodeEigenvector(Nodes[2], modeNumber)
				lNode_Eig = nodeEigenvector(Nodes[3], modeNumber)
				iiNode_Eig = nodeEigenvector(Nodes[4], modeNumber)
				jjNode_Eig = nodeEigenvector(Nodes[5], modeNumber)
				kkNode_Eig = nodeEigenvector(Nodes[6], modeNumber)
				llNode_Eig = nodeEigenvector(Nodes[7], modeNumber)
				
				# Add original and mode shape to get final node coordinates
				iNode_final = [iNode[0]+ scale*iNode_Eig[0], iNode[1]+ scale*iNode_Eig[1], iNode[2]+ scale*iNode_Eig[2]]
				jNode_final = [jNode[0]+ scale*jNode_Eig[0], jNode[1]+ scale*jNode_Eig[1], jNode[2]+ scale*jNode_Eig[2]]
				kNode_final = [kNode[0]+ scale*kNode_Eig[0], kNode[1]+ scale*kNode_Eig[1], kNode[2]+ scale*kNode_Eig[2]]
				lNode_final = [lNode[0]+ scale*lNode_Eig[0], lNode[1]+ scale*lNode_Eig[1], lNode[2]+ scale*lNode_Eig[2]]
				iiNode_final = [iiNode[0]+ scale*iiNode_Eig[0], iiNode[1]+ scale*iiNode_Eig[1], iiNode[2]+ scale*iiNode_Eig[2]]
				jjNode_final = [jjNode[0]+ scale*jjNode_Eig[0], jjNode[1]+ scale*jjNode_Eig[1], jjNode[2]+ scale*jjNode_Eig[2]]
				kkNode_final = [kkNode[0]+ scale*kkNode_Eig[0], kkNode[1]+ scale*kkNode_Eig[1], kkNode[2]+ scale*kkNode_Eig[2]]
				llNode_final = [llNode[0]+ scale*llNode_Eig[0], llNode[1]+ scale*llNode_Eig[1], llNode[2]+ scale*llNode_Eig[2]]
				
				plotCubeSurf([iNode_final, jNode_final, kNode_final, lNode_final])
				plotCubeSurf([iNode_final, jNode_final, jjNode_final, iiNode_final])
				plotCubeSurf([iiNode_final, jjNode_final, kkNode_final, llNode_final])
				plotCubeSurf([lNode_final, kNode_final, kkNode_final, llNode_final])
				plotCubeSurf([jNode_final, kNode_final, kkNode_final, jjNode_final])
				plotCubeSurf([iNode_final, lNode_final, llNode_final, iiNode_final])

		nodeMins = np.array([min(x),min(y),min(z)])
		nodeMaxs = np.array([max(x),max(y),max(z)])
		xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
		yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
		zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		view_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z))
		ax.set_xlim(xViewCenter-(view_range/4), xViewCenter+(view_range/4))
		ax.set_ylim(yViewCenter-(view_range/4), yViewCenter+(view_range/4))
		ax.set_zlim(zViewCenter-(view_range/3), zViewCenter+(view_range/3))
		ax.text2D(0.10, 0.95, "Mode "+str(modeNumber), transform=ax.transAxes)
		ax.text2D(0.10, 0.90, "T = "+str("%.3f" % Tn)+" s", transform=ax.transAxes)
			
	plt.axis('off')
	plt.show()

	wipeAnalysis()


def recordNodeDisp(filename = 'nodeDisp.txt'):
	# This function is meant to be run before an analysis and saves the displacements of all nodes into filename. 
	# It can be used later in the plot_deformedshape function.
	nodeList = getNodeTags()
	if len(nodeCoord(nodeList[0])) == 2:
		dofList = [1, 2]
	if len(nodeCoord(nodeList[0])) == 3:
		dofList = [1, 2, 3]
	# recorder('Node', '-file', filename, '–time', '–node', *nodeList, '-dof', *dofList, 'disp')
	recorder('Node', '-file', filename, '-time', '-closeOnWrite', '–node', *nodeList, '-dof', *dofList, 'disp')

def plot_deformedshape(filename = 'nodeDisp.txt', tstep = -1, scale = 200):
	# Expected input argv : filename contains the displacements of all nodes in the same order they are returned by getNodeTags().
	# First column in filename is time. 
	# tstep is the number of the step of the analysis to be ploted (starting from 1), 
	# and scale is the scale factor for the deformed shape.

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

				plt.plot((iNode[0], jNode[0], kNode[0]), (iNode[1], jNode[1], kNode[1]),marker='', **ele_style)

				plt.plot((iNode_final[0], jNode_final[0], kNode_final[0]), (iNode_final[1], jNode_final[1], kNode_final[1]),marker='', **Disp_style)
				ax.fill([iNode_final[0], jNode_final[0], kNode_final[0]],[iNode_final[1], jNode_final[1], kNode_final[1]],"b", alpha=.6)

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

				plt.plot((iNode[0], jNode[0], kNode[0], lNode[0]), (iNode[1], jNode[1], kNode[1], lNode[1]),marker='', **ele_style)
				plt.plot((iNode_final[0], jNode_final[0], kNode_final[0], lNode_final[0]), (iNode_final[1], jNode_final[1], kNode_final[1], lNode_final[1]),marker='', **Disp_style)
				ax.fill([iNode_final[0], jNode_final[0], kNode_final[0], lNode_final[0]],[iNode_final[1], jNode_final[1], kNode_final[1], lNode_final[1]],"b", alpha=.6)

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

				plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),(iNode[2], jNode[2]), marker='', **ele_style)
				plt.plot((iNode_final[0], jNode_final[0]), (iNode_final[1], jNode_final[1]),(iNode_final[2], jNode_final[2]), 
					marker='', **Disp_style)

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

				plt.plot((iNode[0], jNode[0], kNode[0], lNode[0], iNode[0]), 
							(iNode[1], jNode[1], kNode[1], lNode[1], iNode[1]),
							(iNode[2], jNode[2], kNode[2], lNode[2], iNode[2]), marker='', **ele_style)
  
				plt.plot((iNode_final[0], jNode_final[0], kNode_final[0], lNode_final[0], iNode_final[0]), 
							(iNode_final[1], jNode_final[1], kNode_final[1], lNode_final[1], iNode_final[1]),
							(iNode_final[2], jNode_final[2], kNode_final[2], lNode_final[2], iNode_final[2]), 
								marker='', **Disp_style)
				# Plot surfaces on the mode shape
				ax.plot_surface(np.array([[iNode_final[0], lNode_final[0]], [jNode_final[0], kNode_final[0]]]), 
								np.array([[iNode_final[1], lNode_final[1]], [jNode_final[1], kNode_final[1]]]), 
								np.array([[iNode_final[2], lNode_final[2]], [jNode_final[2], kNode_final[2]]]), 
									color='g', alpha=.6)

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

				plotCubeSurf([iNode_final, jNode_final, kNode_final, lNode_final])
				plotCubeSurf([iNode_final, jNode_final, jjNode_final, iiNode_final])
				plotCubeSurf([iiNode_final, jjNode_final, kkNode_final, llNode_final])
				plotCubeSurf([lNode_final, kNode_final, kkNode_final, llNode_final])
				plotCubeSurf([jNode_final, kNode_final, kkNode_final, jjNode_final])
				plotCubeSurf([iNode_final, lNode_final, llNode_final, iiNode_final])

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
