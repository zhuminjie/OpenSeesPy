.. include:: sub.txt

=================
 dispBeamColumn
=================

.. function:: element('dispBeamColumn',eleTag,*eleNodes,transfTag,integrationTag,'-cMass','-mass',mass=0.0)
   :noindex:

   Create a dispBeamColumn element.

   ========================   =============================================================
   ``eleTag`` |int|           tag of the element
   ``eleNodes`` |listi|         list of two node tags
   ``transfTag`` |int|        tag of transformation
   ``integrationTag`` |int|   tag of :func:`beamIntegration`
   ``'-cMass'``               to form consistent mass matrix (optional, default = lumped mass matrix)
   ``mass`` |float|           element mass density (per unit length), from which a lumped-mass matrix is formed (optional)
   ========================   =============================================================

