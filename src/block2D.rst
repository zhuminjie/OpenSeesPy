.. include:: sub.txt

=================
 block2D command
=================

.. function:: block2D(numX, numY, startNode, startEle, eleType, *eleArgs, *crds)

   Create mesh of quadrilateral elements

   ========================   ===========================================================================
   ``numX`` |int|             number of elements in local x directions of the block.
   ``numY`` |int|             number of elements in local y directions of the block.
   ``startNode`` |int|        node from which the mesh generation will start.
   ``startEle`` |int|         element from which the mesh generation will start.
   ``eleType`` |str|          element type (``'quad'``, ``'shell'``, ``'bbarQuad'``, 
	                      ``'enhancedQuad'``, or ``'SSPquad'``)
   ``eleArgs`` |list|         a list of element parameters.
   ``crds`` |list|            coordinates of the block elements with the format:
	      
	                      [1, x1, y1, <z1>,
   
			      2, x2, y2, <z2>,
			      
			      3, x3, y3, <z3>,
			      
			      4, x4, y4, <z4>,
			      
			      <5>, <x5>, <y5>, <z5>,
			      
			      <6>, <x6>, <y6>, <z6>,
			      
			      <7>, <x7>, <y7>, <z7>,
			      
			      <8>, <x8>, <y8>, <z8>,
			      
			      <9>, <x9>, <y9>, <z9>]

			      <> means optional
   ========================   ===========================================================================

