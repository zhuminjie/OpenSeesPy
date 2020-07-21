.. include:: sub.txt

===========
 UserHinge
===========

.. function:: beamIntegration('UserHinge',tag,secETag,npL,*secsLTags,*locsL,*wtsL,npR,*secsRTags,*locsR,*wtsR)
   :noindex:

   Create a UserHinge beamIntegration object.

   ========================   ============================================================================
   ``tag`` |int|              tag of the beam integration
   ``secETag`` |int|             A previous-defined section objects for non-hinge area.
   ``npL`` |int|              number of integration points along the left hinge.
   ``secsLTags`` |listi|          A list of previous-defined section objects for left hinge area.
   ``locsL`` |listf|          A list of locations of integration points for left hinge area.
   ``wtsL`` |listf|           A list of weights of integration points for left hinge area.
   ``npR`` |int|              number of integration points along the right hinge.
   ``secsRTags`` |listi|          A list of previous-defined section objects for right hinge area.
   ``locsR`` |listf|          A list of locations of integration points for right hinge area.
   ``wtsR`` |listf|           A list of weights of integration points for right hinge area.
   ========================   ============================================================================

   ::

      tag = 1
      secE = 5
      
      npL = 2
      secsL = [1,2]
      locsL = [0.1,0.2]
      wtsL = [0.5,0.5]
      
      npR = 2
      secsR = [3,4]
      locsR = [0.8,0.9]
      wtsR = [0.5,0.5]

      beamIntegration('UserHinge',tag,secE,npL,*secsL,*locsL,*wtsL,npR,*secsR,*locsR,*wtsR)




