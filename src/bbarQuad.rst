.. include:: sub.txt

=======================================
Bbar Plane Strain Quadrilateral Element
=======================================

This command is used to construct a four-node quadrilateral element object, which uses a bilinear isoparametric formulation along with a mixed volume/pressure B-bar assumption. This element is for plane strain problems only.



.. function:: element('bbarQuad', eleTag,*eleNodes,thick,matTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``thick`` |float|                     element thickness
   ``matTag`` |int|                      tag of nDMaterial
   ===================================   ===========================================================================

.. note::

   #. PlainStrain only.
   #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Bbar_Plane_Strain_Quadrilateral_Element>`_
