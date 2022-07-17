.. include:: sub.txt

================
 region command
================

.. function:: region(regTag, '-ele', *eles, '-eleOnly', *eles, '-eleRange', startEle, endEle, '-eleOnlyRange', startEle, endEle, '-node', *nodes, '-nodeOnly', *nodes, '-nodeRange', startNode, endNode, '-nodeOnlyRange', startNode, endNode, '-rayleigh', alphaM, betaK, betaKinit, betaKcomm)

   The region command is used to label a group of nodes and elements. This command is also used to assign rayleigh damping parameters to the nodes and elements in this region. The region is specified by either elements or nodes, not both. If elements are defined, the region includes these elements and the all connected nodes, unless the -eleOnly option is used in which case only elements are included. If nodes are specified, the region includes these nodes and all elements of which all nodes are prescribed to be in the region, unless the -nodeOnly option is used in which case only the nodes are included.


   ========================   =============================================================
   ``regTag`` |int|           unique integer tag
   ``eles`` |listi|           tags of selected elements in domain to be
	                      included in region (optional)
   ``nodes`` |listi|          tags of selected nodes in domain to be
	                      included in region (optional)
   ``startEle`` |int|	      tag for start element (optional)
   ``endEle`` |int|	      tag for end element (optional)
   ``startNode`` |int|	      tag for start node (optional)
   ``endNode`` |int|	      tag for end node (optional)
   ``alphaM`` |float|         factor applied to elements or nodes mass matrix (optional)
   ``betaK`` |float|          factor applied to elements current stiffness matrix (optional)
   ``betaKinit`` |float|      factor applied to elements initial stiffness matrix (optional)
   ``betaKcomm`` |float|      factor applied to elements committed stiffness matrix (optional)
   ========================   =============================================================


.. note::

   The user cannot prescribe the region by BOTH elements and nodes.
