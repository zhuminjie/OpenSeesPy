.. include:: sub.txt

==============
 fixY command
==============

.. function:: fixY(y, *constrValues, '-tol', tol=1e-10)

   Create homogeneous SP constriants.

   ========================   ===========================================================================
   ``y`` |float|              y-coordinate of nodes to be constrained
   ``constrValues`` |listi|   a list of constraint values (0 or 1),
	                      must be preceded with ``*``.

			      * ``0`` free
			      * ``1`` fixed
   ``tol`` |float|            	user-defined tolerance (optional)
   ========================   ===========================================================================


