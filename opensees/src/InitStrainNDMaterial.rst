.. include:: sub.txt

=============================
Initial Strain Material
=============================

.. function:: nDMaterial('InitStrainNDMaterial', matTag, otherTag, initStrain, nDim)
   :noindex:

   This command is used to construct an Initial Strain material object. The stress-strain behaviour for this material is defined by another material. Initial Strain Material enables definition of initial strains for the material under consideration. The stress that corresponds to the initial strain will be calculated from the other material.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``otherTag`` |int|                    tag of the other material
   ``initStrain`` |float|                initial strain
   ``nDim`` |float|                      Number of dimensions
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Initial_Strain_Material>`_
