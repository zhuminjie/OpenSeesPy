.. include:: sub.txt

==================
 eleForce command
==================

.. function:: eleForce(eleTag, dof=-1)

   Returns the elemental resisting force.

   ========================   ===========================================================================
   ``eleTag`` |int|           element tag.
   ``dof`` |int|              specific dof at the element, (optional), if no ``dof`` is
	                      provided, a list of values for all dofs is returned.
   ========================   ===========================================================================
