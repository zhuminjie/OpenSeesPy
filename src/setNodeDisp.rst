.. include:: sub.txt

======================
 setNodeDisp command
======================

.. function:: setNodeDisp(nodeTag, dof, value, '-commit')

   set the nodal displacement at the specified DOF.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dof`` |int|              the DOF of the displacement to be set.
   ``value`` |float|          displacement value
   ``'-commit'`` |str|        commit nodal state. (optional)
   ========================   ===========================================================================
