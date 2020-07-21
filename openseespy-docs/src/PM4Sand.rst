.. include:: sub.txt

==================
 PM4Sand
==================

.. function:: nDMaterial('PM4Sand', matTag, D_r, G_o, h_po, Den, P_atm, h_o, e_max, e_min, n_b, n_d, A_do, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf, Q_bolt, R_bolt, m_par, F_sed, p_sed)
   :noindex:

   This command is used to construct a 2-dimensional PM4Sand material.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``D_r`` |float|                    Relative density, in fraction
   ``G_o`` |float|                    Shear modulus constant
   ``h_po`` |float|                   Contraction rate parameter
   ``Den`` |float|                    Mass density of the material
   ``P_atm`` |float|                  Optional, Atmospheric pressure
   ``h_o`` |float|                    Optional, Variable that adjusts the ratio of plastic modulus
                                      to elastic modulus
   ``e_max`` |float|                  Optional, Maximum and minimum void ratios
   ``e_min`` |float|                  Optional, Maximum and minimum void ratios
   ``n_b`` |float|                    Optional, Bounding surface parameter, :math:`n_b \ge 0`
   ``n_d`` |float|                    Optional, Dilatancy surface parameter :math:`n_d \ge 0`
   ``A_do`` |float|                   Optional, Dilatancy parameter, will be computed at the time
                                      of initialization if input value is negative
   ``z_max`` |float|                  Optional, Fabric-dilatancy tensor parameter
   ``c_z`` |float|                    Optional, Fabric-dilatancy tensor parameter
   ``c_e`` |float|                    Optional, Variable that adjusts the rate of strain accumulation
                                      in cyclic loading
   ``phi_cv`` |float|                 Optional, Critical state effective friction angle
   ``nu`` |float|                     Optional, Poisson's ratio
   ``g_degr`` |float|                 Optional, Variable that adjusts degradation of elastic modulus
                                      with accumulation of fabric
   ``c_dr`` |float|                   Optional, Variable that controls the rotated dilatancy surface
   ``c_kaf`` |float|                  Optional, Variable that controls the effect that sustained
                                      static shear stresses have on plastic modulus
   ``Q_bolt`` |float|                 Optional, Critical state line parameter
   ``R_bolt`` |float|                 Optional, Critical state line parameter
   ``m_par`` |float|                  Optional, Yield surface constant (radius of yield surface
                                      in stress ratio space)
   ``F_sed`` |float|                  Optional, Variable that controls the minimum value the
                                      reduction factor of the elastic moduli can get during reconsolidation
   ``p_sed`` |float|                  Optional, Mean effective stress up to which reconsolidation
                                      strains are enhanced
   ================================   ===========================================================================

The material formulations for the PM4Sand object are:

* ``'PlaneStrain'``

See als `here <http://opensees.berkeley.edu/wiki/index.php/PM4Sand_Material>`_


References

R.W.Boulanger, K.Ziotopoulou. "PM4Sand(Version 3.1): A Sand Plasticity Model for Earthquake Engineering Applications". Report No. UCD/CGM-17/01 2017
