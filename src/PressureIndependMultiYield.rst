.. include:: sub.txt

============================
 PressureIndependMultiYield
============================

.. function:: nDMaterial('PressureIndependMultiYield', matTag, nd, rho, refShearModul, refBulkModul, cohesi, peakShearStra, frictionAng=0., refPress=100., pressDependCoe=0., noYieldSurf=20, *yieldSurf)
   :noindex:

   PressureIndependMultiYield material is an elastic-plastic material in which plasticity exhibits only in the deviatoric stress-strain response. The volumetric stress-strain response is linear-elastic and is independent of the deviatoric response. This material is implemented to simulate monotonic or cyclic response of materials whose shear behavior is insensitive to the confinement change. Such materials include, for example, organic soils or clay under fast (undrained) loading conditions.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``nd`` |float|                     Number of dimensions, 2 for plane-strain, and 3 for 3D analysis.
   ``rho`` |float|                    Saturated soil mass density.
   ``refShearModul`` |float|          (:math:`G_r`) Reference low-strain shear modulus,
                                      specified at a reference mean effective confining
                                      pressure refPress of p'r (see below).
   ``refBulkModul`` |float|           (:math:`B_r`) Reference bulk modulus,
                                      specified at a reference
                                      mean effective confining pressure refPress
                                      of p'r (see below).
   ``cohesi`` |float|                 (:math:`c`) Apparent cohesion at zero
                                      effective confinement.
   ``peakShearStra`` |float|          (:math:`\gamma_{max}`) An octahedral shear strain at
                                      which the maximum shear strength is reached,
				      specified at a reference mean effective confining
				      pressure refPress of p'r (see below).
   ``frictionAng`` |float|            (:math:`phi`) Friction angle at peak shear
                                      strength in degrees, optional (default is 0.0).
   ``refPress`` |float|               (:math:`p'_r`) Reference mean effective confining
                                      pressure at which
				      :math:`G_r`, :math:`B_r`, and :math:`\gamma_{max}`
				      are defined, optional (default is 100. kPa).
   ``pressDependCoe`` |float|         (:math:`d`) A positive constant defining variations
                                      of :math:`G` and :math:`B` as a function of
				      instantaneous effective
				      confinement :math:`p'` (default is 0.0)

				      :math:`G=G_r(\frac{p'}{p'_r})^d`

				      :math:`B=B_r(\frac{p'}{p'_r})^d`

				      If :math:`\phi=0`, :math:`d` is reset to 0.0.

   ``noYieldSurf`` |float|            Number of yield surfaces, optional (must be less
                                      than 40, default is 20). The surfaces are generated
				      based on the hyperbolic relation defined in Note 2
				      below.
   ``yieldSurf`` |listf|              Instead of automatic surfaces generation (Note 2),
                                      you can define yield surfaces directly based on
				      desired shear modulus reduction curve. To do so,
				      add a minus sign in front of noYieldSurf, then
				      provide noYieldSurf pairs of shear strain (r) and
				      modulus ratio (Gs) values. For example, to define
				      10 surfaces: yieldSurf = [r1, Gs1, ..., r10, Gs10]
   ================================   ===========================================================================



See also `notes <http://opensees.berkeley.edu/wiki/index.php/PressureIndependMultiYield_Material>`_
