.. include:: sub.txt

===============
 HingeEndpoint
===============

.. function:: beamIntegration('HingeEndpoint',tag,secI,lpI,secJ,lpJ,secE)
   :noindex:

   Create a HingeEndpoint beamIntegration object.
   Endpoint integration over each hinge region moves the integration points to the element ends;
   however, there is a large integration error for linear curvature distributions along the element.

   ========================   ============================================================================
   ``tag`` |int|              tag of the beam integration.
   ``secI`` |int|             A previous-defined section object for hinge at I.
   ``lpI`` |float|            The plastic hinge length at I.
   ``secJ`` |int|             A previous-defined section object for hinge at J.
   ``lpJ`` |float|            The plastic hinge length at J.
   ``secE`` |int|             A previous-defined section object for the element interior.
   ========================   ============================================================================

   Arguments and examples see :ref:`HingeMidPoint-BeamIntegration`.

