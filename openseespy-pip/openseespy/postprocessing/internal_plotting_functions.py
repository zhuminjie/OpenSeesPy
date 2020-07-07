

########################################################################
##																	  ##
## Internal plotting functions called by the user plotting functions  ##

########################################################################


import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
node_style = {'color':'black', 'marker':'o', 'facecolor':'black','linewidth':0.} 
node_text_style = {'fontsize':6, 'fontweight':'regular', 'color':'green'} 
ele_text_style = {'fontsize':6, 'fontweight':'bold', 'color':'darkred'} 

WireEle_style = {'color':'black', 'linewidth':1, 'linestyle':':'} # elements
Eig_style = {'color':'red', 'linewidth':1, 'linestyle':'-'} # elements


def _plotCubeSurf(nodeCords, ax, fillSurface, eleStyle):
	## This procedure is called by the plotCubeVol() command
	aNode = nodeCords[0]
	bNode = nodeCords[1]
	cNode = nodeCords[2]
	dNode = nodeCords[3]
    			
	## Use arrays for less memory and fast code
	surfXarray = np.array([[aNode[0], dNode[0]], [bNode[0], cNode[0]]])
	surfYarray = np.array([[aNode[1], dNode[1]], [bNode[1], cNode[1]]])
	surfZarray = np.array([[aNode[2], dNode[2]], [bNode[2], cNode[2]]])
	
	## Initialize varables for matplotlib objects
	tempSurface = [None]

	if fillSurface == 'yes':
		tempSurface = ax.plot_surface(surfXarray, surfYarray, surfZarray, edgecolor='k', color='g', alpha=.5)
    			
	del aNode, bNode, cNode, dNode, surfXarray, surfYarray, surfZarray
    
	return tempSurface


def _plotCubeVol(iNode, jNode, kNode, lNode, iiNode, jjNode, kkNode, llNode, ax, show_element_tags, element, eleStyle, fillSurface):
	## procedure to render a cubic element, use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
	## USe fillSurface = "yes" for color fill in the elements. fillSurface="no" for wireframe.
	
	tempSurfaces = 6*[None]
	tempTag = [None]

	# 2D Planer four-node shell elements
	# [iNode, jNode, kNode, lNode,iiNode, jjNode, kkNode, llNode]  = [*nodesCords]
  
	tempSurfaces[0] = _plotCubeSurf([iNode, jNode, kNode, lNode], ax, fillSurface, eleStyle)
	tempSurfaces[1] = _plotCubeSurf([iNode, jNode, jjNode, iiNode], ax, fillSurface, eleStyle)
	tempSurfaces[2] = _plotCubeSurf([iiNode, jjNode, kkNode, llNode], ax, fillSurface, eleStyle)
	tempSurfaces[3] = _plotCubeSurf([lNode, kNode, kkNode, llNode], ax, fillSurface, eleStyle)
	tempSurfaces[4] = _plotCubeSurf([jNode, kNode, kkNode, jjNode], ax, fillSurface, eleStyle)
	tempSurfaces[5] = _plotCubeSurf([iNode, lNode, llNode, iiNode], ax, fillSurface, eleStyle)
    
	if show_element_tags == 'yes':
		tempTag = ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0]+iiNode[0]+jjNode[0]+kkNode[0]+llNode[0])/8, 
							(iNode[1]+jNode[1]+kNode[1]+lNode[1]+iiNode[1]+jjNode[1]+kkNode[1]+llNode[1])/8, 
							(iNode[2]+jNode[2]+kNode[2]+lNode[2]+iiNode[2]+jjNode[2]+kkNode[2]+llNode[2])/8, 
							str(element), **ele_text_style) #label elements
        
	return tempSurfaces, tempTag


def _plotTri2D(iNode, jNode, kNode, ax, show_element_tags, element, eleStyle, fillSurface):
	## procedure to render a 2D three node shell element. use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
	## USe fillSurface = "yes" for color fill in the elements. fillSurface="no" for wireframe.
							
    ## Initialize varables for matplotlib objects
	tempLines = [None]
	tempSurface = [None]
	tempTag = [None]
    
	tempLines, = plt.plot((iNode[0], jNode[0], kNode[0], iNode[0]), 
                         (iNode[1], jNode[1], kNode[1], iNode[1]), marker='')
    
	# update style
	if eleStyle == "wire":
		plt.setp(tempLines,**WireEle_style)
	else:
		plt.setp(tempLines,**ele_style)
    
	if fillSurface == 'yes':
		tempSurface = ax.fill(np.array([iNode[0], jNode[0], kNode[0]]), 
								np.array([iNode[1], jNode[1], kNode[1]]), color='g', alpha=.6)
        
	if show_element_tags == 'yes':
		tempTag = ax.text((iNode[0] + jNode[0] + kNode[0])*1.0/3, (iNode[1]+jNode[1]+kNode[1])*1.0/3, 
							str(element), **ele_text_style) #label elements
	return tempLines, tempSurface, tempTag


