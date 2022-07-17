.. include:: sub.txt

=========
 Steel01
=========

.. function:: uniaxialMaterial('Steel01', matTag, Fy, E0, b, a1, a2, a3, a4)
   :noindex:

   This command is used to construct a uniaxial bilinear steel material object with kinematic hardening and optional isotropic hardening described by a non-linear evolution equation (REF: Fedeas).

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


.. note::

   If strain-hardening ratio is zero and you do not expect softening of your system use BandSPD solver.
