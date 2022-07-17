.. include:: sub.txt

===================
SurfaceLoad Element
===================

This command is used to construct a SurfaceLoad element object.



.. function:: element('SurfaceLoad', eleTag,*eleNodes, p)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  the four nodes defining the element, input in counterclockwise order (-ndm 3 -ndf 3)
   ``p`` |float|                         applied pressure loading normal to the surface, outward is positive, inward is negative
   ===================================   ===========================================================================

The SurfaceLoad element is a four-node element which can be used to apply surface pressure loading to 3D brick elements. The SurfaceLoad element applies energetically-conjugate forces corresponding to the input scalar pressure to the nodes associated with the element. As these nodes are shared with a 3D brick element, the appropriate nodal loads are therefore applied to the brick.



.. note::

   #. There are no valid ElementalRecorder queries for the SurfaceLoad element. Its sole purpose is to apply nodal forces to the adjacent brick element.
   #. The pressure loading from the SurfaceLoad element can be applied in a load pattern. See the analysis example below.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SurfaceLoad_Element>`_
