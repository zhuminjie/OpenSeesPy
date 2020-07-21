.. include:: sub.txt

=======================
 Linear Transformation
=======================

.. function:: geomTransf('Linear', transfTag, '-jntOffset', *dI, *dJ)
   :noindex:

.. function:: geomTransf('Linear', transfTag, *vecxz, '-jntOffset', *dI, *dJ)
   :noindex:

   This command is used to construct a linear coordinate transformation (LinearCrdTransf) object, which performs a linear geometric transformation of beam stiffness and resisting force from the basic system to the global-coordinate system.

   ================================   ===========================================================================
   ``transfTag`` |int|                integer tag identifying transformation
   ``vecxz`` |listf|                  X, Y, and Z components of vecxz, the vector used
                                      to define the local x-z plane of the local-coordinate
                                      system. The local y-axis is defined by taking the
                                      cross product of the vecxz vector and the x-axis.
				      These components are specified in the global-coordinate
                                      system X,Y,Z and define a vector that is in a plane
                                      parallel to the x-z plane of the local-coordinate
                                      system. These items need to be specified for the
                                      three-dimensional problem.
   ``dI`` |listf|                     joint offset values -- offsets specified with respect
                                      to the global coordinate system for element-end
                                      node i (the number of arguments depends on the
                                      dimensions of the current model).
   ``dJ`` |listf|                     joint offset values -- offsets specified with respect
                                      to the global coordinate system for element-end
                                      node j (the number of arguments depends on the
                                      dimensions of the current model).
   ================================   ===========================================================================