def _plotQuad2D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, eleStyle, fillSurface):
	## procedure to render a 2D four node shell element. use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
	## USe fillSurface = "yes" for color fill in the elements. fillSurface="no" for wireframe.
    tempLines = [None]
    tempSurface = [None]
    tempTag = [None]

    tempLines, = plt.plot((iNode[0], jNode[0], kNode[0], lNode[0], iNode[0]), 
               (iNode[1], jNode[1], kNode[1], lNode[1], iNode[1]), marker='')
    
    # update style
    if eleStyle == "wire":
        plt.setp(tempLines,**WireEle_style)
    else:
        plt.setp(tempLines, **ele_style)

    if fillSurface == 'yes':
        tempSurface = ax.fill(np.array([iNode[0], jNode[0], kNode[0], lNode[0]]), 
                               np.array([iNode[1], jNode[1], kNode[1], lNode[1]]), color='g', alpha=.6)
    
    tempTag = []
    if show_element_tags == 'yes':
        tempTag = ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0])*1.0/4, (iNode[1]+jNode[1]+kNode[1]+lNode[1])*1.0/4, 
                          str(element), **ele_text_style) #label elements
    return tempLines, tempSurface, tempTag


def _plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, eleStyle, fillSurface):
	## procedure to render a 3D four node shell element. use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
	## USe fillSurface = "yes" for color fill in the elements. fillSurface="no" for wireframe.
	
    tempLines = [None]
    tempSurface = [None]
    tempTag = [None]
    
    # Create Lines
    tempLines, = plt.plot((iNode[0], jNode[0], kNode[0], lNode[0], iNode[0]), 
                         (iNode[1], jNode[1], kNode[1], lNode[1], iNode[1]),
                         (iNode[2], jNode[2], kNode[2], lNode[2], iNode[2]), marker='')

    # update style
    if eleStyle == "wire":
        plt.setp(tempLines,**WireEle_style)
    else:
        plt.setp(tempLines,**ele_style)
	
    # Get Surface
    if fillSurface == 'yes':
        tempSurface = ax.plot_surface(np.array([[iNode[0], lNode[0]], [jNode[0], kNode[0]]]), 
                                       np.array([[iNode[1], lNode[1]], [jNode[1], kNode[1]]]), 
                                       np.array([[iNode[2], lNode[2]], [jNode[2], kNode[2]]]), color='g', alpha=.6)
    tempTag = []
    # Get Tag
    if show_element_tags == 'yes':
        tempTag = ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0])*1.05/4, (iNode[1]+jNode[1]+kNode[1]+lNode[1])*1.05/4, 
                          (iNode[2]+jNode[2]+kNode[2]+lNode[2])*1.05/4, str(element), **ele_text_style) #label elements

    return tempLines, tempSurface, tempTag


def _plotBeam2D(iNode, jNode, ax, show_element_tags, element, eleStyle):
    ##procedure to render a 2D two-node element. use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
    tempLines, = plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]), marker='')
    
    if eleStyle == "wire":
        plt.setp(tempLines,**WireEle_style)
    else:
        plt.setp(tempLines,**ele_style)
    
    tempTag = []
    if show_element_tags == 'yes':
        tempTag = ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])*1.02/2, 
                           str(element), **ele_text_style) #label elements

    return tempLines, tempTag


def _plotBeam3D(iNode, jNode, ax, show_element_tags, element, eleStyle): 
    ##procedure to render a 3D two-node element. use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
    tempLines, = plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),(iNode[2], jNode[2]), marker='')
    
    if eleStyle == "wire":
        plt.setp(tempLines,**WireEle_style)
    else:
        plt.setp(tempLines,**ele_style)
    
    tempTag = []
    if show_element_tags == 'yes':
        tempTag = ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])*1.02/2, 
                          (iNode[2]+jNode[2])*1.02/2, str(element), **ele_text_style) #label elements

    return tempLines, tempTag


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
				
            figLines[jj], = plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)
				
            if show_element_tags == 'yes':
               figTags[jj] = ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])/2, str(eletag), **ele_text_style) #label elements
			
        if len(tempNodes) == 3:
            # 2D Planer three-node shell elements
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
            kNode = xyz_labels[tempNodes[2]]
				
            outputs = _plotTri2D(iNode,jNode,kNode, ax, show_element_tags, eletag, ele_style, fillSurface='yes')
            [figLines[jj], figSurfaces[SurfCounter], figTags[jj]] = [*outputs]
            SurfCounter += 1
            
						
        if len(tempNodes) == 4:
            # 2D Planer four-node shell elements
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
            kNode = xyz_labels[tempNodes[2]]
            lNode = xyz_labels[tempNodes[3]]
				
            outputs = _plotQuad2D(iNode, jNode, kNode, lNode, ax, show_element_tags, eletag, ele_style, fillSurface='yes')
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
				
            outputs = _plotBeam3D(iNode, jNode, ax, show_element_tags, eletag, "solid")

            [figLines[LineCounter], figTags[jj]] = [*outputs]
            LineCounter += 1
            
        if len(tempNodes) == 4:
            # 3D four-node Quad/shell element
            iNode = xyz_labels[tempNodes[0]]
            jNode = xyz_labels[tempNodes[1]]
            kNode = xyz_labels[tempNodes[2]]
            lNode = xyz_labels[tempNodes[3]]
				
            outputs = _plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, eletag, ele_style, fillSurface='yes')
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
				
            [tempSurfaces, tempTag] = _plotCubeVol(iNode, jNode, kNode, lNode, iiNode, jjNode, kkNode, llNode, ax, show_element_tags, eletag, 'solid', fillSurface='yes')
            
            # Store elements and surfaces
            for jj in range(6):
                figSurfaces[SurfCounter] = tempSurfaces[jj]
                SurfCounter += 1
            figTags[jj] = tempTag
            
    return figLines, figSurfaces, figTags


