.. include:: sub.txt

==================
 nodeDisp command
==================

.. function:: nodeDisp(nodeTag, dof=-1)

   Returns the current displacement at a specified node.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dof`` |int|              specific dof at the node (1 through ndf), (optional), if no ``dof`` is
	                      provided, a list of values for all dofs is returned.
   ========================   ===========================================================================
