.. include:: sub.txt

===========
MultiLinear
===========

.. function:: uniaxialMaterial('MultiLinear', matTag, *pts)
   :noindex:

   This command is used to construct a uniaxial multilinear material object.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``pts`` |listf|                       a list of strain and stress points

                                         ``pts = [strain1, stress1, strain2, stress2, ..., ]``
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/MultiLinear_Material>`_
