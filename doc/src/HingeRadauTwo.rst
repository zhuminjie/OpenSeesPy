.. include:: sub.txt

===============
 HingeRadauTwo
===============

.. function:: beamIntegration('HingeRadauTwo',tag,secI,lpI,secJ,lpJ,secE)
   :noindex:

   Create a HingeRadauTwo beamIntegration object.
   Two-point Gauss-Radau integration over each hinge region places an integration
   point at the element ends and at 2/3 the hinge length inside the element. This approach
   represents linear curvature distributions exactly; however, the characteristic length for softening
   plastic hinges is not equal to the assumed plastic hinge length (equals 1/4 of the plastic hinge length).

   Arguments and examples see :ref:`HingeMidPoint-BeamIntegration`.

