.. include:: sub.txt

===================
FourNodeTetrahedron
===================

This command is used to construct a standard four-node tetrahedron element objec with one-point Gauss integration.



.. function:: element('FourNodeTetrahedron', eleTag,*eleNodes,matTag, <b1,b2,b3>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes
   ``matTag`` |int|                      tag of nDMaterial
   ``b1``  ``b2``  ``b3`` |float|        body forces in global x,y,z directions
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/FourNodeTetrahedron>`_
