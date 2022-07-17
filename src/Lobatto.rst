.. include:: sub.txt

.. _Lobatto-BeamIntegration:
   
=========
 Lobatto
=========

.. function:: beamIntegration('Lobatto',tag,secTag,N)
   :noindex:

   Create a Gauss-Lobatto beamIntegration object.
   Gauss-Lobatto integration is the most common approach for evaluating the response of
   :ref:`forceBeamColumn-Element` (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.

   ========================   =============================================================
   ``tag`` |int|              tag of the beam integration.
   ``secTag`` |int|           A previous-defined section object.
   ``N`` |int|                Number of integration points along the element.
   ========================   =============================================================

