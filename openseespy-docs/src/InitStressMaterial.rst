.. include:: sub.txt

=============================
Initial Stress Material
=============================

.. function:: uniaxialMaterial('InitStressMaterial', matTag, otherTag, initStress)
   :noindex:

   This command is used to construct an Initial Stress material object. The stress-strain behaviour for this material is defined by another material. Initial Stress Material enables definition of initial stress for the material under consideration. The strain that corresponds to the initial stress will be calculated from the other material.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``otherTag`` |float|                  tag of the other material
   ``initStress`` |float|                initial stress
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Initial_Stress_Material>`_
