.. include:: sub.txt

===================
 CastFuse Material
===================

.. function:: uniaxialMaterial('Cast', matTag, n, bo, h, fy, E, L, b, Ro, cR1, cR2, a1=s2*Pp/Kp, a2=1.0, a3=a4*Pp/Kp, a4=1.0)
   :noindex:

   This command is used to construct a parallel material object made up of an arbitrary number of previously-constructed UniaxialMaterial objects.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``n`` |int|                           Number of yield fingers of the CSF-brace
   ``bo`` |float|                        Width of an individual yielding finger at its base of the CSF-brace
   ``h`` |float|                         Thickness of an individual yielding finger
   ``fy`` |float|                        Yield strength of the steel material of the yielding finger
   ``E`` |float|                         Modulus of elasticity of the steel material of the yielding finger
   ``L`` |float|                         Height of an individual yielding finger
   ``b`` |float|                         Strain hardening ratio
   ``Ro`` |float|                        Parameter that controls the Bauschinger effect.
                                         Recommended Values for $Ro=between 10 to 30
   ``cR1`` |float|                       Parameter that controls the Bauschinger effect.
                                         Recommended Value cR1=0.925
   ``cR2`` |float|                       Parameter that controls the Bauschinger effect.
                                         Recommended Value cR2=0.150
   ``a1`` |float|                        isotropic hardening parameter, increase of
                                         compression yield envelope as proportion of yield
					 strength after a plastic deformation of a2*(Pp/Kp)
   ``a2`` |float|                        isotropic hardening parameter (see explanation
                                         under a1). (optional default = 1.0)
   ``a3`` |float|                        isotropic hardening parameter, increase of tension
                                         yield envelope as proportion of yield strength
					 after a plastic deformation of a4*(Pp/Kp)
   ``a4`` |float|                        isotropic hardening parameter (see explanation
                                         under a3). (optional default = 1.0)
   ===================================   ===========================================================================


Gray et al. [1] showed that the monotonic backbone curve of a CSF-brace with known properties (``n``, ``bo``, ``h``, ``L``, ``fy``, ``E``) after yielding can be expressed as a close-form solution that is given by,
:math:`P = P_p/\cos(2d/L)`, in which :math:`d` is the axial deformation of the brace at increment :math:`i` and :math:`P_p` is the yield strength of the CSF-brace and is given by the following expression

:math:`P_p = nb_oh^2f_y/4L`

The elastic stiffness of the CSF-brace is given by,

:math:`K_p = nb_oEh^3f_y/6L^3`

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/CastFuse_Material>`_
