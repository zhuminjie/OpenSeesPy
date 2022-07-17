.. include:: sub.txt

============================
 PressureDependMultiYield
============================

.. function:: nDMaterial('PressureDependMultiYield', matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac, *dilat, *liquefac, noYieldSurf=20.0, *yieldSurf=[], e=0.6, *params=[0.9, 0.02, 0.7, 101.0], c=0.3)
   :noindex:

   PressureDependMultiYield material is an elastic-plastic material for simulating the essential response characteristics of pressure sensitive soil materials under general loading conditions. Such characteristics include dilatancy (shear-induced volume contraction or dilation) and non-flow liquefaction (cyclic mobility), typically exhibited in sands or silts during monotonic or cyclic loading.

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
   ``frictionAng`` |float|            (:math:`phi`) Friction angle at peak shear
                                      strength in degrees, optional (default is 0.0).
   ``peakShearStra`` |float|          (:math:`\gamma_{max}`) An octahedral shear strain at
                                      which the maximum shear strength is reached,
				      specified at a reference mean effective confining
				      pressure refPress of p'r (see below).
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

   ``PTAng`` |float|                  (:math:`\phi_{PT}`) Phase transformation angle,
                                      in degrees.
   ``contrac`` |float|                A non-negative constant defining the rate of
                                      shear-induced volume decrease (contraction) or
                                      pore pressure buildup. A larger value corresponds
                                      to faster contraction rate.
   ``dilat`` |listf|                  Non-negative constants defining the rate of
                                      shear-induced volume increase (dilation).
                                      Larger values correspond to stronger dilation rate.
				      ``dilat = [dilat1, dilat2]``.
   ``liquefac`` |listf|               Parameters controlling the mechanism of
                                      liquefaction-induced perfectly plastic shear strain
				      accumulation, i.e., cyclic mobility.
				      Set ``liquefac[0] = 0`` to deactivate this mechanism
				      altogether. ``liquefac[0]`` defines the effective
				      confining pressure (e.g., 10 kPa in SI units or
				      1.45 psi in English units) below which the mechanism
				      is in effect. Smaller values should be assigned to
				      denser sands. ``Liquefac[1]`` defines the maximum
				      amount of perfectly plastic shear strain developed
				      at zero effective confinement during each loading
				      phase. Smaller values should be assigned to denser
				      sands. ``Liquefac[2]`` defines the maximum amount
				      of biased
				      perfectly plastic shear strain :math:`\gamma_b`
				      accumulated at
				      each loading phase under biased shear loading
				      conditions, as
				      :math:`\gamma_b=liquefac[1]\times liquefac[2]`.
				      Typically, :math:`liquefac[2]` takes a value
				      between 0.0 and 3.0. Smaller values should be
				      assigned to denser sands. See the references listed
				      at the end of this chapter for more information.
   ``noYieldSurf`` |float|            Number of yield surfaces, optional (must be less
                                      than 40, default is 20). The surfaces are generated
				      based on the hyperbolic relation defined in Note 2
				      below.
   ``yieldSurf`` |listf|              If ``noYieldSurf<0 && >-100``, the user defined
                                      yield surface is used. You have to provide
				      a list of ``2*(-noYieldSurf)``, otherwise, the arguments
				      will be messed up. Also don't provide user defined
				      yield surface if ``noYieldSurf>0``, it will
				      mess up the argument list too.
                                      Instead of automatic surfaces generation (Note 2),
                                      you can define yield surfaces directly based on
				      desired shear modulus reduction curve. To do so,
				      add a minus sign in front of noYieldSurf, then
				      provide noYieldSurf pairs of shear strain (r) and
				      modulus ratio (Gs) values. For example, to define
				      10 surfaces: yieldSurf = [r1, Gs1, ..., r10, Gs10]
   ``e`` |float|                      Initial void ratio, optional (default is 0.6).
   ``params`` |listf|                 ``params=[cs1, cs2, cs3, pa]``
                                      defining a straight critical-state line ec
				      in e-p' space.

				      If cs3=0,

				      ec = cs1-cs2 log(p'/pa)

				      else (Li and Wang, JGGE, 124(12)),

				      ec = cs1-cs2(p'/pa)cs3

				      where pa is atmospheric pressure for normalization
				      (typically 101 kPa in SI units, or 14.65 psi in
				      English units). All four constants are optional

   ``c`` |float|                      Numerical constant (default value = 0.3 kPa)
   ================================   ===========================================================================



See also `notes <http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield_Material>`_
