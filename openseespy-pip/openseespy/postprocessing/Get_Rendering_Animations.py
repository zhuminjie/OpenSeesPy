
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
## 																	##
## You can download more examples from https://github.com/u-anurag						##
##########################################################################################


# Check if the script is executed on Jupyter Notebook Ipython. 
# If yes, force inline, interactive backend for Matplotlib.
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

import os
import openseespy.opensees as ops

import openseespy.postprocessing.internal_database_functions as idbf
import openseespy.postprocessing.internal_plotting_functions as ipltf
from openseespy.postprocessing.Get_Rendering import readODB

### All the plotting related definitions start here.

ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
node_style = {'color':'black', 'marker':'o', 'facecolor':'black'} 
node_text_style = {'fontsize':6, 'fontweight':'regular', 'color':'green'} 
ele_text_style = {'fontsize':6, 'fontweight':'bold', 'color':'darkred'} 

WireEle_style = {'color':'black', 'linewidth':1, 'linestyle':':'} # elements
Eig_style = {'color':'red', 'linewidth':1, 'linestyle':'-'} # elements


# =============================================================================
# Local functions
# =============================================================================

def _initializeFig(nodeCords,ndm):
    
    # set the maximum figure size
    maxFigSize = 8
    
    # Find the node 
    nodeMins = np.min(nodeCords, 0)
    nodeMaxs = np.max(nodeCords, 0)    
    
    # Find the difference between each node.
    nodeDelta = nodeMaxs - nodeMins
    dmax = np.max(nodeDelta[:2])
    
    # Set the figure size
    figsize = (maxFigSize*nodeDelta[0]/dmax , maxFigSize*nodeDelta[1]/dmax)
    
    # Initialize figure
    if ndm == 2:
        fig = plt.figure(figsize = figsize)
        ax = fig.add_subplot(1,1,1)
    elif ndm == 3:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, projection='3d')    
    
    return fig, ax

# =============================================================================
# 
# =============================================================================



def _plotEle_2D(nodes, elements, DispNodeCoordArray, fig, ax, show_element_tags):

    nodeList = nodes[:,0]
    Nnode = len(nodeList)    
    
    # Find the number of surfaces
    Nele = len(elements)
    Nsurf = len([ele for ele in elements if len(ele) >= 4])   
    
    Nsurf = len([ele for ele in elements if len(ele) >= 4])
    figSurfaces = [None]*(Nsurf)
    figLines = [None]*(Nele)
    figTags = [None]*Nele
    
    # xyz label dafault tabale for the current displacement
    xyz_labels = {}
    for jj in range(Nnode):
        xyz_labels[int(nodeList[jj])] = [*DispNodeCoordArray[jj,:]]

    SurfCounter = 0
    for jj, element in enumerate(elements):
        # Get element Nodes
        eletag = int(element[0])     
        tempNodes = element[1:]
        
        if len(tempNodes) == 2:
            # 2D Beam-Column Elements
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
				
            figLines[jj] = plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)
				
            if show_element_tags == 'yes':
               figTags[jj] = ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])/2, str(eletag), **ele_text_style) #label elements
			
        if len(tempNodes) == 3:
            # 2D Planer three-node shell elements
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
            kNode = xyz_labels[tempNodes[2]]
				
            outputs = ipltf._plotTri2D(iNode,jNode,kNode, ax, show_element_tags, eletag, ele_style, fillSurface='yes')
            [figLines[jj], figSurfaces[SurfCounter], figTags[jj]] = [*outputs]
            SurfCounter += 1
            
						
        if len(tempNodes) == 4:
            # 2D Planer four-node shell elements
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
            kNode = xyz_labels[tempNodes[2]]
            lNode = xyz_labels[tempNodes[3]]
				
            outputs = ipltf._plotQuad2D(iNode, jNode, kNode, lNode, ax, show_element_tags, eletag, ele_style, fillSurface='yes')
            [figLines[jj], figSurfaces[SurfCounter], figTags[jj]] = [*outputs]
            SurfCounter += 1
            
    return figLines, figSurfaces, figTags



def _plotEle_3D(nodes, elements, DispNodeCoordArray, fig, ax, show_element_tags):

    nodeList = nodes[:,0]
    Nnode = len(nodeList)

    
    # Find the number of surfaces
    Nele = len(elements)
    Nsurf = len([ele for ele in elements if len(ele) >= 4])   
    
    # For each 8 node surface there are a total of 6 nodes, so we need
    # 5 additional surfaces for each 8Node element.
    Nsurf = len([ele for ele in elements if len(ele) >= 4])
    Nsurf8Node = len([ele for ele in elements if len(ele) == 9])    
    figSurfaces = [None]*(Nsurf + Nsurf8Node*5)
    figLines = [None]*(Nele + Nsurf8Node*5)
    figTags = [None]*Nele
    
    
    # Create a dictionary that makes nodeID to coodinantes
    xyz_labels = {}
    for jj in range(Nnode):
        xyz_labels[int(nodeList[jj])] = [*DispNodeCoordArray[jj,:]]

    # The amount of surfaces and lines is different for each element and needs to be tracked.
    # The amount of tags does not need to be tracked - every element has a tag.
    SurfCounter = 0
    LineCounter = 0

    for jj, element in enumerate(elements):
        
        # Get element Nodes
        tempNodes = element[1:]
        eletag = int(element[0])
        if len(tempNodes) == 2:
            # 3D beam-column elements
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
				
            outputs = ipltf._plotBeam3D(iNode, jNode, ax, show_element_tags, eletag, "solid")

            [figLines[LineCounter], figTags[jj]] = [*outputs]
            LineCounter += 1
            
        if len(tempNodes) == 4:
            # 3D four-node Quad/shell element
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
            kNode = xyz_labels[tempNodes[2]]
            lNode = xyz_labels[tempNodes[3]]
				
            outputs = ipltf._plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, eletag, ele_style, fillSurface='yes')
            [figLines[LineCounter], figSurfaces[SurfCounter], figTags[jj]] = [*outputs]
            
            LineCounter += 1
            SurfCounter += 1
            
        if len(tempNodes) == 8:
            # 3D eight-node Brick element
            # Nodes in CCW on bottom (0-3) and top (4-7) faces resp
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
            kNode = xyz_labels[tempNodes[2]]
            lNode = xyz_labels[tempNodes[3]]
            iiNode = xyz_labels[tempNodes[4]]
            jjNode = xyz_labels[tempNodes[5]]
            kkNode = xyz_labels[tempNodes[6]]
            llNode = xyz_labels[tempNodes[7]]
				
            [tempSurfaces, tempTag] = ipltf._plotCubeVol(iNode, jNode, kNode, lNode, iiNode, jjNode, kkNode, llNode, ax, show_element_tags, eletag, 'solid', fillSurface='yes')
            
            # Store elements and surfaces
            for jj in range(6):
                figSurfaces[SurfCounter] = tempSurfaces[jj]
                SurfCounter += 1
            figTags[jj] = tempTag
            
    return figLines, figSurfaces, figTags



