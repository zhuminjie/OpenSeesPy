.. include:: sub.txt

=========
 Steel02
=========

.. function:: uniaxialMaterial('Steel02', matTag, Fy, E0, b, *params, a1=a2*Fy/E0, a2=1.0, a3=a4*Fy/E0, a4=1.0, sigInit=0.0)
   :noindex:

   This command is used to construct a uniaxial Giuffre-Menegotto-Pinto steel material object with isotropic strain hardening.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``Fy`` |float|                     yield strength
   ``E0`` |float|                     initial elastic tangent
   ``b`` |float|                      strain-hardening ratio (ratio between post-yield
                                      tangent and initial elastic tangent)
   ``params`` |listf|                 parameters to control the transition from elastic to
                                      plastic branches.
				      ``params=[R0,cR1,cR2]``.
				      Recommended values: R0=between 10 and 20,
				      cR1=0.925, cR2=0.15
   ``a1`` |float|                     isotropic hardening parameter, increase of
                                      compression yield envelope as proportion of yield
                                      strength after a plastic strain of
                                      :math:`a_2*(F_y/E_0)` (optional)
   ``a2`` |float|                     isotropic hardening parameter
                                      (see explanation under ``a1``). (optional).
   ``a3`` |float|                     isotropic hardening parameter, increase of tension
                                      yield envelope as proportion of yield strength
                                      after a plastic strain
                                      of :math:`a_4*(F_y/E_0)`. (optional)
   ``a4`` |float|                     isotropic hardening parameter (see explanation
                                      under ``a3``). (optional)
   ``sigInit`` |float|                Initial Stress Value (optional, default: 0.0)
                                      the strain is calculated from ``epsP=sigInit/E``
				      ::

					 if (sigInit!= 0.0) {
					   double epsInit = sigInit/E;
				           eps = trialStrain+epsInit;
					 } else {
				           eps = trialStrain;
					 }
   ================================   ===========================================================================


.. seealso::

   `Steel02 <http://opensees.berkeley.edu/wiki/index.php/Steel02_Material_--_Giuffr%C3%A9-Menegotto-Pinto_Model_with_Isotropic_Strain_Hardening>`_
