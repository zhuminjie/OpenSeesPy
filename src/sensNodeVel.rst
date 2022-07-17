.. include:: sub.txt

======================
 sensNodeVel command
======================

.. function:: sensNodeVel(nodeTag, dof, paramTag)

   Returns the current velocity sensitivity to a parameter at a specified node.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag
   ``dof`` |int|              specific dof at the node (1 through ndf)
   ``paramTag`` |int|         parameter tag
   ========================   ===========================================================================
