.. include:: sub.txt

===============================
 Pinching Limit State Material
===============================

This command is used to construct a uniaxial material that simulates a pinched load-deformation response and exhibits degradation under cyclic loading. This material works with the RotationShearCurve limit surface that can monitor a key deformation and/or a key force in an associated frame element and trigger a degrading behavior in this material when a limiting value of the deformation and/or force are reached. The material can be used in two modes: 1) direct input mode, where pinching and damage parameters are directly input; and 2) calibrated mode for shear-critical concrete columns, where only key column properties are input for model to fully define pinching and damage parameters.

.. function:: uniaxialMaterial('PinchingLimitStateMaterial', matTag,nodeT, nodeB, driftAxis, Kelas, crvTyp, crvTag, YpinchUPN, YpinchRPN, XpinchRPN, YpinchUNP, YpinchRNP, XpinchRNP, dmgStrsLimE, dmgDispMax, dmgE1, dmgE2, dmgE3, dmgE4, dmgELim, dmgR1, dmgR2, dmgR3, dmgR4, dmgRLim, dmgRCyc, dmgS1, dmgS2, dmgS3, dmgS4, dmgSLim, dmgSCyc)
   :noindex:

   MODE 1: Direct Input

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``nodeT`` |int|                       integer node tag to define the first node at the extreme end of the associated flexural frame member (L3 or D5 in Figure)
   ``nodeB`` |int|                       integer node tag to define the last node at the extreme end of the associated flexural frame member (L2 or D2 in Figure)
   ``driftAxis`` |int|                   integer to indicate the drift axis in which lateral-strength degradation will occur. This axis should be orthogonal to the axis of measured rotation (see    ``rotAxis`` in Rotation Shear Curve definition)

                                         ``driftAxis`` = 1 - Drift along the x-axis
					 ``driftAxis`` = 2 - Drift along the y-axis
					 ``driftAxis`` = 3 - Drift along the z-axis
   ``Kelas`` |float|                     floating point value to define the initial material elastic stiffness (Kelastic); Kelas > 0
   ``crvTyp`` |int|                      integer flag to indicate the type of limit curve associated with this material.

                                         ``crvTyp`` = 0 - No limit curve
					 ``crvTyp`` = 1 - axial limit curve
					 ``crvTyp`` = 2 - RotationShearCurve
   ``crvTag`` |int|                      integer tag for the unique limit curve object associated with this material
   ``YpinchUPN`` |float|                 floating point unloading force pinching factor for loading in the negative direction. **Note: This value must be between zero and unity**
   ``YpinchRPN`` |float|                 floating point reloading force pinching factor for loading in the negative direction. **Note: This value must be between negative one and unity**
   ``XpinchRPN`` |float|                 floating point reloading displacement pinching factor for loading in the negative direction. **Note: This value must be between negative one and unity**
   ``YpinchUNP`` |float|                 floating point unloading force pinching factor for loading in the positive direction. **Note: This value must be between zero and unity**
   ``YpinchRNP`` |float|                 floating point reloading force pinching factor for loading in the positive direction. **Note: This value must be between negative one and unity**
   ``XpinchRNP`` |float|                 floating point reloading displacement pinching factor for loading in the positive direction. **Note: This value must be between negative one and unity**
   ``dmgStrsLimE`` |float|               floating point force limit for elastic stiffness damage (typically defined as the lowest of shear strength or shear at flexrual yielding).
                                         This value is used to compute the maximum deformation at flexural yield (δmax Eq. 1) and using the initial elastic stiffness (Kelastic) the monotonic energy (Emono Eq. 1) to yield. Input 1 if this type of damage is not required and set    ``dmgE1``,    ``dmgE2``,    ``dmgE3``,    ``dmgE4``, and    ``dmgELim`` to zero
   ``dmgDispMax`` |float|                floating point for ultimate drift at failure (δmax Eq. 1) and is used for strength and stiffness damage.
                                         This value is used to compute the monotonic energy at axial failure (Emono Eq. 2) by computing the area under the backbone in the positive loading direction up to δmax. Input 1 if this type of damage is not required and set    ``dmgR1``,    ``dmgR2``,    ``dmgR3``,    ``dmgR4``, and    ``dmgRLim`` to zero for reloading stiffness damage. Similarly set    ``dmgS1``,    ``dmgS2``,    ``dmgS3``,    ``dmgS4``, and    ``dmgSLim`` to zero if reloading strength damage is not required
   ``dmgE1``  ``dmgE2`` |float|          floating point elastic stiffness damage factors α1,α2,α3,α4 shown in Eq. 1
   ``dmgE3``  ``dmgE4`` |float|          floating point elastic stiffness damage factors α1,α2,α3,α4 shown in Eq. 1
   ``dmgELim`` |float|                   floating point elastic stiffness damage limit Dlim shown in Eq. 1; **Note: This value must be between zero and unity**
   ``dmgR1``    ``dmgR2`` |float|        floating point reloading stiffness damage factors α1,α2,α3,α4 shown in Eq. 1
   ``dmgR3``    ``dmgR4`` |float|        floating point reloading stiffness damage factors α1,α2,α3,α4 shown in Eq. 1
   ``dmgRLim`` |float|                   floating point reloading stiffness damage limit Dlim shown in Eq. 1; **Note: This value must be between zero and unity**
   ``dmgRCyc`` |float|                   floating point cyclic reloading stiffness damage index; **Note: This value must be between zero and unity**
   ``dmgS1``    ``dmgS2`` |float|        floating point backbone strength damage factors α1,α2,α3,α4 shown in Eq. 1
   ``dmgS3``    ``dmgS4`` |float|        floating point backbone strength damage factors α1,α2,α3,α4 shown in Eq. 1
   ``dmgSLim`` |float|                   floating point backbone strength damage limit Dlim shown in Eq. 1; **Note: This value must be between zero and unity**
   ``dmgSCyc`` |float|                   floating point cyclic backbone strength damage index; **Note: This value must be between zero and unity**
   ===================================   ===========================================================================

