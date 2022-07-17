.. include:: sub.txt

=============
BeamContact3D
=============

This command is used to construct a BeamContact3D element object.




.. function:: element('BeamContact3D', eleTag,iNode, jNode, cNode, lNode, radius, crdTransf, matTag, gTol, fTol, <cFlag>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``iNode``  ``jNode`` |int|            master nodes (-ndm 3 -ndf 6)
   ``cNode`` |int|                       constrained node (-ndm 3 -ndf 3)
   ``lNode`` |int|                       Lagrange multiplier node (-ndm 3 -ndf 3)
   ``radius`` |float|                    constant radius of circular beam associated with beam element
   ``crdTransf`` |int|                   unique integer tag associated with previously-defined geometricTransf object
   ``matTag`` |int|                      unique integer tag associated with previously-defined nDMaterial object
   ``gTol`` |float|                      gap tolerance
   ``fTol`` |float|                      force tolerance
   ``cFlag`` |int|                       optional initial contact flag

                                         ``cFlag`` = 0 >> contact between bodies is initially assumed (DEFAULT)

					 ``cFlag`` = 1 >> no contact between bodies is initially assumed
   ===================================   ===========================================================================

The BeamContact3D element is a three-dimensional beam-to-node contact element which defines a frictional contact interface between a beam element and a separate body. The master nodes (6 DOF) are the endpoints of the beam element, and the slave node (3 DOF) is a node from a second body. The Lagrange multiplier node (3 DOF) is required to enforce the contact condition. Each contact element should have a unique Lagrange multiplier node. The Lagrange multiplier node should not be fixed, otherwise the contact condition will not work.

.. note::

   #. The BeamContact3D element has been written to work exclusively with the ContactMaterial3D nDMaterial object.
   #. The valid recorder queries for this element are:

      #. force - returns the contact force acting on the slave node in vector form.
      #. frictionforce - returns the frictional force acting on the slave node in vector form.
      #. forcescalar - returns the scalar magnitudes of the single normal and two tangential contact forces.
      #. masterforce - returns the reactions (forces only) acting on the master nodes.
      #. mastermoment - returns the reactions (moments only) acting on the master nodes.
      #. masterreaction - returns the full reactions (forces and moments) acting on the master nodes.
      #. The BeamContact3D elements are set to consider frictional behavior as a default, but the frictional state of the BeamContact3D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below
   #. The BeamContact3D element works well in static and pseudo-static analysis situations.
   #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/BeamContact3D>`_
