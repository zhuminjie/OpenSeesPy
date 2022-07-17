.. include:: sub.txt

==================
 SteelMPF
==================

.. function:: uniaxialMaterial('SteelMPF', matTag, fyp, fyn, E0, bp, bn, *params, a1=0.0, a2=1.0, a3=0.0, a4=1.0)
   :noindex:

   This command is used to construct a uniaxialMaterial SteelMPF (Kolozvari et al., 2015), which represents the well-known uniaxial constitutive nonlinear hysteretic material model for steel proposed by Menegotto and Pinto (1973), and extended by Filippou et al. (1983) to include isotropic strain hardening effects.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fyp`` |float|                       Yield strength in tension (positive loading direction)
   ``fyn`` |float|                       Yield strength in compression (negative loading direction)
   ``E0`` |float|                        Initial tangent modulus
   ``bp`` |float|                        Strain hardening ratio in tension (positive loading direction)
   ``bn`` |float|                        Strain hardening ratio in compression (negative loading direction)
   ``params`` |listf|                    parameters to control the transition from elastic to plastic branches.
                                         ``params=[R0,cR1,cR2]``.
                                         Recommended values: ``R0=20``, ``cR1=0.925``, ``cR2=0.15`` or ``cR2=0.0015``
   ``a1`` |float|                        Isotropic hardening in compression parameter (optional, default = 0.0). Shifts compression
                                         yield envelope by a proportion of compressive yield strength after a maximum plastic tensile
					 strain of a2(fyp/E0)
   ``a2`` |float|                        Isotropic hardening in compression parameter (optional, default = 1.0).
   ``a3`` |float|                        Isotropic hardening in tension parameter (optional, default = 0.0). Shifts tension yield
                                         envelope by a proportion of tensile yield strength after a maximum plastic compressive
					 strain of a3(fyn/E0).
   ``a4`` |float|                        Isotropic hardening in tension parameter (optional, default = 1.0). See explanation of a3.
   ===================================   ===========================================================================



.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SteelMPF_-_Menegotto_and_Pinto_(1973)_Model_Extended_by_Filippou_et_al._(1983)>`_
