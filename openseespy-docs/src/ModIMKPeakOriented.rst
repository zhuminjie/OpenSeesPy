.. include:: sub.txt

============================================================================================================================
 Modified Ibarra-Medina-Krawinkler Deterioration Model with Peak-Oriented Hysteretic Response (ModIMKPeakOriented Material)
============================================================================================================================

.. function:: uniaxialMaterial('ModIMKPeakOriented', matTag, K0, as_Plus, as_Neg, My_Plus, My_Neg, Lamda_S, Lamda_C, Lamda_A, Lamda_K, c_S, c_C, c_A, c_K, theta_p_Plus, theta_p_Neg, theta_pc_Plus, theta_pc_Neg, Res_Pos, Res_Neg, theta_u_Plus, theta_u_Neg, D_Plus, D_Neg)
   :noindex:

   This command is used to construct a ModIMKPeakOriented material. This material simulates the modified Ibarra-Medina-Krawinkler deterioration model with peak-oriented hysteretic response. Note that the hysteretic response of this material has been calibrated with respect to 200 experimental data of RC beams in order to estimate the deterioration parameters of the model. This information was developed by Lignos and Krawinkler (2012). NOTE: before you use this material make sure that you have downloaded the latest OpenSees version. A youtube video presents a summary of this model including the way to be used within openSees `youtube link <http://youtu.be/YHBHQ-xuybE>`_.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``K0`` |float|                        elastic stiffness
   ``as_Plus`` |float|                   strain hardening ratio for positive loading direction
   ``as_Neg`` |float|                    strain hardening ratio for negative loading direction
   ``My_Plus`` |float|                   effective yield strength for positive loading direction
   ``My_Neg`` |float|                    effective yield strength for negative loading direction (negative value)
   ``Lamda_S`` |float|                   Cyclic deterioration parameter for strength deterioration [E_t=Lamda_S*M_y, see Lignos and Krawinkler (2011); set Lamda_S = 0 to disable this mode of deterioration]
   ``Lamda_C`` |float|                   Cyclic deterioration parameter for post-capping strength deterioration [E_t=Lamda_C*M_y, see Lignos and Krawinkler (2011); set Lamda_C = 0 to disable this mode of deterioration]
   ``Lamda_A`` |float|                   Cyclic deterioration parameter for accelerated reloading stiffness deterioration [E_t=Lamda_A*M_y, see Lignos and Krawinkler (2011); set Lamda_A = 0 to disable this mode of deterioration]
   ``Lamda_K`` |float|                   Cyclic deterioration parameter for unloading stiffness deterioration [E_t=Lamda_K*M_y, see Lignos and Krawinkler (2011); set Lamda_K = 0 to disable this mode of deterioration]
   ``c_S`` |float|                       rate of strength deterioration. The default value is 1.0.
   ``c_C`` |float|                       rate of post-capping strength deterioration. The default value is 1.0.
   ``c_A`` |float|                       rate of accelerated reloading deterioration. The default value is 1.0.
   ``c_K`` |float|                       rate of unloading stiffness deterioration. The default value is 1.0.
   ``theta_p_Plus`` |float|              pre-capping rotation for positive loading direction (often noted as plastic rotation capacity)
   ``theta_p_Neg`` |float|               pre-capping rotation for negative loading direction (often noted as plastic rotation capacity) (must be defined as a positive value)
   ``theta_pc_Plus`` |float|             post-capping rotation for positive loading direction
   ``theta_pc_Neg`` |float|              post-capping rotation for negative loading direction (must be defined as a positive value)
   ``Res_Pos`` |float|                   residual strength ratio for positive loading direction
   ``Res_Neg`` |float|                   residual strength ratio for negative loading direction (must be defined as a positive value)
   ``theta_u_Plus`` |float|              ultimate rotation capacity for positive loading direction
   ``theta_u_Neg`` |float|               ultimate rotation capacity for negative loading direction (must be defined as a positive value)
   ``D_Plus`` |float|                    rate of cyclic deterioration in the positive loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
   ``D_Neg`` |float|                     rate  of cyclic deterioration in the negative loading direction (this parameter is used to create assymetric hysteretic behavior for the case of a composite beam). For symmetric hysteretic response use 1.0.
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Modified_Ibarra-Medina-Krawinkler_Deterioration_Model_with_Peak-Oriented_Hysteretic_Response_(ModIMKPeakOriented_Material)>`_
