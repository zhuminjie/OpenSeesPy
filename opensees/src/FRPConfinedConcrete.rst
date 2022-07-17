.. include:: sub.txt

=====================
 FRPConfinedConcrete
=====================

.. function:: uniaxialMaterial('FRPConfinedConcrete', matTag, fpc1, fpc2, epsc0, D, c, Ej, Sj, tj, eju, S, fyl, fyh, dlong, dtrans, Es, nu0, k, useBuck)
   :noindex:

   This command is used to construct a uniaxial Megalooikonomou-Monti-Santini concrete material object with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fpc1`` |float|                      concrete core compressive strength.
   ``fpc2`` |float|                      concrete cover compressive strength.
   ``epsc0`` |float|                     strain corresponding to unconfined concrete strength.
   ``D`` |float|                         diameter of the circular section.
   ``c`` |float|                         dimension of concrete cover (until the outer edge of steel stirrups)
   ``Ej`` |float|                        elastic modulus of the fiber reinforced polymer (FRP) jacket.
   ``Sj`` |float|                        clear spacing of the FRP strips - zero if FRP jacket is continuous.
   ``tj`` |float|                        total thickness of the FRP jacket.
   ``eju`` |float|                       rupture strain of the FRP jacket from tensile coupons.
   ``S`` |float|                         spacing of the steel spiral/stirrups.
   ``fyl`` |float|  	                   yielding strength of longitudinal steel bars.
   ``fyh`` |float|                       yielding strength of the steel spiral/stirrups.
   ``dlong`` |float|                     diameter of the longitudinal bars of the circular section.
   ``dtrans`` |float|                    diameter of the steel spiral/stirrups.
   ``Es`` |float|                        elastic modulus of steel.
   ``nu0`` |float|                       initial Poisson's coefficient for concrete.
   ``k`` |float|                         reduction factor for the rupture strain of the FRP
                                         jacket, recommended values 0.5-0.8.
   ``useBuck`` |float|                   FRP jacket failure criterion due to buckling of longitudinal compressive steel bars (0 = not                                            include it, 1= to include it).
   ===================================   ===========================================================================

.. note::
   #.IMPORTANT: The units of the input parameters should be in MPa, N, mm.
   #.Concrete compressive strengths and the corresponding strain should be input as positive values.
   #.When rupture of FRP jacket occurs due to dilation of concrete (lateral concrete strain exceeding reduced rupture strain of FRP          jacket), the analysis is not terminated. Only a message "FRP Rupture" is plotted on the screen.
   #.When $useBuck input parameter is on (equal to 1) and the model's longitudinal steel buckling conditions are fulfilled, a message        "Initiation of Buckling of Long.Bar under Compression" is plotted on the screen.
   #.When rupture of FRP jacket occurs due to its interaction with buckled longitudinal compressive steel bars, the analysis is not          terminated. Only a message "FRP Rupture due to Buckling of Long.Bar under compression" is plotted on the screen.

.. seealso::

   `Notes <http://opensees.berkeley.edu/wiki/index.php/FRPConfinedConcrete>`_