def sample_plot_model(ModelName = '', LoadCaseName = '', Scale = 1, 
                      show_element_tags = 'no', show_node_tags = 'no',
                      Plot_Displacements = 'no'):
  
    # try to read a model the nodes and elements
    try :
        nodes, elements = idbf.getNodesandElements()
        Input = True
    except:
        print("No model active.") 

    # try to get the nodes and elements from the database
    try :
        nodes, elements = idbf._readNodesandElements(ModelName)
        Input = True
    except:
        print("No database found.")
    
    if not Input:
        raise Exception('No input model was specified')    
    
    
    # Process Node information, Calulate number of degrees of freedom
    nodeList = nodes[:,0]    
    Nnodes = len(nodeList)
    nodeCoordArray = nodes[:,1:]
    ndm = len(nodes[0,1:])   

    # Get displacements
    if Plot_Displacements == 'yes':
        # Get Node coordinants
        OBD = readODB(ModelName, LoadCaseName)
        
        DispNodeArray = OBD[2]*Scale
        
    # Otherwise we use zero as our displacement
    else:
        DispNodeArray = np.zeros([Nnodes,ndm])
    
    DispNodeCoordArray = nodes[:,1:] + DispNodeArray

    
    Nele = len(elements)
    figNodeTags = [None]*Nele
    NodeText = [None]*Nnodes
    
    # Initialize figure
    fig, ax = _initializeFig(DispNodeCoordArray, ndm)
    
    # Check if the model is 2D or 3D
    if ndm == 2:
        
        # Plot elements
        OutputObjects = _plotEle_2D(nodes, elements, DispNodeCoordArray, fig, ax, show_element_tags)

        if show_node_tags == 'yes':
            for j in range(Nnodes):
                NodeText[j] = ax.text(*nodes[j,1:]*1.02, str(int(nodes[j,0])), **node_text_style) #label nodes
			
        nodeObjects = ax.scatter(nodeCoordArray[:,0], nodeCoordArray[:,1], **node_style)

        #ResizePlot(fig, ax, ndm)
        nodeMins = np.array([min(nodeCoordArray[:,0]), min(nodeCoordArray[:,1])])
        nodeMaxs = np.array([max(nodeCoordArray[:,0]), max(nodeCoordArray[:,1])])
		
        xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
        yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
        view_range = max(max(nodeCoordArray[:,0])-min(nodeCoordArray[:,0]), max(nodeCoordArray[:,1])-min(nodeCoordArray[:,1]))
		
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
			

    if ndm == 3:
        

        print('3D model')
		
        # Plot Model and make Objects
        OutputObjects = _plotEle_3D(nodes, elements, DispNodeCoordArray, fig, ax, show_element_tags)

        if show_node_tags == 'yes':
            for jj in range(Nnodes):
                NodeText[jj] = ax.text(*nodes[jj,1:]*1.02, str(int(nodes[jj,0])), **node_text_style) #label nodes
				
        nodeObjects = ax.scatter(nodeCoordArray[:,0], nodeCoordArray[:,1], nodeCoordArray[:,2], **node_style)								#show nodes
		
        nodeMins = np.array([min(nodeCoordArray[:,0]),min(nodeCoordArray[:,1]),min(nodeCoordArray[:,2])])
        nodeMaxs = np.array([max(nodeCoordArray[:,0]),max(nodeCoordArray[:,1]),max(nodeCoordArray[:,2])])
		
        xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
        yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
        zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
		
        view_range = max(max(nodeCoordArray[:,0])-min(nodeCoordArray[:,0]), max(nodeCoordArray[:,1])-min(nodeCoordArray[:,1]), max(nodeCoordArray[:,2])-min(nodeCoordArray[:,2]))

        ax.set_xlim(xViewCenter-(view_range/4), xViewCenter+(view_range/4))
        ax.set_ylim(yViewCenter-(view_range/4), yViewCenter+(view_range/4))
        ax.set_zlim(zViewCenter-(view_range/3), zViewCenter+(view_range/3))
		
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
	
    plt.axis('on')
    plt.show()
    
    OutputObjects = [nodeObjects, NodeText, *OutputObjects]
    
    return OutputObjects
	

