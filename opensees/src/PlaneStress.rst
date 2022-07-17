.. include:: sub.txt

==================
 PlaneStress
==================

.. function:: nDMaterial('PlaneStress', matTag, mat3DTag)
   :noindex:

   This command is used to construct a plane-stress material wrapper which converts any three-dimensional material into a plane stress material via static condensation.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``mat3DTag`` |int|                 tag of perviously defined 3d ndMaterial material
   ================================   ===========================================================================

The material formulations for the PlaneStress object are:

* ``'Plane Stress'``
