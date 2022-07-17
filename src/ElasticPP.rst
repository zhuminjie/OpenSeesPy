.. include:: sub.txt

====================================
 Elastic-Perfectly Plastic Material
====================================

.. function:: uniaxialMaterial('ElasticPP', matTag, E, epsyP, epsyN=epsyP, eps0=0.0)
   :noindex:

   This command is used to construct an elastic perfectly-plastic uniaxial material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``E`` |float|                         tangent
   ``epsyP`` |float|                     strain or deformation at which material reaches plastic state in tension
   ``epsyN`` |float|                     strain or deformation at which material
                                         reaches plastic state in compression.
                                         (optional, default is tension value)
   ``eps0`` |float|                      initial strain (optional, default: zero)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastic-Perfectly_Plastic_Material>`_
