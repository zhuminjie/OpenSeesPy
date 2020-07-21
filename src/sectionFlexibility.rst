.. include:: sub.txt

============================
 sectionFlexibility command
============================

.. function:: sectionFlexibility(eleTag, secNum, dof)

   Returns the section flexibility matrix for a beam-column element.
   A list of values in the row order will be returned.

   ========================   ===========================================================================
   ``eleTag`` |int|           element tag.
   ``secNum`` |int|           section number, i.e. the Gauss integratio number
   ``dof`` |int|              the dof of the section
   ========================   ===========================================================================
