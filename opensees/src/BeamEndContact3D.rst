.. include:: sub.txt

================
BeamEndContact3D
================

This command is used to construct a BeamEndContact3D element object.


.. function:: element('BeamEndContact3D', eleTag,iNode, jNode, cNode, lNode, radius, gTol, fTol, <cFlag>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``iNode`` |int|                       master node from the beam (-ndm 3 -ndf 6)
   ``jNode`` |int|                       the remaining node on the beam element with ``iNode`` (-ndm 3 -ndf 6)
   ``cNode`` |int|                       constrained node (-ndm 3 -ndf 3)
   ``lNode`` |int|                       Lagrange multiplier node (-ndm 3 -ndf 3)
   ``radius`` |float|                    radius of circular beam associated with beam element
   ``gTol`` |float|                      gap tolerance
   ``fTol`` |float|                      force tolerance
   ``cFlag`` |float|                     optional initial contact flag

                                         ``cFlag`` = 0 >> contact between bodies is initially assumed (DEFAULT)
					 ``cFlag1`` = 1 >> no contact between bodies is initially assumed
   ===================================   ===========================================================================

The BeamEndContact3D element is a node-to-surface contact element which defines a normal contact interface between the end of a beam element and a separate body. The first master node ($iNode) is the beam node which is at the end of the beam (i.e. only connected to a single beam element), the second node ($jNode) is the remaining node on the beam element in question. The slave node is a node from a second body. The Lagrange multiplier node is required to enforce the contact condition. This node should not be shared with any other element in the domain, and should be created with the same number of DOF as the slave node.

The BeamEndContact3D element enforces a contact condition between a fictitious circular plane associated with a beam element and a node from a second body. The normal direction of the contact plane coincides with the endpoint tangent of the beam element at the master beam node ($iNode). The extents of this circular plane are defined by the radius input parameter. The master beam node can only come into contact with a slave node which is within the extents of the contact plane. There is a lag step associated with changing between the 'in contact' and 'not in contact' conditions.

This element was developed for use in establishing a contact condition for the tip of a pile modeled as using beam elements and the underlying soil elements in three-dimensional analysis.

.. note::

   #. The BeamEndContact3D element does not use a material object.
   #. The valid recorder queries for this element are:

      #. force - returns the contact force acting on the slave node in vector form.
      #. masterforce - returns the reactions (forces and moments) acting on the master node.
      #. The BeamEndContact3D element works well in static and pseudo-static analysis situations.
   #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamEndContact3D>`_
