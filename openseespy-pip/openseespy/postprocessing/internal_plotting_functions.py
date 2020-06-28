

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
							
    # Initialize varables for matplotlib objects
    tempLines = [None]
    tempSurf = [None]
    tempTag = [None]
    
    tempLines, = plt.plot((iNode[0], jNode[0], kNode[0], iNode[0]), 
                         (iNode[1], jNode[1], kNode[1], iNode[1]), marker='')
    
    # update style
    if eleStyle == "wire":
    	plt.setp(tempLines,**WireEle_style)
    else:
    	plt.setp(tempLines,**ele_style)
    
    if fillSurface == 'yes':
    	tempSurfaces = ax.fill(np.array([iNode[0], jNode[0], kNode[0]]), 
                                        np.array([iNode[1], jNode[1], kNode[1]]), color='g', alpha=.6)
        
    if show_element_tags == 'yes':
    	tempTag = ax.text((iNode[0] + jNode[0] + kNode[0])*1.0/3, (iNode[1]+jNode[1]+kNode[1])*1.0/3, 
                           str(element), **ele_text_style) #label elements
    return tempLines, tempSurfaces, tempTag


def _plotQuad2D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, eleStyle, fillSurface):
	## procedure to render a 2D four node shell element. use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
	## USe fillSurface = "yes" for color fill in the elements. fillSurface="no" for wireframe.
	   
    tempLines, = plt.plot((iNode[0], jNode[0], kNode[0], lNode[0], iNode[0]), 
               (iNode[1], jNode[1], kNode[1], lNode[1], iNode[1]), marker='')
    
    # update style
    if eleStyle == "wire":
        plt.setp(tempLines,**WireEle_style)
    else:
        plt.setp(tempLines, **ele_style)

    if fillSurface == 'yes':
        tempSurfaces = ax.fill(np.array([iNode[0], jNode[0], kNode[0], lNode[0]]), 
                               np.array([iNode[1], jNode[1], kNode[1], lNode[1]]), color='g', alpha=.6)
    
    tempTag = []
    if show_element_tags == 'yes':
        tempTag = ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0])*1.0/4, (iNode[1]+jNode[1]+kNode[1]+lNode[1])*1.0/4, 
                          str(element), **ele_text_style) #label elements
    return tempLines, tempSurfaces, tempTag


def _plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, eleStyle, fillSurface):
	## procedure to render a 3D four node shell element. use eleStyle = "wire" for a wire frame, and "solid" for solid element lines.
	## USe fillSurface = "yes" for color fill in the elements. fillSurface="no" for wireframe.
	
    # [iNode, jNode, kNode, lNode] = [*nodesCords]
    
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
        tempSurfaces = ax.plot_surface(np.array([[iNode[0], lNode[0]], [jNode[0], kNode[0]]]), 
                                       np.array([[iNode[1], lNode[1]], [jNode[1], kNode[1]]]), 
                                       np.array([[iNode[2], lNode[2]], [jNode[2], kNode[2]]]), color='g', alpha=.6)
    tempTag = []
    # Get Tag
    if show_element_tags == 'yes':
        tempTag = ax.text((iNode[0]+jNode[0]+kNode[0]+lNode[0])*1.05/4, (iNode[1]+jNode[1]+kNode[1]+lNode[1])*1.05/4, 
                          (iNode[2]+jNode[2]+kNode[2]+lNode[2])*1.05/4, str(element), **ele_text_style) #label elements

    return tempLines, tempSurfaces, tempTag

def _plotBeam3D(iNode, jNode, ax, show_element_tags, element, eleStyle):
        
    ##
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