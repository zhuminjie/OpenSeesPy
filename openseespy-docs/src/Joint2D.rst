.. include:: sub.txt

===============
Joint2D Element
===============

This command is used to construct a two-dimensional beam-column-joint element object. The two dimensional beam-column joint is idealized as a parallelogram shaped shear panel with adjacent elements connected to its mid-points. The midpoints of the parallelogram are referred to as external nodes. These nodes are the only analysis components that connect the joint element to the surrounding structure.

.. function:: element('Joint2D', eleTag,*eleNodes, <Mat1, Mat2, Mat3, Mat4>, MatC, LrgDspTag, <'-damage', DmgTag>, <'-damage', Dmg1 Dmg2 Dmg3 Dmg4 DmgC>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of five element nodes = ``[nd1,nd2,nd3,nd4,ndC]``. ``ndC`` is the central node of beam-column joint. (the tag ``ndC`` is used to generate the internal node, thus, the node should not exist in the domain or be used by any other node)
   ``Mat1`` |int|                        uniaxial material tag for interface rotational spring at node 1. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)
   ``Mat2`` |int|                        uniaxial material tag for interface rotational spring at node 2. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)
   ``Mat3`` |int|                        uniaxial material tag for interface rotational spring at node 3. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)
   ``Mat4`` |int|                        uniaxial material tag for interface rotational spring at node 4. Use a zero tag to indicate the case that a beam-column element is rigidly framed to the joint. (optional)
   ``MatC`` |int|                        uniaxial material tag for rotational spring of the central node that describes shear panel behavior
   ``LrgDspTag`` |int|                   an integer indicating the flag for considering large deformations:
                                         * ``0`` - for small deformations and constant geometry
					 * ``1`` - for large deformations and time varying geometry
					 * ``2`` - for large deformations ,time varying geometry and length correction
   ``DmgTag`` |int|                      damage model tag
   ``Dmg1`` |int|                        damage model tag for Mat1
   ``Dmg2`` |int|                        damage model tag for Mat2
   ``Dmg3`` |int|                        damage model tag for Mat3
   ``Dmg4`` |int|                        damage model tag for Mat4
   ``DmgC`` |int|                        panel damage model tag
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Joint2D_Element>`_
