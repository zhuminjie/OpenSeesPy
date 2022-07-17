.. include:: sub.txt

================
 Steel01Thermal
================

.. function:: uniaxialMaterial('Steel01Thermal', matTag, Fy, E0, b, a1, a2, a3, a4)
   :noindex:

   This command is the thermal version for ``'Steel01'``.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``Fy`` |float|                     yield strength
   ``E0`` |float|                     initial elastic tangent
   ``b`` |float|                      strain-hardening ratio (ratio between post-yield
                                      tangent and initial elastic tangent)
   ``a1`` |float|                     isotropic hardening parameter, increase of
                                      compression yield envelope as proportion of yield
                                      strength after a plastic strain of
                                      :math:`a_2*(F_y/E_0)` (optional)
   ``a2`` |float|                     isotropic hardening parameter
                                      (see explanation under ``a1``). (optional).
   ``a3`` |float|                     isotropic hardening parameter, increase of tension
                                      yield envelope as proportion of yield strength
                                      after a plastic strain
                                      of :math:`a_4*(F_y/E_0)`. (optional)
   ``a4`` |float|                     isotropic hardening parameter (see explanation
                                      under ``a3``). (optional)
   ================================   ===========================================================================

