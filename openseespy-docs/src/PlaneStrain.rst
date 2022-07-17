.. include:: sub.txt

==================
 PlaneStrain
==================

.. function:: nDMaterial('PlaneStrain', matTag, mat3DTag)
   :noindex:

   This command is used to construct a plane-stress material wrapper which converts any three-dimensional material into a plane strain material by imposing plain strain conditions on the three-dimensional material.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``mat3DTag`` |int|                 integer tag of previously defined 3d ndMaterial material
   ================================   ===========================================================================

The material formulations for the PlaneStrain object are:

* ``'PlaneStrain'``
