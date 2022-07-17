.. include:: sub.txt

=====
AC3D8
=====

This command is used to construct an eight-node 3D brick acoustic element object based on a trilinear isoparametric formulation.



.. function:: element('AC3D8', eleTag, *eleNodes, matTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  8 end nodes
   ``matTag`` |int|                      Material Tag of previously defined nD material
   ===================================   ===========================================================================

.. note::

   Reference: ABAQUS theory manual. (2.9.1 Coupled acoustic-structural medium analysis)



.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/AC3D8>`_
