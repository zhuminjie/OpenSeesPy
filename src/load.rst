.. include:: sub.txt

===================
 load command
===================

.. function:: load(nodeTag, *loadValues)

   This command is used to construct a NodalLoad object and add it to the enclosing LoadPattern.

   ========================   =============================================================
   ``nodeTag`` |int|          tag of node to which load is applied.
   ``loadValues`` |listf|     ndf reference load values.
   ========================   =============================================================


.. note::

   The load values are reference loads values. It is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the node.
