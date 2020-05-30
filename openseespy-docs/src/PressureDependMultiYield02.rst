.. include:: sub.txt

============================
 PressureDependMultiYield02
============================

.. function:: nDMaterial('PressureDependMultiYield02', matTag, nd, rho, refShearModul, refBulkModul, frictionAng, peakShearStra, refPress, pressDependCoe, PTAng, contrac[0], contrac[2], dilat[0], dilat[2], noYieldSurf=20.0, *yieldSurf=[], contrac[1]=5.0, dilat[1]=3.0, *liquefac=[1.0,0.0],e=0.6, *params=[0.9, 0.02, 0.7, 101.0], c=0.1)
   :noindex:

   PressureDependMultiYield02 material is modified from PressureDependMultiYield material, with:

   #. additional parameters (``contrac[2]`` and ``dilat[2]``) to account for :math:`K_{\sigma}` effect,
   #. a parameter to account for the influence of previous dilation history on subsequent contraction phase (``contrac[1]``), and
   #. modified logic related to permanent shear strain accumulation (``liquefac[0]`` and ``liquefac[1]``).

   ================================   ================================================================================
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
   ``contrac[2]`` |float|             A non-negative constant reflecting :math:`K_\sigma` effect.
   ``dilat[2]`` |float|               A non-negative constant reflecting :math:`K_\sigma` effect.
   ``contrac[1]`` |float|             A non-negative constant reflecting dilation history on contraction tendency.
   ``liquefac[0]`` |float|            Damage parameter to define accumulated permanent
                                      shear strain as a function of dilation
				      history. (Redefined and different from
				      PressureDependMultiYield material).
   ``liquefac[1]`` |float|            Damage parameter to define biased accumulation of
                                      permanent shear strain as a function of load reversal
				      history. (Redefined and different from
				      PressureDependMultiYield material).
   ``c`` |float|                      Numerical constant (default value = 0.1 kPa)
   ================================   ================================================================================



See also `notes <http://opensees.berkeley.edu/wiki/index.php/PressureDependMultiYield02_Material>`_