def _initializeFig(nodeCords,ndm, Disp = np.array([])):
    
    # set the maximum figure size
    maxFigSize = 8
    
    # Find the node 
    nodeMins = np.min(nodeCords, 0)
    nodeMaxs = np.max(nodeCords, 0)    
    
    # Get the maximum displacement in each direction
    if len(Disp) != 0:
        
        # if it's the animation
        if len(Disp.shape) == 3:
            dispmax = np.max(np.abs(Disp), (0,1))
            # dispmax = np.max(Disp, (0,1))
            # dispmin = np.min(Disp, (0,1))
            
        # if it's regular displacement 
        else:
            dispmax = np.max(np.abs(Disp), 0)
            # dispmax = np.max(Disp, 0)
            # dispmin = np.min(Disp, 0)
        # nodeMins = np.min(nodeCords, 0) + dispmin
        nodeMaxs = np.min(nodeCords, 0) - dispmax   
        nodeMaxs = np.max(nodeCords, 0) + dispmax   
        
    # Find the difference between each node.
    nodeDelta = np.abs(nodeMaxs - nodeMins)
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


def _setStandardViewport(fig, ax, nodeCords, ndm, Disp = np.array([])):
    """
    This function sets the standard viewport size of a function, using the
    nodes as an input.
    
    The displacement is sperated from the node coordinants, because in the 
    animation we want to find the bounds over all time. If displacement
    was combined with node coordinants before the funciton starts, we couldn't
    find the maximum over all time.
    
    Displcament is used in situations where nodeCoords hasn't been updated
    already - most notably in the case of animations.
       
    Parameters
    ----------
    fig : matplotlib figure object
        The figure. This is passed just incase it's needed in the future.
    ax : matplotlib ax object
        The axis object to set the size of.
    nodes : array
        An array of the bounding node coordinants in the object. This can
        simply be the node coordinats, or it can be the node coordinats with 
        updated
    ndm : int
        The number of dimenions.

    Returns
    -------
    fig : TYPE
        The updated figure.
    ax : TYPE
        The updated axis.

    """
       
    # For the displacement function, the input is a vector
    
    # Get the bounds on both x/y/z. These are vector outsputs
    nodeMins = np.min(nodeCords, 0)
    nodeMaxs = np.max(nodeCords, 0)
    
    # Get the maximum displacement in each direction
    if len(Disp) != 0:
        
        # if it's the animation
        if len(Disp.shape) == 3:
            dispmax = np.max(np.abs(Disp), (0,1))
            # dispmax = np.max(Disp, (0,1))
            # dispmin = np.min(Disp, (0,1))
            
        # if it's regular displacement 
        else:
            dispmax = np.max(np.abs(Disp), 0)
            # dispmax = np.max(Disp, 0)
            # dispmin = np.min(Disp, 0)
        # nodeMins = np.min(nodeCords, 0) + dispmin
        nodeMins = np.min(nodeCords, 0) - dispmax  
        nodeMaxs = np.max(nodeCords, 0) + dispmax  


    viewCenter = np.average([nodeMins, nodeMaxs], 0)
    viewDelta = 1.1*(abs(nodeMaxs - nodeMins))
    viewRange = max(nodeMaxs - nodeMins)
        
    if ndm == 2:
        ax.set_xlim(viewCenter[0] - viewDelta[0]/2, viewCenter[0] + viewDelta[0]/2)
        ax.set_ylim(viewCenter[1] - viewDelta[1]/2, viewCenter[1] + viewDelta[1]/2)       
        		
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        
    if ndm == 3:
        # ax.set_xlim(viewCenter[0]-(viewRange/4), viewCenter[0]+(viewRange/4))
        # ax.set_ylim(viewCenter[1]-(viewRange/4), viewCenter[1]+(viewRange/4))
        # ax.set_zlim(viewCenter[2]-(viewRange/3), viewCenter[2]+(viewRange/3))
        ax.set_xlim(viewCenter[0]-(viewRange/2), viewCenter[0]+(viewRange/2))
        ax.set_ylim(viewCenter[1]-(viewRange/2), viewCenter[1]+(viewRange/2))
        ax.set_zlim(viewCenter[2]-(viewRange/2), viewCenter[2]+(viewRange/2))
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
	   
    return fig, ax
