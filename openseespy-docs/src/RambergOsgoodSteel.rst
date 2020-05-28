.. include:: sub.txt

====================
 RambergOsgoodSteel
====================

.. function:: uniaxialMaterial('RambergOsgoodSteel', matTag, fy, E0, a, n)
   :noindex:

   This command is used to construct a Ramberg-Osgood steel material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fy`` |float|                        Yield strength
   ``E0`` |float|                        initial elastic tangent
   ``a`` |float|                         "yield offset" and the Commonly used value for a is 0.002
   ``n`` |float|                         Parameters to control the transition from elastic
                                         to plastic branches. And controls the hardening
					 of the material by increasing the "n" hardening ratio will be decreased.
					 Commonly used values for n are ~5 or greater.
   ===================================   ===========================================================================



.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/RambergOsgoodSteel_Material>`_
