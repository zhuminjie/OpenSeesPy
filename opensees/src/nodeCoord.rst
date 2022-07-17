.. include:: sub.txt

==================
 nodeCoord command
==================

.. function:: nodeCoord(nodeTag, dim=-1)

   Returns the coordinates of a specified node.

   ========================   ==============================================================================
   ``nodeTag`` |int|          node tag.
   ``dof`` |int|              specific dimension at the node (1 through ndf), (optional), if no ``dim`` is
	                      provided, a list of values for all dimensions is returned.
   ========================   ==============================================================================
