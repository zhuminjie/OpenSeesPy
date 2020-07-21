.. include:: sub.txt

======
ASI3D8
======

This command is used to construct an eight-node zero-thickness 3D brick acoustic-structure interface element object based on a bilinear isoparametric formulation. The nodes in the acoustic domain share the same coordinates with the nodes in the solid domain.



.. function:: element('ASI3D8', eleTag, *eleNodes1, *eleNodes2)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``*eleNodes1`` |listi|                four nodes defining structure domain of element boundaries
   ``*eleNodes2`` |listi|                four nodes defining acoustic domain of element boundaries
   ===================================   ===========================================================================

.. note::

   Reference: ABAQUS theory manual. (2.9.1 Coupled acoustic-structural medium analysis)



.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ASI3D8>`_
