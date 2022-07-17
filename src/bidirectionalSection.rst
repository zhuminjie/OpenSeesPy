.. include:: sub.txt

=======================
 Bidirectional Section
=======================

.. function:: section('Bidirectional',secTag,E_mod,Fy,Hiso,Hkin,code1='Vy',code2='P')
   :noindex:

   This command allows the user to construct a Bidirectional section, which is a stress-resultant plasticity model of two coupled forces. The yield surface is circular and there is combined isotropic and kinematic hardening.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``E_mod`` |float|                      elastic modulus
   ``Fy`` |float|                     yield force
   ``Hiso`` |float|                   isotropic hardening modulus
   ``Hkin`` |float|                   kinematic hardening modulus
   ``code1`` |str|                    section force code for direction 1 (optional)
   ``code2`` |str|                    section force code for direction 2 (optional)

                                      One of the following section
                                      code may be used:

                                      * ``'P'`` Axial force-deformation
				      * ``'Mz'`` Moment-curvature about section local z-axis
				      * ``'Vy'`` Shear force-deformation along section local y-axis
				      * ``'My'`` Moment-curvature about section local y-axis
				      * ``'Vz'`` Shear force-deformation along section local z-axis
				      * ``'T'`` Torsion Force-Deformation
   ================================   ===========================================================================
