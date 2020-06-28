
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
import matplotlib.animation as animation

import numpy as np
from math import asin, sqrt
from matplotlib.widgets import Slider


import os
import openseespy.opensees as ops

import openseespy.postprocessing.internal_database_functions as idbf
import openseespy.postprocessing.internal_plotting_functions as ipltf
from openseespy.postprocessing.Get_Rendering import readODB

### All the plotting related definitions start here.

ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
# node_style = {'color':'black', 'marker':'o', 'facecolor':'black','linewidth':0.} 
node_style = {'color':'black', 'marker':'o', 'linewidth':0.} 
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


def _setStandardViewport(fig, ax, nodeCords, ndm, Disp = [], scale = 1):
    """
    This function sets the standard viewport size of a function, using the
    nodes as an input.
       
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
    
    # Adjust plot area, get the bounds on both x and y
    nodeMins = np.min(nodeCords, 0)
    nodeMaxs = np.max(nodeCords, 0)
    
    # Get the maximum displacement in each direction
    if Disp != []:
        
        # if it's the animation
        if len(Disp.shape) == 3:
            dispmax = np.max(np.abs(Disp), (0,1))*scale
        # if it's regular displacement 
        else:
            dispmax = np.max(np.abs(Disp), 0)*scale
        nodeMins = np.min(nodeCords, 0) - dispmax
        nodeMaxs = np.max(nodeCords, 0) + dispmax


    viewCenter = np.average([nodeMins, nodeMaxs], 0)
    viewDelta = 1.1*(nodeMaxs - nodeMins)
    viewRange = max(nodeMaxs - nodeMins)
        
    if ndm == 2:
        ax.set_xlim(viewCenter[0] - viewDelta[0]/2, viewCenter[0] + viewDelta[0]/2)
        ax.set_ylim(viewCenter[1] - viewDelta[1]/2, viewCenter[1] + viewDelta[1]/2)       
        		
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        
    if ndm == 3:
        ax.set_xlim(viewCenter[0]-(viewRange/4), viewCenter[0]+(viewRange/4))
        ax.set_ylim(viewCenter[1]-(viewRange/4), viewCenter[1]+(viewRange/4))
        ax.set_zlim(viewCenter[2]-(viewRange/3), viewCenter[2]+(viewRange/3))
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
	   
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
				
            figLines[jj], = plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)
				
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
    
    Input = False
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
    
    OutputObjects = [nodeObjects, *OutputObjects, NodeText]
    
    return OutputObjects
	


def getDispAnimationSlider(dt, Model, Loadcase, Scale = 1, 
                           fps = 24, FrameInterval = 0, skipFrame =1, timeScale = 1,
                           show_node_tags = 'no', show_element_tags = 'no'):
    """
    This defines the animation of an opensees model, given input data.
    
    For big models it's unlikely that the animation will actually run at the 
    desired fps in "real time". Matplotlib just isn't built for high fps 
    animation.

    Parameters
    ----------
    dt : 1D array
        The input time steps.
    deltaAni : 3D array, [NtimeAni,Nnodes,ndm]
        The input displacement of each node for all time, in every dimension.
    nodes: 
        The node list in standard format
    elements: 1D list
        The elements list in standard format.
    NodeFileName : Str
        Name of the input node information file.
    ElementFileName : Str
        Name of the input element connectivity file.
    Scale :  float, optional
        The scale on the xy/xyz displacements. The default is 1.
    fps : TYPE, optional
        The frames per second to be displayed. These values are dubious at best
        The default is 24.
    FrameInterval : float, optional
        The time interval between frames to be used. The default is 0.
    skipFrame : TYPE, optional
        DESCRIPTION. The default is 1.
    timeScale : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    TYPE
        Earthquake animation.

    """
       
    # Read Disp From ODB
    DBOutputs = readODB(Model,Loadcase)
    nodes = DBOutputs[0]
    elements = DBOutputs[1]
    Disp = DBOutputs[2]
    Disp = Disp*Scale
    
    # Reshape array
    Ntime = len(Disp[:,0])
    ndm = len(nodes[0,1:])
    Nnodes = int((len(Disp[0,:]))/ndm)
    
    # Reshape Displacements [NtimeAni,Nnodes,ndm]
    tempDisp = np.zeros([Ntime,Nnodes,ndm])
    tempDisp[:,:,0] = Disp[:,0::ndm]
    tempDisp[:,:,1] = Disp[:,1::ndm]
    if ndm == 3:
        tempDisp[:,:,2] = Disp[:,2::ndm]    
    
    Disp = tempDisp

    
    # Get nodes and elements
    ndm = len(nodes[0,1:])
    Nnodes = len(nodes[:,0])
    Nele = len(elements)
    
    nodeLabels = nodes[:, 0]       
    NodeText = [None]*Nnodes

    # initialize figure
    fig, ax = _initializeFig(nodes[:,1:], ndm)    
    
	# Adjust plot area.   
    _setStandardViewport(fig, ax, nodes[:,1:], ndm, Disp[0,:,:])
         
       
    # ========================================================================
    # Initialize Plots
    # ========================================================================
    
    initialDisp = nodes[:, 1:] + Disp[0,:,:]
    
    # Add Text
    if ndm == 2:
        time_text = ax.text(0.95, 0.01, '', verticalalignment='bottom', 
                            horizontalalignment='right', transform=ax.transAxes, color='grey')
        
        EQObjects = _plotEle_2D(nodes, elements, initialDisp, fig, ax, show_element_tags)
        [EqfigLines, EqfigSurfaces, EqfigText] = EQObjects 
        EqfigNodes, = ax.plot(tempDisp[0,:,0],tempDisp[0,:,1], **node_style)  
    
        if show_node_tags == 'yes':
            for j in range(Nnodes):
                NodeText[j] = ax.text(*nodes[j,1:]*1.02, str(int(nodes[j,0])), **node_text_style)
                
    if ndm == 3:
        
        EQObjects = _plotEle_3D(nodes, elements, initialDisp, fig, ax, show_element_tags)
        [EqfigLines, EqfigSurfaces, EqfigText] = EQObjects 
        EqfigNodes, = ax.plot(tempDisp[0,:,0], tempDisp[0,:,1], tempDisp[0,:,2], **node_style)  

        if show_node_tags == 'yes':
            for j in range(Nnodes):
                NodeText[j] = ax.text(*nodes[j,1:]*1.02, str(int(nodes[j,0])), **node_text_style)
                
    # EqfigNodes
    Nsurf = len(EqfigSurfaces)

    # ========================================================================
    # Animation
    # ========================================================================
   
    
    # Scale on displacement
    dtInput  = dt
    dtFrames  = 1/fps
    Ntime = len(Disp[:,0])
    Frames = np.arange(0,Ntime)
       
    # If the interval is zero
    if FrameInterval == 0:
        FrameInterval = dtFrames*1000/timeScale
    else: 
        pass    
        
    FrameStart = Frames[0]
    FrameEnd = Frames[-1]
    
    # Slider Location and size relative to plot
    # [x, y, xsize, ysize]
    axSlider = plt.axes([0.25, .03, 0.50, 0.02])
    plotSlider = Slider(axSlider, 'Frame', FrameStart, FrameEnd, valinit=FrameStart)
    
    # Animation controls
    global is_manual
    is_manual = False # True if user has taken control of the animation   
    
    def on_click(event):
        # Check where the click happened
        (xm,ym),(xM,yM) = plotSlider.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # user clicked somewhere else on canvas = unpause
            global is_manual
            is_manual=False    
        
    def animate2D_slider(TimeStep):
        """
        The slider value is liked with the plot - we update the plot by updating
        the slider.
        """
        global is_manual
        is_manual=True
        TimeStep = int(TimeStep)
               
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
        
        # print('loop start')
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
        time_text.set_text(round(TimeStep*dtInput,1))
        time_text.set_text(str(round(TimeStep*dtInput,1)) )        
        
        # redraw canvas while idle
        fig.canvas.draw_idle()    
            
        return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText

    def animate3D_slider(TimeStep):
        
        global is_manual
        is_manual=True
        TimeStep = int(TimeStep)
        
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
                
        # redraw canvas while idle
        fig.canvas.draw_idle()   

        return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText

    def update_plot(ii):
        print(ii)
        # If the control is manual, we don't change the plot    
        global is_manual
        if is_manual:
            return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText
       
        # Find the close timeStep and plot that
        CurrentFrame = int(np.floor(plotSlider.val))
        CurrentFrame += 1
        if CurrentFrame >= FrameEnd:
            CurrentFrame = 0
        
        # Update the slider
        plotSlider.set_val(CurrentFrame)
        is_manual = False # the above line called update_slider, so we need to reset this
        return EqfigNodes, EqfigLines, EqfigSurfaces, EqfigText

    if ndm == 2:
        plotSlider.on_changed(animate2D_slider)
    elif ndm == 3:
        plotSlider.on_changed(animate3D_slider)
    
    # assign click control
    fig.canvas.mpl_connect('button_press_event', on_click)

    ani = animation.FuncAnimation(fig, update_plot, Frames, interval = FrameInterval)
    return ani





