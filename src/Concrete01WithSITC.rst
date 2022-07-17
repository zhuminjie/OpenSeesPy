.. include:: sub.txt

====================
 Concrete01WithSITC
====================

.. function:: uniaxialMaterial('Concrete01WithSITC', matTag, fpc, epsc0, fpcu, epsU, endStrainSITC=0.01)
   :noindex:

   This command is used to construct a modified uniaxial Kent-Scott-Park concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. The modification is to model the effect of Stuff In The Cracks (SITC).

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fpc`` |float|                       concrete compressive strength at 28 days (compression is negative)
   ``epsc0`` |float|                     concrete strain at maximum strength
   ``fpcu`` |float|                      concrete crushing strength
   ``epsU`` |float|                      concrete strain at crushing strength
   ``endStrainSITC`` |float|             	optional, default = 0.03
   ===================================   ===========================================================================

.. note::

   #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
   #. The initial slope for this model is (2*fpc/epsc0)


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete01_Material_With_Stuff_in_the_Cracks>`_
