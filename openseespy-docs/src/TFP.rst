.. include:: sub.txt

========================================
Triple Friction Pendulum Bearing Element
========================================

This command is used to construct a Triple Friction Pendulum Bearing element object, which is defined by two nodes. The element can have zero length or the appropriate bearing height. The bearing has unidirectional (2D) or coupled (3D) friction properties (with post-yield stiffening due to the concave sliding surface) for the shear deformations, and force-deformation behaviors defined by UniaxialMaterials in the remaining two (2D) or four (3D) directions. To capture the uplift behavior of the bearing, the user-specified UniaxialMaterial in the axial direction is modified for no-tension behavior. P-Delta moments are entirely transferred to the concave sliding surface (iNode). It is important to note that rotations of the concave sliding surface (rotations at the iNode) affect the shear behavior of the bearing. If the element has non-zero length, the local x-axis is determined from the nodal geometry unless the optional x-axis vector is specified in which case the nodal geometry is ignored and the user-defined orientation is utilized.

.. function:: element('TFP', eleTag,*eleNodes,R1, R2, R3, R4, Db1, Db2, Db3, Db4, d1, d2, d3, d4, mu1, mu2, mu3, mu4, h1, h2, h3, h4, H0, colLoad,<K>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``R1`` |float|                        Radius of inner bottom sliding surface
   ``R2`` |float|                        Radius of inner top sliding surface
   ``R3`` |float|                        Radius of outer bottom sliding surface
   ``R4`` |float|                        Radius of outer top sliding surface
   ``Db1`` |float|                       Diameter of inner bottom sliding surface
   ``Db2`` |float|                       Diameter of inner top sliding surface
   ``Db3`` |float|                       Diameter of outer bottom sliding surface
   ``Db4`` |float|                       Diameter of outer top sliding surface
   ``d1`` |float|                        diameter of inner slider
   ``d2`` |float|                        diameter of inner slider
   ``d3`` |float|                        diameter of outer bottom slider
   ``d4`` |float|                        diameter of outer top slider
   ``mu1`` |float|                       friction coefficient of inner bottom sliding surface
   ``mu2`` |float|                       friction coefficient of inner top sliding surface
   ``mu3`` |float|                       friction coefficient of outer bottom sliding surface
   ``mu4`` |float|                       friction coefficient of outer top sliding surface
   ``h1`` |float|                        height from inner bottom sliding surface to center of bearing
   ``h2`` |float|                        height from inner top sliding surface to center of bearing
   ``h3`` |float|                        height from outer bottom sliding surface to center of bearing
   ``h4`` |float|                        height from inner top sliding surface to center of bearing
   ``H0`` |float|                        total height of bearing
   ``colLoad`` |float|                   initial axial load on bearing (only used for first time step then load come from model)
   ``K`` |float|                         optional, stiffness of spring in vertical dirn (dof 2 if ndm= 2, dof 3 if ndm = 3) (default=1.0e15)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Bearing_Element>`_
