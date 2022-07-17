.. include:: sub.txt

====================
 Section Aggregator
====================

.. function:: section('Aggregator',secTag,*mats,'-section',sectionTag)
   :noindex:

   This command is used to construct a SectionAggregator object which aggregates groups previously-defined UniaxialMaterial objects into a single section force-deformation model. Each UniaxialMaterial object represents the section force-deformation response for a particular section degree-of-freedom (dof). There is no interaction between responses in different dof directions. The aggregation can include one previously defined section.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``mats`` |list|                    list of tags and dofs of previously-defined
                                      UniaxialMaterial objects,
                                      ``mats = [matTag1,dof1,matTag2,dof2,...]``

                                      the force-deformation quantity to be modeled by
                                      this section object. One of the following section
                                      dof may be used:

				      * ``'P'`` Axial force-deformation
				      * ``'Mz'`` Moment-curvature about section local z-axis
				      * ``'Vy'`` Shear force-deformation along section local y-axis
				      * ``'My'`` Moment-curvature about section local y-axis
				      * ``'Vz'`` Shear force-deformation along section local z-axis
				      * ``'T'`` Torsion Force-Deformation
   ``sectionTag`` |int|               tag of previously-defined Section object to which the UniaxialMaterial objects are aggregated as additional force-deformation relationships (optional)
   ================================   ===========================================================================
