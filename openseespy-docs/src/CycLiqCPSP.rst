.. include:: sub.txt

==================
 CycLiqCPSP
==================

.. function:: nDMaterial('CycLiqCPSP', matTag, G0, kappa, h, M, dre1, dre2, rdr, alpha, dir, lambdac, ksi, e0, np, nd, ein, rho)
   :noindex:

   This command is used to construct a multi-dimensional material object that that follows the constitutive behavior of a cyclic elastoplasticity model for large post- liquefaction deformation.

   CycLiqCPSP material is a constitutive model for sand with special considerations for cyclic behaviour and accumulation of large post-liquefaction shear deformation, and is implemented using a cutting plane algorithm. The model: (1) achieves the simulation of post-liquefaction shear deformation based on its physics, allowing the unified description of pre- and post-liquefaction behavior of sand; (2) directly links the cyclic mobility of sand with reversible and irreversible dilatancy, enabling the unified description of monotonic and cyclic loading; (3) introduces critical state soil mechanics concepts to achieve unified modelling of sand under different states.

The critical, maximum stress ratio and reversible dilatancy surfaces follow a rounded triangle in the pi plane similar to the Matsuoka-Nakai criterion.

When this material is employed in regular solid elements (e.g., FourNodeQuad, Brick), it simulates drained soil response. When solid-fluid coupled elements (u-p elements and SSP u-p elements) are used, the model is able to simulate undrained and partially drained behavior of soil.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``G0`` |float|                     A constant related to elastic shear modulus
   ``kappa`` |float|                  bulk modulus
   ``h`` |float|                      Model parameter for plastic modulus
   ``M`` |float|                      Critical state stress ratio
   ``dre1`` |float|                   Coefficient for reversible dilatancy generation
   ``dre2`` |float|                   Coefficient for reversible dilatancy release
   ``rdr`` |float|                    Reference shear strain length
   ``alpha`` |float|                  Parameter controlling the decrease rate of irreversible dilatancy
   ``dir`` |float|                    Coefficient for irreversible dilatancy potential
   ``lambdac`` |float|                Critical state constant
   ``ksi`` |float|                    Critical state constant
   ``e0`` |float|                     Void ratio at pc=0
   ``np`` |float|                     Material constant for peak mobilized stress ratio
   ``nd`` |float|                     Material constant for reversible dilatancy generation stress ratio
   ``ein`` |float|                    Initial void ratio
   ``rho`` |float|                    Saturated mass density
   ================================   ===========================================================================

The material formulations for the CycLiqCP object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``

See also `here <http://opensees.berkeley.edu/wiki/index.php/CycLiqCPSP_Material>`_

REFERENCES: Wang R., Zhang J.M., Wang G., 2014. A unified plasticity model for large post-liquefaction shear deformation of sand. Computers and Geotechnics. 59, 54-66.
