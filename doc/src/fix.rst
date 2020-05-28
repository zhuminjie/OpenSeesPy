.. include:: sub.txt

=============
 fix command
=============

.. function:: fix(nodeTag, *constrValues)

   Create a homogeneous SP constriant.

   ========================   ===========================================================================
   ``nodeTag`` |int|          tag of node to be constrained
   ``constrValues`` |listi|   a list of constraint values (0 or 1),
	                      must be preceded with ``*``.

			      * ``0`` free
			      * ``1`` fixed
   ========================   ===========================================================================

For example, 

.. code-block:: python

   # fully fixed
   vals = [1,1,1]
   fix(nodeTag, *vals)

