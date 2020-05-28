.. include:: sub.txt

==================
 ElasticIsotropic
==================

.. function:: nDMaterial('ElasticIsotropic', matTag, E, nu, rho=0.0)
   :noindex:

   This command is used to construct an ElasticIsotropic material object.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``E`` |float|                      elastic modulus
   ``nu`` |float|                     Poisson's ratio
   ``rho`` |float|                    mass density (optional)
   ================================   ===========================================================================

The material formulations for the ElasticIsotropic object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``
* ``'Plane Stress'``
* ``'AxiSymmetric'``
* ``'PlateFiber'``
