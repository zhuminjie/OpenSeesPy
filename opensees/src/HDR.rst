.. include:: sub.txt

===
HDR
===

This command is used to construct an HDR bearing element object in three-dimension. The 3D continuum geometry of an high damping rubber bearing is modeled as a 2-node, 12 DOF discrete element. This is the third element in the series of elements developed for analysis of base-isolated structures under extreme loading (others being ElastomericX and LeadRubberX). The major difference between HDR element with ElastomericX is the hysteresis model in shear. The HDR element uses a model proposed by Grant et al. (2004) to capture the shear behavior of a high damping rubber bearing. The time-dependent values of mechanical properties (e.g., vertical stiffness, buckling load capacity) can also be recorded using the "parameters" recorder.



.. function:: element('HDR', eleTag,*eleNodes,Gr, Kbulk, D1, D2, ts, tr, n, a1, a2, a3, b1, b2, b3, c1, c2, c3, c4, <<x1, x2, x3>, y1, y2, y3>,<kc>,<PhiM>,<ac>,<sDratio>,<m>,<tc>)
   :noindex:

   For 3D problem

   =========================================================================================   ===========================================================================
   ``eleTag`` |int|                                                                            unique element object tag
   ``eleNodes`` |listi|                                                                        a list of two element nodes
   ``Gr`` |float|                                                                              shear modulus of elastomeric bearing
   ``Kbulk`` |float|                                                                           bulk modulus of rubber
   ``D1`` |float|                                                                              internal diameter
   ``D2`` |float|                                                                              outer diameter (excluding cover thickness)
   ``ts`` |float|                                                                              single steel shim layer thickness
   ``tr`` |float|                                                                              single rubber layer thickness
   ``n`` |int|                                                                                 number of rubber layers
   ``a1``  ``a2``  ``a3``  ``b1``  ``b2``  ``b3``  ``c1``  ``c2``  ``c3``  ``c4`` |float|      parameters of the Grant model
   ``x1``  ``x2``  ``x3`` |float|                                                              vector components in global coordinates defining local x-axis (optional)
   ``y1``  ``y2``  ``y3`` |float|                                                              vector components in global coordinates defining local y-axis (optional)
   ``kc`` |float|                                                                              cavitation parameter (optional, default = 10.0)
   ``PhiM`` |float|                                                                            damage parameter (optional, default = 0.5)
   ``ac`` |float|                                                                              strength reduction parameter (optional, default = 1.0)
   ``sDratio`` |float|                                                                         shear distance from iNode as a fraction of the element length (optional, default = 0.5)
   ``m`` |float|                                                                               element mass (optional, default = 0.0)
   ``tc`` |float|                                                                              cover thickness (optional, default = 0.0)
   =========================================================================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/HDR>`_
