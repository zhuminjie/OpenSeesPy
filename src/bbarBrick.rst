.. include:: sub.txt

==================
Bbar Brick Element
==================

This command is used to construct an eight-node mixed volume/pressure brick element object, which uses a trilinear isoparametric formulation.



.. function:: element('bbarBrick', eleTag,*eleNodes,matTag,<b1,b2,b3>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of eight element nodes in bottom and top faces and in counter-clockwise order
   ``matTag`` |int|                      tag of nDMaterial
   ``b1``  ``b2``  ``b3`` |float|        body forces in global x,y,z directions
   ===================================   ===========================================================================

.. note::

   #. Node numbering for this element is different from that for the eight-node brick (Brick8N) element.
   #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses', 'strains', and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Bbar_Brick_Element>`_
