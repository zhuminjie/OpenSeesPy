.. include:: sub.txt

=============
Shell Element
=============

This command is used to construct a ShellMITC4 element object, which uses a bilinear isoparametric formulation in combination with a modified shear interpolation to improve thin-plate bending performance.



.. function:: element('ShellMITC4', eleTag,*eleNodes,secTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. Currently must be either a ``'PlateFiberSection'``, or ``'ElasticMembranePlateSection'``
   ===================================   ===========================================================================

.. note::

   #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.
   #. It is a 3D element with 6 dofs and CAN NOT be used in 2D domain.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Shell_Element>`_
