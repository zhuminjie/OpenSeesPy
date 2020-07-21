.. include:: sub.txt

============================
 MultiaxialCyclicPlasticity
============================

.. function:: nDMaterial('MultiaxialCyclicPlasticity', matTag, rho, K, G, Su, Ho, h, m, beta, KCoeff)
   :noindex:

   This command is used to construct an multiaxial Cyclic Plasticity model for clays

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``rho`` |float|                    density
   ``K`` |float|                      buck modulus
   ``G`` |float|                      maximum (small strain) shear modulus
   ``Su`` |float|                     undrained shear strength, size of bounding
                                      surface :math:`R=\sqrt{8/3}*Su`
   ``Ho`` |float|                     linear kinematic hardening modulus of bounding surface
   ``h`` |float|                      hardening parameter
   ``m`` |float|                      hardening parameter
   ``beta`` |float|                   integration parameter, usually beta=0.5
   ``KCoeff`` |float|                 coefficient of earth pressure, K0
   ================================   ===========================================================================