.. function:: uniaxialMaterial('PinchingLimitStateMaterial', matTag,dnodeT, nodeB, driftAxis, Kelas, crvTyp, crvTag, eleTag, b, d, h, a, st, As, Acc, ld, db, rhot, fc, fy, fyt)
   :noindex:

   MODE 2: Calibrated Model for Shear-Critical Concrete Columns

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``nodeT`` |int|                       integer node tag to define the first node at the extreme end of the associated flexural frame member (L3 or D5 in Figure)
   ``nodeB`` |int|                       integer node tag to define the last node at the extreme end of the associated flexural frame member (L2 or D2 in Figure)
   ``driftAxis`` |int|                   integer to indicate the drift axis in which lateral-strength degradation will occur. This axis should be orthogonal to the axis of measured rotation (see    ``rotAxis``` in Rotation Shear Curve definition)

                                         ``driftAxis`` = 1 - Drift along the x-axis
					 ``driftAxis`` = 2 - Drift along the y-axis
					 ``driftAxis`` = 3 - Drift along the z-axis

   ``Kelas`` |float|                     floating point value to define the shear stiffness (Kelastic) of the shear spring prior to shear failure

                                         ``Kelas`` = -4 - Shear stiffness calculated assuming double curvature and shear springs at both column element ends

					 ``Kelas`` = -3 - Shear stiffness calculated assuming double curvature and a shear spring at one column element end

					 ``Kelas`` = -2 - Shear stiffness calculated assuming single curvature and shear springs at both column element ends

					 ``Kelas`` = -1 - Shear stiffness calculated assuming single curvature and a shear spring at one column element end

					 ``Kelas`` > 0 - Shear stiffness is the input value

					 Note: integer inputs allow the model to know whether column height equals the shear span (cantelever) or twice the shear span (double curvature). For columns in frames, input the value for the case that best approximates column end conditions or manually input shear stiffness (typically double curvature better estimates framed column behavior)
   ``crvTag`` |int|                      integer tag for the unique limit curve object associated with this material
   ``eleTag`` |int|                      integer element tag to define the associated beam-column element used to extract axial load
   ``b`` |float|                         floating point column width (inches)
   ``d`` |float|                         floating point column depth (inches)
   ``h`` |float|                         floating point column height (inches)
   ``a`` |float|                         floating point shear span length (inches)
   ``st`` |float|                        floating point transverse reinforcement spacing (inches) along column height
   ``As`` |float|                        floating point total area (inches squared) of longitudinal steel bars in section
   ``Acc`` |float|                       floating point gross confined concrete area (inches squared) bounded by the transverse reinforcement in column section
   ``ld`` |float|                        floating point development length (inches) of longitudinal bars using ACI 318-11 Eq. 12-1 and Eq. 12-2
   ``db`` |float|                        floating point diameter (inches) of longitudinal bars in column section
   ``rhot`` |float|                      floating point transverse reinforcement ratio (Ast/st.db)
   ``f'c`` |float|                       floating point concrete compressive strength (ksi)
   ``fy`` |float|                        floating point longitudinal steel yield strength (ksi)
   ``fyt`` |float|                       floating point transverse steel yield strength (ksi)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Pinching_Limit_State_Material>`_
