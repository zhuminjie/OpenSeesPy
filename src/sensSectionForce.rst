.. include:: sub.txt

==========================
 sensSectionForce command
==========================

.. function:: sensSectionForce(eleTag, <secNum>, dof, paramTag)

   Returns the current section force sensitivity to a parameter at a specified element and section.

   ========================   ===========================================================================
   ``eleTag`` |int|           element tag
   ``secNum`` |int|           section number (optional)
   ``dof`` |int|              specific dof at the element (1 through element force ndf)
   ``paramTag`` |int|         parameter tag
   ========================   ===========================================================================
