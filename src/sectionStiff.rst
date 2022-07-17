.. include:: sub.txt

==========================
 sectionStiffness command
==========================

.. function:: sectionStiffness(eleTag, secNum)

   Returns the section stiffness matrix for a beam-column element.
   A list of values in the row order will be returned.

   ========================   ===========================================================================
   ``eleTag`` |int|           element tag.
   ``secNum`` |int|           section number, i.e. the Gauss integration number
   ========================   ===========================================================================
