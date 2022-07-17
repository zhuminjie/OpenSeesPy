.. include:: sub.txt

==============================================
 Legendre  
==============================================

.. function:: beamIntegration('Legendre',tag,secTag,N)
   :noindex:

   Create a Gauss-Legendre beamIntegration object.
   Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common
   in force-based elements because there are no integration points at the element ends.


   Places ``N`` Gauss-Legendre integration points along the element. The location and weight
   of each integration point are tabulated in references on numerical analysis.
   The force deformation response at each integration point is defined by the section.
   The order of accuracy for Gauss-Legendre integration is 2N-1.

   Arguments and examples see :ref:`Lobatto-BeamIntegration`.

