.. include:: sub.txt

================================
Triple Friction Pendulum Element
================================

.. function:: element('TripleFrictionPendulum', eleTag,*eleNodes,frnTag1, frnTag2, frnTag3, vertMatTag, rotZMatTag, rotXMatTag, rotYMatTag, L1, L2, L3, d1, d2, d3, W, uy, kvt, minFv, tol)
   :noindex:

   ===============================================================   ===========================================================================
   ``eleTag`` |int|                                                  unique element object tag
   ``eleNodes`` |listi|                                              a list of two element nodes
   ``frnTag1``, ``frnTag2``  ``frnTag3`` |int|                       = tags associated with previously-defined FrictionModels at the three sliding interfaces
   ``vertMatTag`` |int|                                              = Pre-defined material tag for COMPRESSION behavior of the bearing
   ``rotZMatTag``  ``rotXMatTag``  ``rotYMatTag`` |int|              = Pre-defined material tags for rotational behavior about 3-axis, 1-axis and 2-axis, respectively.
   ``L1``  ``L2``  ``L3`` |float|                                    = effective radii. Li = R_i - h_i (see Figure 1)
   ``d1``  ``d2``  ``d3`` |float|                                    = displacement limits of pendulums (Figure 1). Displacement limit of the bearing is 2   ``d1`` +   ``d2`` +   ``d3`` +   ``L1``.   ``d3``/   ``L3`` -   ``L1``.   ``d2``/   ``L2``
   ``W`` |float|                                                     = axial force used for the first trial of the first analysis step.
   ``uy`` |float|                                                    = lateral displacement where sliding of the bearing starts. Recommended value = 0.25 to 1 mm. A smaller value may cause convergence problem.
   ``kvt`` |float|                                                   = Tension stiffness k_vt of the bearing.
   ``minFv (>=0)`` |float|                                           = minimum vertical compression force in the bearing used for computing the horizontal tangent stiffness matrix from the normalized tangent stiffness matrix of the element.    ``minFv`` is substituted for the actual compressive force when it is less than    ``minFv``, and prevents the element from using a negative stiffness matrix in the horizontal direction when uplift occurs. The vertical nodal force returned to nodes is always computed from    ``kvc`` (or    ``kvt``) and vertical deformation, and thus is not affected by    ``minFv``.
   ``tol`` |float|                                                   = relative tolerance for checking the convergence of the element. Recommended value = 1.e-10 to 1.e-3.
   ===============================================================   ===========================================================================


.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Triple_Friction_Pendulum_Element>`_
