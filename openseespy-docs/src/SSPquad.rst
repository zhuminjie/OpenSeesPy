.. include:: sub.txt

===============
SSPquad Element
===============

This command is used to construct a SSPquad element object.



.. function:: element('SSPquad', eleTag,*eleNodes,matTag, type, thick,<b1, b2>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``thick`` |float|                     thickness of the element in out-of-plane direction
   ``type`` |str|                        string to relay material behavior to the element, can be either ``'PlaneStrain'`` or ``'PlaneStress'``
   ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object
   ``b1``  ``b2`` |float|                constant body forces in global x- and y-directions, respectively (optional, default = 0.0)
   ===================================   ===========================================================================

   The SSPquad element is a four-node quadrilateral element using physically stabilized single-point integration (SSP --> Stabilized Single Point). The stabilization incorporates an assumed strain field in which the volumetric dilation and the shear strain associated with the the hourglass modes are zero, resulting in an element which is free from volumetric and shear locking. The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. Analysis times are generally faster than corresponding full integration elements. The formulation for this element is identical to the solid phase portion of the SSPquadUP element as described by McGann et al. (2012).

.. note::

   #. Valid queries to the SSPquad element when creating an ElementalRecorder object correspond to those for the nDMaterial object assigned to the element (e.g., 'stress', 'strain'). Material response is recorded at the single integration point located in the center of the element.
   #. The SSPquad element was designed with intentions of duplicating the functionality of the Quad Element. If an example is found where the SSPquad element cannot do something that works for the Quad Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SSPquad_Element>`_
