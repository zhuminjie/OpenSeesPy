.. include:: sub.txt

==================
 Concrete01
==================

.. function:: uniaxialMaterial('Concrete01', matTag, fpc, epsc0, fpcu, epsU)
   :noindex:

   This command is used to construct a uniaxial Kent-Scott-Park concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. (REF: Fedeas).

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fpc`` |float|                       concrete compressive strength at 28 days (compression is negative)
   ``epsc0`` |float|                     concrete strain at maximum strength
   ``fpcu`` |float|                      concrete crushing strength
   ``epsU`` |float|                      concrete strain at crushing strength
   ===================================   ===========================================================================

.. note::

   #. Compressive concrete parameters should be input as negative values (if input as positive, they will be converted to negative internally).
   #. The initial slope for this model is (2*fpc/epsc0)


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Concrete01_Material_--_Zero_Tensile_Strength>`_
