.. include:: sub.txt

========================
 equalDOF_Mixed command
========================

.. function:: equalDOF_Mixed(rNodeTag, cNodeTag, numDOF, *rcdofs)

   Create a multi-point constraint between nodes.

	      
   ========================   ===========================================================================
   ``rNodeTag`` |int|         integer tag identifying the retained, or master node.
   ``cNodeTag`` |int|         integer tag identifying the constrained, or slave node.
   ``numDOF`` |int|           number of dofs to be constrained
   ``rcdofs`` |listi|         nodal degrees-of-freedom that are constrained at the
	                      cNode to be the same as those at the rNode
			      Valid range is from 1 through
			      ndf, the number of nodal degrees-of-freedom.

			      ``rcdofs = [rdof1, cdof1, rdof2, cdof2, ...]``
   ========================   ===========================================================================


