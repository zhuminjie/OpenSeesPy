.. include:: sub.txt

=========
 Steel4
=========

.. function:: uniaxialMaterial('Steel4', matTag, Fy, E0, '-asym', '-kin', b_k, *params, b_kc, R_0c, r_1c, r_2c, '-iso', b_i, rho_i, b_l, R_i, l_yp, b_ic, rho_ic, b_lc, R_ic, '-ult', f_u, R_u, f_uc, R_uc, '-init', sig_init, '-mem', cycNum)
   :noindex:


   This command is used to construct a general uniaxial material with combined kinematic and isotropic hardening and optional non-symmetric behavior.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``Fy`` |float|                        yield strength
   ``E0`` |float|                        initial elastic tangent
   ``'-kin'`` |str|                      apply kinematic hardening
   ``b_k`` |float|                       hardening ratio (E_k/E_0)
   ``params`` |listf|                    control the exponential transition from linear elastic to hardening asymptote
                                         ``params=[R_0,r_1,r_2]``.
                                         Recommended values: ``R_0 = 20, r_1 = 0.90, r_2 = 0.15``
   ``'-iso'`` |str|                      apply isotropic hardening
   ``b_i`` |float|                       initial hardening ratio (E_i/E_0)
   ``b_l`` |float|                       saturated hardening ratio (E_is/E_0)
   ``rho_i`` |float|                     specifies the position of the intersection point
                                         between initial and saturated hardening asymptotes
   ``R_i`` |float|                       control the exponential transition from initial
                                         to saturated asymptote
   ``l_yp`` |float|                      length of the yield plateau in eps_y0 = f_y / E_0 units
   ``'-ult'`` |str|                      apply an ultimate strength limit
   ``f_u`` |float|                       ultimate strength
   ``R_u`` |float|                       control the exponential transition from
                                         kinematic hardening to perfectly plastic asymptote
   ``'-asym'`` |str|                     assume non-symmetric behavior
   ``'-init'`` |str|                     apply initial stress
   ``sig_init`` |float|                  initial stress value
   ``'-mem'`` |str|                      configure the load history memory
   ``cycNum`` |float|                    expected number of half-cycles during the loading
                                         process
                                         Efficiency of the material can be slightly
					 increased by correctly setting this value.
					 The default value is ``cycNum = 50``
					 Load history memory can be turned off by
					 setting ``cycNum = 0``.
   ===================================   ===========================================================================

.. seealso::


   `Steel4 <http://opensees.berkeley.edu/wiki/index.php/Steel4_Material>`_
