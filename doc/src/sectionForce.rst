.. include:: sub.txt

======================
 sectionForce command
======================

.. function:: sectionForce(eleTag, secNum, dof)

   Returns the section force for a beam-column element. The dof of the section
   depends on the section type. Please check with the section manual.

   ========================   ===========================================================================
   ``eleTag`` |int|           element tag.
   ``secNum`` |int|           section number, i.e. the Gauss integratio number
   ``dof`` |int|              the dof of the section
   ========================   ===========================================================================
