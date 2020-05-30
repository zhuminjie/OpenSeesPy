.. include:: sub.txt

=========================
 nodeEigenvector command
=========================

.. function:: nodeEigenvector(nodeTag, eigenvector, dof=-1)

   Returns the eigenvector at a specified node.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``eigenvector`` |int|      mode number of eigenvector to be returned
   ``dof`` |int|              specific dof at the node (1 through ndf), (optional), if no ``dof`` is
	                      provided, a list of values for all dofs is returned.
   ========================   ===========================================================================
