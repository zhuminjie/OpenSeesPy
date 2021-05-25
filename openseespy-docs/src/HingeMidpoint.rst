.. include:: sub.txt

.. _HingeMidPoint-BeamIntegration:
   
===============
 HingeMidpoint
===============

.. function:: beamIntegration('HingeMidpoint',tag,secI,lpI,secJ,lpJ,secE)
   :noindex:

   Create a HingeMidpoint beamIntegration object.
   Midpoint integration over each hinge region is the most accurate one-point integration rule;
   however, it does not place integration points at the element ends and there is a small integration
   error for linear curvature distributions along the element.

   ========================   ============================================================================
   ``tag`` |int|              tag of the beam integration.
   ``secI`` |int|             A previous-defined section object for hinge at I.
   ``lpI`` |float|            The plastic hinge length at I.
   ``secJ`` |int|             A previous-defined section object for hinge at J.
   ``lpJ`` |float|            The plastic hinge length at J.
   ``secE`` |int|             A previous-defined section object for the element interior.
   ========================   ============================================================================

   The plastic hinge length at end I (J) is equal to ``lpI`` (``lpJ``) and the associated force deformation response is defined by the ``secI`` (``secJ``). The force deformation
   response of the element interior is defined by the ``secE``.
   Typically, the interior section is linear-elastic, but this is not necessary.


   ::

      lpI = 0.1
      lpJ = 0.2
      beamIntegration('HingeMidpoint',tag,secI,lpI,secJ,lpJ,secE)




