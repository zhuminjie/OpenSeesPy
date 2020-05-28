.. include:: sub.txt

======================
 setNodeAccel command
======================

.. function:: setNodeAccel(nodeTag, dim, value, '-commit')

   set the nodal acceleration at the specified dimension.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dim`` |int|              the dimension of the accelinate to be set.
   ``value`` |float|          acceleration value
   ``'-commit'`` |str|        commit nodal state. (optional)
   ========================   ===========================================================================
