.. include:: sub.txt

====================
 StressDensityModel
====================

.. function:: nDMaterial('stressDensity', matTag, mDen, eNot, A, n, nu, a1, b1, a2, b2, a3, b3, fd, muNot, muCyc, sc, M, patm, *ssls, hsl, p1)
   :noindex:

   This command is used to construct a multi-dimensional stress density material object for modeling sand behaviour following the work of Cubrinovski and Ishihara (1998a,b).

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``mDen`` |float|                   mass density
   ``eNot`` |float|                   initial void ratio
   ``A`` |float|                      constant for elastic shear modulus
   ``n`` |float|                      pressure dependency exponent for elastic shear modulus
   ``nu`` |float|                     Poisson's ratio
   ``a1`` |float|                     peak stress ratio coefficient (:math:`etaMax = a1 + b1*Is`)
   ``b1`` |float|                     peak stress ratio coefficient (:math:`etaMax = a1 + b1*Is`)
   ``a2`` |float|                     max shear modulus coefficient (:math:`Gn_max = a2 + b2*Is`)
   ``b2`` |float|                     max shear modulus coefficient (:math:`Gn_max = a2 + b2*Is`)
   ``a3`` |float|                     min shear modulus coefficient (:math:`Gn_min = a3 + b3*Is`)
   ``b3`` |float|                     min shear modulus coefficient (:math:`Gn_min = a3 + b3*Is`)
   ``fd`` |float|                     degradation constant
   ``muNot`` |float|                  dilatancy coefficient (monotonic loading)
   ``muCyc`` |float|                  dilatancy coefficient (cyclic loading)
   ``sc`` |float|                     dilatancy strain
   ``M`` |float|                      critical state stress ratio
   ``patm`` |float|                   atmospheric pressure (in appropriate units)
   ``ssls`` |listf|                   void ratio of quasi steady state (QSS-line) at pressures
                                      [pmin, 10kPa, 30kPa, 50kPa, 100kPa, 200kPa, 400kPa]
                                      (default = [0.877, 0.877, 0.873, 0.870, 0.860, 0.850, 0.833])
   ``hsl`` |float|                    void ratio of upper reference state (UR-line) for all pressures
                                      (default = 0.895)
   ``p1`` |float|                     pressure corresponding to ssl1 (default = 1.0 kPa)
   ================================   ===========================================================================

The material formulations for the StressDensityModel object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``

References

Cubrinovski, M. and Ishihara K. (1998a) 'Modelling of sand behaviour based on state concept,' Soils and Foundations, 38(3), 115-127.

Cubrinovski, M. and Ishihara K. (1998b) 'State concept and modified elastoplasticity for sand modelling,' Soils and Foundations, 38(4), 213-225.

Das, S. (2014) Three Dimensional Formulation for the Stress-Strain-Dilatancy Elasto-Plastic Constitutive Model for Sand Under Cyclic Behaviour, Master's Thesis, University of Canterbury.
