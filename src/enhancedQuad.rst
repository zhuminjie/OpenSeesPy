.. include:: sub.txt

=====================================
Enhanced Strain Quadrilateral Element
=====================================

This command is used to construct a four-node quadrilateral element, which uses a bilinear isoparametric formulation with enhanced strain modes.



.. function:: element('enhancedQuad', eleTag,*eleNodes,thick, type, matTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``thick`` |float|                     element thickness
   ``type`` |str|                        string representing material behavior. Valid options depend on the NDMaterial object and its available material formulations. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``
   ``matTag`` |int|                      tag of nDMaterial
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Enhanced_Strain_Quadrilateral_Element>`_
