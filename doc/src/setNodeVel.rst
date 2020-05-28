.. include:: sub.txt

======================
 setNodeVel command
======================

.. function:: setNodeVel(nodeTag, dim, value, '-commit')

   set the nodal velocity at the specified dimension.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dim`` |int|              the dimension of the velinate to be set.
   ``value`` |float|          velocity value
   ``'-commit'`` |str|        commit nodal state. (optional)
   ========================   ===========================================================================
