.. include:: sub.txt

===============
SimpleContact3D
===============

This command is used to construct a SimpleContact3D element object.



.. function:: element('SimpleContact3D', eleTag,iNode, jNode, kNode, lNode, cNode, lagr_node, matTag, gTol, fTol)
   :noindex:

   ====================================================   ===========================================================================
   ``eleTag`` |int|                                       unique element object tag
   ``iNode``  ``jNode``  ``kNode``  ``lNode`` |int|       master nodes (-ndm 3 -ndf 3)
   ``cNode`` |int|                                        constrained node (-ndm 3 -ndf 3)
   ``lagr_node`` |int|                                    Lagrange multiplier node (-ndm 3 -ndf 3)
   ``matTag`` |int|                                       unique integer tag associated with previously-defined nDMaterial object
   ``gTol`` |float|                                       gap tolerance
   ``fTol`` |float|                                       force tolerance
   ====================================================   ===========================================================================


The SimpleContact3D element is a three-dimensional node-to-surface contact element which defines a frictional contact interface between two separate bodies. The master nodes are the nodes which define a surface of a hexahedral element on the first body, and the slave node is a node from the second body. The Lagrange multiplier node is required to enforce the contact condition. This node should not be shared with any other element in the domain. Information on the theory behind this element can be found in, e.g. Wriggers (2002).

.. note::

   #. The SimpleContact3D element has been written to work exclusively with the ContactMaterial3D nDMaterial object.
   #. The valid recorder queries for this element are:

      #. force - returns the contact force acting on the slave node in vector form.
      #. frictionforce - returns the frictional force acting on the slave node in vector form.
      #. forcescalar - returns the scalar magnitudes of the single normal and two tangential contact forces.
      #. The SimpleContact3D elements are set to consider frictional behavior as a default, but the frictional state of the SimpleContact3D element can be changed from the input file using the setParameter command. When updating, value of 0 corresponds to the frictionless condition, and a value of 1 signifies the inclusion of friction. An example command for this update procedure is provided below
   #. The SimpleContact3D element works well in static and pseudo-static analysis situations.
   #. In transient analysis, the presence of the contact constraints can effect the stability of commonly-used time integration methods in the HHT or Newmark family (e.g., Laursen, 2002). For this reason, use of alternative time-integration methods which numerically damp spurious high frequency behavior may be required. The TRBDF2 integrator is an effective method for this purpose. The Newmark integrator can also be effective with proper selection of the gamma and beta coefficients. The trapezoidal rule, i.e., Newmark with gamma = 0.5 and beta = 0.25, is particularly prone to instability related to the contact constraints and is not recommended.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SimpleContact3D>`_
