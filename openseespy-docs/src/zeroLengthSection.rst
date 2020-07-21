.. include:: sub.txt

=========================
zeroLengthSection Element
=========================

.. function:: element('zeroLengthSection', eleTag,*eleNodes,secTag, <'-orient', *vecx,*vecyp>, <'-doRayleigh', rFlag>)
   :noindex:

   This command is used to construct a zero length element object, which is defined by two nodes at the same location. The nodes are connected by a single section object to represent the force-deformation relationship for the element.



   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``secTag`` |int|                      tag associated with previously-defined Section object
   ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)
   ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional)
   ``rFlag`` |float|                     optional, default = 0

                                         * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)
					 * ``rFlag`` = 1 include rayleigh damping
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthSection_Element>`_
