.. include:: sub.txt

===========================
 eleDynamicalForce command
===========================

.. function:: eleDynamicalForce(eleTag, dof=-1)

   Returns the elemental dynamic force.

   ========================   ===========================================================================
   ``eleTag`` |int|           element tag.
   ``dof`` |int|              specific dof at the element, (optional), if no ``dof`` is
	                      provided, a list of values for all dofs is returned.
   ========================   ===========================================================================
