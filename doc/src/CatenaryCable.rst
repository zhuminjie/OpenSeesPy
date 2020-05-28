.. include:: sub.txt

====================
CatenaryCableElement
====================

This command is used to construct a catenary cable element object.



.. function:: element('CatenaryCable', eleTag,iNode, jNode, weight, E, A, L0, alpha, temperature_change, rho, errorTol, Nsubsteps, massType)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``iNode``  ``jNode`` |int|            end nodes (3 dof per node)
   ``weight`` |float|                    undefined
   ``E`` |float|                         elastic modulus of the cable material
   ``A`` |float|                         cross-sectional area of element
   ``L0`` |float|                        unstretched length of the cable
   ``alpha`` |float|                     coefficient of thermal expansion
   ``temperature_change`` |float|        temperature change for the element
   ``rho`` |float|                       mass per unit length
   ``errorTol`` |float|                  allowed tolerance for within-element equilbrium (Newton-Rhapson iterations)
   ``Nsubsteps`` |int|                   number of within-element substeps into which equilibrium iterations are subdivided (not number of steps to convergence)
   ``massType`` |int|                    Mass matrix model to use (``massType`` = 0 lumped mass matrix,    ``massType`` = 1 rigid-body mass matrix (in development))
   ===================================   ===========================================================================

This cable is a flexibility-based formulation of the catenary cable. An iterative scheme is used internally to compute equilibrium. At each iteration, node i is considered fixed while node j is free. End-forces are applied at node-j and its displacements computed. Corrections to these forces are applied iteratively using a Newton-Rhapson scheme (with optional sub-stepping via $Nsubsteps) until nodal displacements are within the provided tolerance ($errortol). When convergence is reached, a stiffness matrix is computed by inversion of the flexibility matrix and rigid-body mode injection.


.. note::

   #. The stiffness of the cable comes from the large-deformation interaction between loading and cable shape. Therefore, all cables must have distributed forces applied to them. See example. Should not work for only nodal forces.
   #. Valid queries to the CatenaryCable element when creating an ElementalRecorder object correspond to 'forces', which output the end-forces of the element in global coordinates (3 for each node).
   #. Only the lumped-mass formulation is currently available.
   #. The element does up 100 internal iterations. If convergence is not achieved, will result in error and some diagnostic information is printed out.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/CatenaryCableElement>`_
