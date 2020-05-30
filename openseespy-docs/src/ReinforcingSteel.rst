.. include:: sub.txt

==================
 ReinforcingSteel
==================

.. function:: uniaxialMaterial('ReinforcingSteel', matTag, fy, fu, Es, Esh, eps_sh, eps_ult, '-GABuck', lsr, beta, r, gamma, '-DMBuck', lsr, alpha=1.0, '-CMFatigue', Cf, alpha, Cd, '-IsoHard', a1=4.3, limit=1.0, '-MPCurveParams',R1=0.333,R2=18.0,R3=4.0)
   :noindex:

   This command is used to construct a ReinforcingSteel uniaxial material object. This object is intended to be used in a reinforced concrete fiber section as the steel reinforcing material.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fy`` |float|                        Yield stress in tension
   ``fu`` |float|                        Ultimate stress in tension
   ``Es`` |float|                        Initial elastic tangent
   ``Esh`` |float|                       Tangent at initial strain hardening
   ``eps_sh`` |float|                       Strain corresponding to initial strain hardening
   ``eps_ult`` |float|                      Strain at peak stress
   ``'-GABuck'`` |str|                   Buckling Model Based on Gomes and Appleton (1997)
   ``lsr`` |float|                       Slenderness Ratio
   ``beta`` |float|                      Amplification factor for the buckled stress strain curve.
   ``r`` |float|                         Buckling reduction factor

                                         r can be a real number between [0.0 and 1.0]

                                         r=1.0 full reduction (no buckling)

					 r=0.0 no reduction

					 0.0<r<1.0 linear interpolation between buckled and unbuckled curves
   ``gamma`` |float|                     Buckling constant
   ``'-DMBuck'`` |str|                   Buckling model based on Dhakal and Maekawa (2002)
   ``lsr`` |float|                       Slenderness Ratio
   ``alpha`` |float|                     Adjustment Constant usually between 0.75 and 1.0
                                         Default: alpha=1.0, this parameter is optional.
   ``'-CMFatigue'`` |str|                Coffin-Manson Fatigue and Strength Reduction
   ``Cf`` |float|                        Coffin-Manson constant C
   ``alpha`` |float|                     Coffin-Manson constant a
   ``Cd`` |float|                        Cyclic strength reduction constant
   ``'-IsoHard'`` |str|                  Isotropic Hardening / Diminishing Yield Plateau
   ``a1`` |float|                        Hardening constant (default = 4.3)
   ``limit`` |float|                     Limit for the reduction of the yield plateau.
                                         % of original plateau length to remain (0.01 < limit < 1.0 )
					 Limit =1.0, then no reduction takes place (default =0.01)
   ``'-MPCurveParams'`` |str|            Menegotto and Pinto Curve Parameters
   ``R1`` |float|                        (default = 0.333)
   ``R2`` |float|                        (default = 18)
   ``R3`` |float|                        (default = 4)
   ===================================   ===========================================================================



.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Reinforcing_Steel_Material>`_
