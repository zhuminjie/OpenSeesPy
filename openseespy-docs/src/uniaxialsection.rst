.. include:: sub.txt

==================
 Uniaxial Section
==================

.. function:: section('Uniaxial',secTag,matTag,quantity)
   :noindex:

   This command is used to construct a UniaxialSection object which uses a previously-defined UniaxialMaterial object to represent a single section force-deformation response quantity.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``matTag`` |int|                   tag of uniaxial material
   ``quantity`` |str|                 the force-deformation quantity to be modeled by
                                      this section object. One of the following section
                                      dof may be used:

				      * ``'P'`` Axial force-deformation
				      * ``'Mz'`` Moment-curvature about section local z-axis
				      * ``'Vy'`` Shear force-deformation along section local y-axis
				      * ``'My'`` Moment-curvature about section local y-axis
				      * ``'Vz'`` Shear force-deformation along section local z-axis
				      * ``'T'`` Torsion Force-Deformation
   ================================   ===========================================================================
