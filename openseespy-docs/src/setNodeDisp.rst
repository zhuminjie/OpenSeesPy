.. include:: sub.txt

======================
 setNodeDisp command
======================

.. function:: setNodeDisp(nodeTag, dim, value, '-commit')

   set the nodal displacement at the specified dimension.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dim`` |int|              the dimension of the dispinate to be set.
   ``value`` |float|          displacement value
   ``'-commit'`` |str|        commit nodal state. (optional)
   ========================   ===========================================================================
