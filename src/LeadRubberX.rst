.. include:: sub.txt

===========
LeadRubberX
===========

This command is used to construct a LeadRubberX bearing element object in three-dimension. The 3D continuum geometry of a lead rubber bearing is modeled as a 2-node, 12 DOF discrete element. It extends the formulation of ElastomericX by including strength degradation in lead rubber bearing due to heating of the lead-core. The LeadRubberX element requires only the geometric and material properties of an elastomeric bearing as arguments. The material models in six direction are formulated within the element from input arguments. The time-dependent values of mechanical properties (e.g., shear stiffness, buckling load capacity, temperature in the lead-core, yield strength) can also be recorded using the "parameters" recorder.



.. function:: element('LeadRubberX', eleTag,*eleNodes,Fy, alpha, Gr, Kbulk, D1, D2, ts, tr, n, <<x1, x2, x3>, y1, y2, y3>,<kc>,<PhiM>,<ac>,<sDratio>,<m>,<cd>,<tc>,<qL>,<cL>,<kS>,<aS>,<tag1>,<tag2>,<tag3>,<tag4>,<tag5>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``Fy`` |float|                        yield strength
   ``alpha`` |float|                     post-yield stiffness ratio
   ``Gr`` |float|                        shear modulus of elastomeric bearing
   ``Kbulk`` |float|                     bulk modulus of rubber
   ``D1`` |float|                        internal diameter
   ``D2`` |float|                        outer diameter (excluding cover thickness)
   ``ts`` |float|                        single steel shim layer thickness
   ``tr`` |float|                        single rubber layer thickness
   ``n`` |int|                           number of rubber layers
   ``x1``  ``x2``  ``x3`` |float|        vector components in global coordinates defining local x-axis (optional)
   ``y1``  ``y2``  ``y3`` |float|        vector components in global coordinates defining local y-axis (optional)
   ``kc`` |float|                        cavitation parameter (optional, default = 10.0)
   ``PhiM`` |float|                      damage parameter (optional, default = 0.5)
   ``ac`` |float|                        strength reduction parameter (optional, default = 1.0)
   ``sDratio`` |float|                   shear distance from iNode as a fraction of the element length (optional, default = 0.5)
   ``m`` |float|                         element mass (optional, default = 0.0)
   ``cd`` |float|                        viscous damping parameter (optional, default = 0.0)
   ``tc`` |float|                        cover thickness (optional, default = 0.0)
   ``qL`` |float|                        density of lead (optional, default = 11200 kg/m3)
   ``cL`` |float|                        specific heat of lead (optional, default = 130 N-m/kg oC)
   ``kS`` |float|                        thermal conductivity of steel (optional, default = 50 W/m oC)
   ``aS`` |float|                        thermal diffusivity of steel (optional, default = 1.41e-05 m2/s)
   ``tag1`` |int|                        Tag to include cavitation and post-cavitation (optional, default = 0)
   ``tag2`` |int|                        Tag to include buckling load variation (optional, default = 0)
   ``tag3`` |int|                        Tag to include horizontal stiffness variation (optional, default = 0)
   ``tag4`` |int|                        Tag to include vertical stiffness variation (optional, default = 0)
   ``tag5`` |int|                        Tag to include strength degradation in shear due to heating of lead core (optional, default = 0)
   ===================================   ===========================================================================

.. note::

   Because default values of heating parameters are in SI units, user must override the default heating parameters values if using Imperial units

   User should distinguish between yield strength of elastomeric bearing (:math:`F_y`) and characteristic strength (:math:`Q_d`): :math:`Q_d=F_y*(1-alpha)`

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/LeadRubberX>`_
