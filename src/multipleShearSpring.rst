.. include:: sub.txt

===========================
MultipleShearSpring Element
===========================

This command is used to construct a multipleShearSpring (MSS) element object, which is defined by two nodes. This element consists of a series of identical shear springs arranged radially to represent the isotropic behavior in the local y-z plane.


.. function:: element('multipleShearSpring', eleTag,*eleNodes,nSpring,'-mat', matTag,<'-lim', lim>,<'-orient',<x1, x2, x3>, yp1, yp2, yp3>,<'-mass', mass>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``nSpring`` |int|                     number of springs
   ``matTag`` |int|                      tag associated with previously-defined UniaxialMaterial object
   ``lim`` |float|                       minimum deformation to calculate equivalent coefficient (see note 1)
   ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis
   ``yp1``  ``yp2``  ``yp3`` |float|     vector components in global coordinates defining vector yp which lies in the local x-y plane for the element
   ``mass`` |float|                         element mass
   ===================================   ===========================================================================

.. note::

   If ``dsp`` is positive and the shear deformation of MSS exceeds    ``dsp``, this element calculates equivalent coefficient to adjust force and stiffness of MSS. The adjusted MSS force and stiffness reproduce the behavior of the previously defined uniaxial material under monotonic loading in every direction. If    ``dsp`` is zero, the element does not calculate the equivalent coefficient.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/MultipleShearSpring_Element>`_
