.. include:: sub.txt

.. _NewtonCotes-BeamIntegration:
   
=============
 NewtonCotes
=============

.. function:: beamIntegration('NewtonCotes',tag,secTag,N)
   :noindex:

   Create a Newton-Cotes beamIntegration object.
   Newton-Cotes places integration points uniformly along the element, including a point at
   each end of the element.

   Places ``N`` Newton-Cotes integration points along the element. The weights for the uniformly
   spaced integration points are tabulated in references on numerical analysis. The force deformation
   response at each integration point is defined by the section.
   The order of accuracy for Gauss-Radau integration is N-1.

   Arguments and examples see :ref:`Lobatto-BeamIntegration`.

