.. include:: sub.txt

============
Quad Element
============

This command is used to construct a FourNodeQuad element object which uses a bilinear isoparametric formulation.



.. function:: element('quad', eleTag,*eleNodes,thick, type, matTag,<pressure=0.0, rho=0.0, b1=0.0, b2=0.0>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``thick`` |float|                     element thickness
   ``type`` |str|                        string representing material behavior. The type parameter can be either ``'PlaneStrain'`` or ``'PlaneStress'``
   ``matTag`` |int|                      tag of nDMaterial
   ``pressure`` |float|                  surface pressure (optional, default = 0.0)
   ``rho`` |float|                       element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)
   ``b1``  ``b2`` |float|                constant body forces defined in the isoparametric domain (optional, default=0.0)
   ===================================   ===========================================================================

.. note::

   #. Consistent nodal loads are computed from the pressure and body forces.
   #. The valid queries to a Quad element when creating an ElementRecorder object are 'forces', 'stresses,' and 'material $matNum matArg1 matArg2 ...' Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Quad_Element>`_
