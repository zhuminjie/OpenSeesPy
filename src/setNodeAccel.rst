.. include:: sub.txt

======================
 setNodeAccel command
======================

.. function:: setNodeAccel(nodeTag, dof, value, '-commit')

   set the nodal acceleration at the specified DOF.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dof`` |int|              the DOF of the acceleration to be set.
   ``value`` |float|          acceleration value
   ``'-commit'`` |str|        commit nodal state. (optional)
   ========================   ===========================================================================
