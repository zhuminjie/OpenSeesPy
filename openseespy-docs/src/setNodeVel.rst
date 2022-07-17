.. include:: sub.txt

======================
 setNodeVel command
======================

.. function:: setNodeVel(nodeTag, dof, value, '-commit')

   set the nodal velocity at the specified DOF.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dof`` |int|              the DOF of the velocity to be set.
   ``value`` |float|          velocity value
   ``'-commit'`` |str|        commit nodal state. (optional)
   ========================   ===========================================================================
