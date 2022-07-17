.. include:: sub.txt

==================
 CycLiqCP
==================

.. function:: nDMaterial('CycLiqCP', matTag, G0, kappa, h, Mfc, dre1, Mdc, dre2, rdr, alpha, dir, ein, rho)
   :noindex:

   This command is used to construct a multi-dimensional material object that that follows the constitutive behavior of a cyclic elastoplasticity model for large post- liquefaction deformation.

   CycLiqCP material is a cyclic elastoplasticity model for large post-liquefaction deformation, and is implemented using a cutting plane algorithm. The model is capable of reproducing small to large deformation in the pre- to post-liquefaction regime. The elastic moduli of the model are pressure dependent. The plasticity in the model is developed within the framework of bounding surface plasticity, with special consideration to the formulation of reversible and irreversible dilatancy.

The model does not take into consideration of the state of sand, and requires different parameters for sand under different densities and confining pressures. The surfaces (i.e. failure and maximum pre-stress) are considered as circles in the pi plane.

The model has been validated against VELACS centrifuge model tests and has used on numerous simulations of liquefaction related problems.

When this material is employed in regular solid elements (e.g., FourNodeQuad, Brick), it simulates drained soil response. When solid-fluid coupled elements (u-p elements and SSP u-p elements) are used, the model is able to simulate undrained and partially drained behavior of soil.


   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``G0`` |float|                     A constant related to elastic shear modulus
   ``kappa`` |float|                  bulk modulus
   ``h`` |float|                      Model parameter for plastic modulus
   ``Mfc`` |float|                    Stress ratio at failure in triaxial compression
   ``dre1`` |float|                   Coefficient for reversible dilatancy generation
   ``Mdc`` |float|                    Stress ratio at which the reversible dilatancy sign changes
   ``dre2`` |float|                   Coefficient for reversible dilatancy release
   ``rdr`` |float|                    Reference shear strain length
   ``alpha`` |float|                  Parameter controlling the decrease rate of irreversible dilatancy
   ``dir`` |float|                    Coefficient for irreversible dilatancy potential
   ``ein`` |float|                    Initial void ratio
   ``rho`` |float|                    Saturated mass density
   ================================   ===========================================================================

The material formulations for the CycLiqCP object are:

* ``'ThreeDimensional'``
* ``'PlaneStrain'``

See also `here <http://opensees.berkeley.edu/wiki/index.php/CycLiqCP_Material_(Cyclic_ElasticPlasticity)>`_
