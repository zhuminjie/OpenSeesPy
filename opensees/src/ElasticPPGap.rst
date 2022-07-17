.. include:: sub.txt

========================================
 Elastic-Perfectly Plastic Gap Material
========================================

.. function:: uniaxialMaterial('ElasticPPGap', matTag, E, Fy, gap, eta=0.0, damage='noDamage')
   :noindex:

   This command is used to construct an elastic perfectly-plastic gap uniaxial material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``E`` |float|                         tangent
   ``Fy`` |float|                        stress or force at which material reaches plastic state
   ``gap`` |float|                       initial gap (strain or deformation)
   ``eta`` |float|                       hardening ratio (=Eh/E), which can be negative
   ``damage`` |str|                      an optional string to specify whether to accumulate
                                         damage or not in the material. With the default
					 string, ``'noDamage'`` the gap material will
					 re-center on load reversal.
					 If the string ``'damage'``
					 is provided this recentering will not occur and gap
					 will grow.
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic-Perfectly_Plastic_Gap_Material>`_
