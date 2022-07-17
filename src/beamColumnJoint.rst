.. include:: sub.txt

=======================
BeamColumnJoint Element
=======================

This command is used to construct a two-dimensional beam-column-joint element object. The element may be used with both two-dimensional and three-dimensional structures; however, load is transferred only in the plane of the element.



.. function:: element('beamColumnJoint', eleTag,*eleNodes,Mat1Tag, Mat2Tag, Mat3Tag, Mat4Tag, Mat5Tag, Mat6Tag, Mat7Tag, Mat8Tag, Mat9Tag, Mat10Tag, Mat11Tag, Mat12Tag, Mat13Tag, <eleHeightFac=1.0, eleWidthFac=1.0>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes
   ``Mat1Tag`` |int|                     uniaxial material tag for left bar-slip spring at node 1
   ``Mat2Tag`` |int|                     uniaxial material tag for right bar-slip spring at node 1
   ``Mat3Tag`` |int|                     uniaxial material tag for interface-shear spring at node 1
   ``Mat4Tag`` |int|                     uniaxial material tag for lower bar-slip spring at node 2
   ``Mat5Tag`` |int|                     uniaxial material tag for upper bar-slip spring at node 2
   ``Mat6Tag`` |int|                     uniaxial material tag for interface-shear spring at node 2
   ``Mat7Tag`` |int|                     uniaxial material tag for left bar-slip spring at node 3
   ``Mat8Tag`` |int|                     uniaxial material tag for right bar-slip spring at node 3
   ``Mat9Tag`` |int|                     uniaxial material tag for interface-shear spring at node 3
   ``Mat10Tag`` |int|                    uniaxial material tag for lower bar-slip spring at node 4
   ``Mat11Tag`` |int|                    uniaxial material tag for upper bar-slip spring at node 4
   ``Mat12Tag`` |int|                    uniaxial material tag for interface-shear spring at node 4
   ``Mat13Tag`` |int|                    uniaxial material tag for shear-panel
   ``eleHeightFac`` |float|              floating point value (as a ratio to the total height of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0)
   ``eleWidthFac`` |float|               floating point value (as a ratio to the total width of the element) to be considered for determination of the distance in between the tension-compression couples (optional, default: 1.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamColumnJoint_Element>`_
