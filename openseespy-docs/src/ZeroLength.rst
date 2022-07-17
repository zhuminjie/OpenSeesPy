.. include:: sub.txt

==================
zeroLength Element
==================

.. function:: element('zeroLength', eleTag, *eleNodes, '-mat', *matTags, '-dir', *dirs, <'-doRayleigh', rFlag=0>, <'-orient', *vecx, *vecyp>)
   :noindex:

   This command is used to construct a zeroLength element object, which is defined by two nodes at the same location. The nodes are connected by multiple UniaxialMaterial objects to represent the force-deformation relationship for the element.



   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``matTags`` |listi|                   a list of tags associated with previously-defined UniaxialMaterials
   ``dirs`` |listi|                      a list of material directions:

                                         * 1,2,3 - translation along local x,y,z axes, respectively;
					                     * 4,5,6 - rotation about local x,y,z axes, respectively
   ``rFlag`` |float|                     optional, default = 0
                                         * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)
   ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)
   ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element. (optional)

					 * ``rFlag`` = 1 include rayleigh damping
   ===================================   ===========================================================================

.. note::

   If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLength_Element>`_
