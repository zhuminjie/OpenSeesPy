.. include:: sub.txt

======================================
Elastomeric Bearing (Bouc-Wen) Element
======================================

This command is used to construct an elastomericBearing element object, which is defined by two nodes. The element can have zero length or the appropriate bearing height. The bearing has unidirectional (2D) or coupled (3D) plasticity properties for the shear deformations, and force-deformation behaviors defined by UniaxialMaterials in the remaining two (2D) or four (3D) directions. By default (sDratio = 0.5) P-Delta moments are equally distributed to the two end-nodes. To avoid the introduction of artificial viscous damping in the isolation system (sometimes referred to as "damping leakage in the isolation system"), the bearing element does not contribute to the Rayleigh damping by default. If the element has non-zero length, the local x-axis is determined from the nodal geometry unless the optional x-axis vector is specified in which case the nodal geometry is ignored and the user-defined orientation is utilized.

.. function:: element('ElastomericBearingBoucWen', eleTag,*eleNodes,kInit, qd, alpha1, alpha2, mu, eta, beta, gamma, '-P', PMatTag, '-Mz', MzMatTag, <'-orient', *orientVals>, <'-shearDist', shearDist>, <'-doRayleigh'>, <'-mass', mass>)
   :noindex:

   For a two-dimensional problem

.. function:: element('ElastomericBearingBoucWen', eleTag,*eleNodes,kInit, qd, alpha1, alpha2, mu, eta, beta, gamma, '-P', PMatTag,'-T', TMatTag,'-My', MyMatTag,'-Mz', MzMatTag, <'-orient' ,*orientVals> ,<'-shearDist', shearDist> ,<'-doRayleigh'> ,<'-mass', mass>)
   :noindex:

   For a three-dimensional problem

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``kInit`` |float|                     initial elastic stiffness in local shear direction
   ``qd`` |float|                        characteristic strength
   ``alpha1`` |float|                    post yield stiffness ratio of linear hardening component
   ``alpha2`` |float|                    post yield stiffness ratio of non-linear hardening component
   ``mu`` |float|                        exponent of non-linear hardening component
   ``eta`` |float|                       yielding exponent (sharpness of hysteresis loop corners) (default = 1.0)
   ``beta`` |float|                      first hysteretic shape parameter (default = 0.5)
   ``gamma`` |float|                     second hysteretic shape parameter (default = 0.5)
   ``PMatTag``  |int|                    tag associated with previously-defined
                                         UniaxialMaterial in axial direction
   ``TMatTag``  |int|                    tag associated with previously-defined
                                         UniaxialMaterial in torsional direction
   ``MyMatTag``  |int|                   tag associated with previously-defined
                                         UniaxialMaterial in moment direction around local y-axis
   ``MzMatTag`` |int|                    tag associated with previously-defined UniaxialMaterial
                                         in moment direction around local z-axis
   ``orientVals`` |listi|                vector components in global coordinates
                                         defining local x-axis (optional),
                                         vector components in global coordinates defining
					 local y-axis (optional)
   ``shearDist`` |float|                 shear distance from iNode as a fraction
                                         of the element length (optional, default = 0.5)
   ``'-doRayleigh'`` |str|               to include Rayleigh damping from the
                                         bearing (optional, default = no Rayleigh damping
					 contribution)
   ``mass`` |float|                      element mass (optional, default = 0.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Elastomeric_Bearing_(Bouc-Wen)_Element>`_
