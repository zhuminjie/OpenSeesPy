.. include:: sub.txt

==================
 DruckerPrager
==================

.. function:: nDMaterial('DruckerPrager', matTag, K, G, sigmaY, rho, rhoBar, Kinf, Ko, delta1, delta2, H, theta, density, atmPressure=101e3)
   :noindex:

   This command is used to construct an multi dimensional material object that has a Drucker-Prager yield criterium.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``K`` |float|                      bulk modulus
   ``G`` |float|                      shear modulus
   ``sigmaY`` |float|                 yield stress
   ``rho`` |float|                    frictional strength parameter
   ``rhoBar`` |float|                 controls evolution of plastic volume change, :math:`0\le rhoBar \le rho`.
   ``Kinf`` |float|                   nonlinear isotropic strain hardening parameter, :math:`Kinf \ge 0`.
   ``Ko`` |float|                     nonlinear isotropic strain hardening parameter, :math:`Ko \ge 0`.
   ``delta1`` |float|                 nonlinear isotropic strain hardening parameter, :math:`delta1\ge 0`.
   ``delta2`` |float|                 tension softening parameter, :math:`delta2\ge 0`.
   ``H`` |float|                      linear hardening parameter, :math:`H \ge 0`.
   ``theta`` |float|                  controls relative proportions of isotropic and kinematic
                                      hardening, :math:`0 \le theta \le 1`.
   ``density`` |float|                mass density of the material
   ``atmPressure`` |float|            optional atmospheric pressure for update of elastic bulk and shear moduli
   ================================   ===========================================================================

The material formulations for the DrukerPrager object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``

See `theory <http://opensees.berkeley.edu/wiki/index.php/Drucker_Prager>`_.
