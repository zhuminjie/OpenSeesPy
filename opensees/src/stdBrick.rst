.. include:: sub.txt

======================
Standard Brick Element
======================

This element is used to construct an eight-node brick element object, which uses a trilinear isoparametric formulation.



.. function:: element('stdBrick', eleTag,*eleNodes,matTag,<b1, b2, b3>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of eight element nodes in bottom and top faces and in counter-clockwise order
   ``matTag`` |int|                      tag of nDMaterial
   ``b1``  ``b2``  ``b3`` |float|        body forces in global x,y,z directions
   ===================================   ===========================================================================

.. note::

   #. The valid queries to a Brick element when creating an ElementRecorder object are 'forces', 'stresses,' ('strains' version > 2.2.0) and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.
   #. This element can only be defined in -ndm 3 -ndf 3

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Standard_Brick_Element>`_
