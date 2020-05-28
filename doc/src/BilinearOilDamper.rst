.. include:: sub.txt

============================
 BilinearOilDamper Material
============================

.. function:: uniaxialMaterial('BilinearOilDamper', matTag, K_el, Cd, Fr=1.0, p=1.0, LGap=0.0,  NM=1, RelTol=1e-6, AbsTol=1e-10, MaxHalf=15)
   :noindex:

   This command is used to construct a BilinearOilDamper material, which simulates the hysteretic response of bilinear oil dampers with relief valve. Two adaptive iterative algorithms have been implemented and validated to solve numerically the constitutive equations within a bilinear oil damper with a high-precision accuracy.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``K_el`` |float|                      Elastic stiffness of linear spring to model the axial flexibility of a
                                         viscous damper (e.g. combined stiffness of the supporting brace and
					 internal damper portion)
   ``Cd`` |float|                        Damping coefficient
   ``Fr`` |float|                        Damper relief load (default=1.0, Damper property)
   ``p`` |float|                         Post-relief viscous damping coefficient ratio
                                         (default=1.0, linear oil damper)
   ``LGap`` |float|                      Gap length to simulate the gap length due to the pin tolerance
   ``NM`` |int|                          Employed adaptive numerical algorithm (default value NM = 1;

                                         * ``1`` = Dormand-Prince54,
					 * ``2`` = 6th order Adams-Bashforth-Moulton,
					 * ``3`` = modified Rosenbrock Triple)
   ``RelTol`` |float|                    Tolerance for absolute relative error control of the adaptive
                                         iterative algorithm (default value 10^-6)
   ``AbsTol`` |float|                    Tolerance for absolute error control of adaptive iterative
                                         algorithm (default value 10^-10)
   ``MaxHalf`` |int|                     Maximum number of sub-step iterations within an
                                         integration step (default value 15)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BilinearOilDamper_Material>`_
