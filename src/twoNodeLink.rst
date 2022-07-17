.. include:: sub.txt

=====================
Two Node Link Element
=====================

This command is used to construct a twoNodeLink element object, which is defined by two nodes. The element can have zero or non-zero length. This element can have 1 to 6 degrees of freedom, where only the transverse and rotational degrees of freedom are coupled as long as the element has non-zero length. In addition, if the element length is larger than zero, the user can optionally specify how the P-Delta moments around the local x- and y-axis are distributed among a moment at node i, a moment at node j, and a shear couple. The sum of these three ratios is always equal to 1. In addition the shear center can be specified as a fraction of the element length from the iNode. The element does not contribute to the Rayleigh damping by default. If the element has non-zero length, the local x-axis is determined from the nodal geometry unless the optional x-axis vector is specified in which case the nodal geometry is ignored and the user-defined orientation is utilized. It is important to recognize that if this element has zero length, it does not consider the geometry as given by the nodal coordinates, but utilizes the user-defined orientation vectors to determine the directions of the springs.

.. function:: element('twoNodeLink', eleTag,*eleNodes,'-mat', *matTags, '-dir', *dir, <'-orient', *vecx, *vecyp>,<'-pDelta', *pDeltaVals>, <'-shearDist', *shearDist>, <'-doRayleigh'>, <'-mass', m>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``matTags`` |listi|                   a list of tags associated with previously-defined UniaxialMaterial objects
   ``dirs`` |listi|                      a list material directions:

                                         * 2D-case: ``1`` , ``2`` - translations along local x,y axes; ``3`` - rotation about local z axis
					 * 3D-case: ``1``, ``2``, ``3`` - translations along local x,y,z axes; ``4``, ``5``, ``6`` - rotations about local x,y,z axes
   ``vecx`` |listf|                      vector components in global coordinates defining local x-axis (optional)
   ``vecyp`` |listf|                      vector components in global coordinates defining local y-axis (optional)
   ``pDeltaVals`` |listf|                   P-Delta moment contribution ratios, size of ratio vector is 2 for 2D-case and 4 for 3D-case (entries: ``[My_iNode, My_jNode, Mz_iNode, Mz_jNode]``) ``My_iNode`` + ``My_jNode`` <= 1.0, ``Mz_iNode`` + ``Mz_jNode`` <= 1.0. Remaining P-Delta moments are resisted by shear couples. (optional)
   ``sDratios`` |listf|                  shear distances from iNode as a fraction of the element length, size of ratio vector is 1 for 2D-case and 2 for 3D-case. (entries: ``[dy_iNode, dz_iNode]``) (optional, default = ``[0.5, 0.5]``)
   ``'-doRayleigh'`` |str|               to include Rayleigh damping from the element (optional, default = no Rayleigh damping contribution)
   ``m`` |float|                         element mass (optional, default = 0.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Two_Node_Link_Element>`_
