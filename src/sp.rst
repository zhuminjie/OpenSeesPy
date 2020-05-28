.. include:: sub.txt

============
 sp command
============

.. function:: sp(nodeTag, dof, *dofValues)

   This command is used to construct a single-point constraint object and add it to the enclosing LoadPattern.

   ========================   =============================================================
   ``nodeTag`` |int|          tag of node to which load is applied.
   ``dof`` |int|              the degree-of-freedom at the node to which constraint
	                      is applied (1 through ndf)
   ``dofValues`` |listf|      ndf reference constraint values.
   ========================   =============================================================


.. note::

   The dofValue is a reference value, it is the time series that provides the load factor. The load factor times the reference value is the constraint that is actually applied to the node.
