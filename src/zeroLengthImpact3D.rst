.. include:: sub.txt

==================
zeroLengthImpact3D
==================

.. function:: element('zeroLengthImpact3D', eleTag,*eleNodes,direction, initGap, frictionRatio, Kt, Kn, Kn2, Delta_y, cohesion)
   :noindex:

   This command constructs a node-to-node zero-length contact element in 3D space to simulate the impact/pounding and friction phenomena.



   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of a constrained and a retained nodes
   ``direction`` |int|
                                         * ``1`` if out-normal vector of master plane points to +X direction
					 * ``2`` if out-normal vector of master plane points to +Y direction
					 * ``3`` if out-normal vector of master plane points to +Z direction
   ``initGap`` |float|                   Initial gap between master plane and slave plane
   ``frictionRatio`` |float|             Friction ratio in two tangential directions (parallel to master and slave planes)
   ``Kt`` |float|                        Penalty in two tangential directions
   ``Kn`` |float|                        Penalty in normal direction (normal to master and slave planes)
   ``Kn2`` |float|                       Penalty in normal direction after yielding based on Hertz impact model
   ``Delta_y`` |float|                   Yield deformation based on Hertz impact model
   ``cohesion`` |float|                  Cohesion, if no cohesion, it is zero
   ===================================   ===========================================================================

.. note::

   #. This element has been developed on top of the "zeroLengthContact3D". All the notes available in "zeroLengthContact3D" wiki page would apply to this element as well. It includes the definition of master and slave nodes, the number of degrees of freedom in the domain, etc.
   #. Regarding the number of degrees of freedom (DOF), the end nodes of this element should be defined in 3DOF domain. For getting information on how to use 3DOF and 6DOF domain together, please refer to OpenSees documentation and forums or see the zip file provided in the EXAMPLES section below.
   #. This element adds the capabilities of "ImpactMaterial" to "zeroLengthContact3D."
   #. For simulating a surface-to-surface contact, the element can be defined for connecting the nodes on slave surface to the nodes on master surface.
   #. The element was found to be fast-converging and eliminating the need for extra elements and nodes in the modeling process.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthImpact3D>`_
