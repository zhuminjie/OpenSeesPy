.. include:: sub.txt

==================
Hardening Material
==================

.. function:: uniaxialMaterial('Hardening', matTag, E, sigmaY, H_iso, H_kin, eta=0.0)
   :noindex:

   This command is used to construct a uniaxial material object with combined linear kinematic and isotropic hardening. The model includes optional visco-plasticity using a Perzyna formulation.



   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``E`` |float|                         tangent stiffness
   ``sigmaY`` |float|                    yield stress or force
   ``H_iso`` |float|                     isotropic hardening Modulus
   ``H_kin`` |float|                     kinematic hardening Modulus
   ``eta`` |float|                       visco-plastic coefficient (optional, default=0.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Hardening_Material>`_
