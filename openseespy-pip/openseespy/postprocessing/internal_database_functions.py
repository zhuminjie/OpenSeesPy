

import numpy as np
import os
import openseespy.opensees as ops



def getNodesandElements():
    """
    This function returns the nodes and elments for an active model, in a 
    standardized format. The OpenSees model must be active in order for the 
    function to work.
    
    Returns
    -------
    nodes : 2dArray
        An array of all nodes in the model.
        Returns nodes in the shape:
        [Nodes, 3] in 2d and [Nodes, 4]
        For each node the information is tored as follows:
        [NodeID, x, y] or [NodeID, x, y, z]
    elements : Array 
        An list of all elements in. Each entry in the list is it's own'
        [element1, element2,...],   element1 = [element#, node1, node2,...]

    """
   
    # Get nodes and elements
    nodeList = ops.getNodeTags()
    eleList = ops.getEleTags()   
    
    # Check Number of dimensions and intialize variables
    ndm = len(ops.nodeCoord(nodeList[0]))
    Nnodes = len(nodeList)
    nodes = np.zeros([Nnodes, ndm + 1])
    
    # Get Node list
    for ii, node in enumerate(nodeList):
        nodes[ii,0] = node
        nodes[ii,1:] = ops.nodeCoord(nodeList[ii])           
    
    Nele = len(eleList)
    elements = [None]*Nele
    
    # Generate the element list by looping through all emenemts
    for ii, ele in enumerate(eleList):
        tempNodes = ops.eleNodes(ele)
        
        tempNnodes = len(tempNodes)
        tempEle = np.zeros(tempNnodes + 1)
        
        tempEle[0] = int(ele)
        tempEle[1:] = tempNodes
        
        elements[ii] = tempEle       
    
    return nodes, elements

def _saveNodesandElements(ModelName):
    """   
    This file saves the node and element information for the structure. 
    For each node information is saved in the following format:
        Nodes:    [NodeID, xcord, ycord] or [NodeID, xcord, ycord, zcord]
    
    For elements, the element is saved with the element connectivity. 
    A different file is created for each type of element
    each possible element type.
        Elements: [EleID, eleNode1, eleNode2, ... , eleNodeN]

    Parameters
    ----------
    nodeName : str, optional
        The name of the file to be saved. The default is 'Nodes'.
    eleName : str, optional
        The name of the . The default is 'Elements'.
    delim : str, optional
        The delimeter for the output file. The default is ','.
    fmt : str, optional
        the format of the file to be saved in. The default is '%.5e'.

    """
    

    # Consider making these optional arguements
    nodeName = 'Nodes'
    eleName = 'Elements'
    delim = ' '
    fmt = '%.5e'
    ftype = '.out'
    
    ODBdir = ModelName+"_ODB"		# ODB Dir name
    
    # Creates the ODB folder if does not exist. OpenSees will overwrite the existing output data.
    if not os.path.exists(ODBdir):
        os.makedirs(ODBdir)
        
    # Read noades and elements
    nodes, elements = getNodesandElements()

    # Sort through the element arrays
    ele2Node = np.array([ele for ele in elements if len(ele) == 3])
    ele3Node = np.array([ele for ele in elements if len(ele) == 4])
    ele4Node = np.array([ele for ele in elements if len(ele) == 5])
    ele8Node = np.array([ele for ele in elements if len(ele) == 9])

    
    nodeFile = os.path.join(ODBdir, nodeName + ftype)
    
    ele2File = os.path.join(ODBdir, eleName + "_2Node" + ftype)
    ele3File = os.path.join(ODBdir, eleName + "_3Node" + ftype)
    ele4File = os.path.join(ODBdir, eleName + "_4Node"  + ftype)
    ele8File = os.path.join(ODBdir, eleName + "_8Node"  + ftype)

    # SaveNodes
    np.savetxt(nodeFile, nodes, delimiter = delim, fmt = fmt)
    
    # Save element arrays
    np.savetxt(ele2File, ele2Node, delimiter = delim, fmt = fmt)
    np.savetxt(ele3File, ele3Node, delimiter = delim, fmt = fmt)
    np.savetxt(ele4File, ele4Node, delimiter = delim, fmt = fmt)
    np.savetxt(ele8File, ele8Node, delimiter = delim, fmt = fmt)







    
def _readNodesandElements(ModelName):
    """   
    This function reads input node/element information, assuming it is in the 
    standard format. 

    If outputDir == False, the base directory will be used.    
    
    Parameters
    ----------
    nodeName : str, optional
        The base name for the node file. It will be appended to include
        the file type. The default is 'Nodes.out'.
    eleName : str, optional
        The base nae for the element files. The default is 'Elements.out'.
    delim : str, optional
        The delimiter for files to be read. The default is ','.
    dtype : TYPE, optional
        The data type to read in. The default is 'float32'.

    Returns
    -------
    nodes : Array
        An output vector in standard format
    elements : List
        An output Element vector in standard format.
        elements = [ele1, ele2,..., elen], 
        ele1 = [element, node 1, node 2, ... , node n]

    """

    # Consider making these optional arguements
    nodeName = 'Nodes'
    eleName = 'Elements'
    delim = ' '
    dtype ='float32' 
    ftype = '.out'
        
    ODBdir = ModelName+"_ODB"		# ODB Dir name
    
    # Check if output database exists
    if not os.path.exists(ODBdir):
        print('No directory found for nodes and elements')
        
    # Generate the file names
    nodeFile = os.path.join(ODBdir, nodeName + ftype)
    ele2File = os.path.join(ODBdir, eleName + "_2Node" + ftype)
    ele3File = os.path.join(ODBdir, eleName + "_3Node" + ftype)
    ele4File = os.path.join(ODBdir, eleName + "_4Node"  + ftype)
    ele8File = os.path.join(ODBdir, eleName + "_8Node"  + ftype)     
       
    eleFileNames = [ele2File, ele3File, ele4File, ele8File]    
    
    # Load Node information
    nodes = np.loadtxt(nodeFile, dtype, delimiter = delim)
    
    # Populate an array with the input element information
    TempEle = [[]]*4
    
    # Check if the file exists, read it if it does
    for ii, FileName in enumerate(eleFileNames):
        if os.path.isfile(FileName):
            TempEle[ii] = np.loadtxt(FileName, dtype,  delimiter = delim)

    # define the final element array
    elements = [*TempEle[0],*TempEle[1],*TempEle[2],*TempEle[3]]

    # Check if any files were read
    if elements is []:
        raise Exception('No files were found!')

    return nodes, elements