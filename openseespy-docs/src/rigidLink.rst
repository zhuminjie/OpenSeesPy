.. include:: sub.txt

===================
 rigidLink command
===================

.. function:: rigidLink(type, rNodeTag, cNodeTag)

   Create a multi-point constraint between nodes.
	      
   ========================   ===========================================================================
   ``type`` |str|             string-based argument for rigid-link type:

                              * ``'bar'``: only the translational degree-of-freedom will be constrained to be exactly the same as those at the master node
			      * ``'beam'``: both the translational and rotational degrees of freedom are constrained.
   ``rNodeTag`` |int|         integer tag identifying the master node
   ``cNodeTag`` |int|         integar tag identifying the slave node
   ========================   ===========================================================================


