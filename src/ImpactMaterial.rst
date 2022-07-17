.. include:: sub.txt

===================
Impact Material
===================

.. function:: uniaxialMaterial('ImpactMaterial', matTag, K1, K2, sigy, gap)
   :noindex:

   This command is used to construct an impact material object

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``K1`` |float|                        initial stiffness
   ``K2`` |float|                        secondary stiffness
   ``sigy`` |float|                      yield displacement
   ``gap`` |float|                       initial gap
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Impact_Material>`_
