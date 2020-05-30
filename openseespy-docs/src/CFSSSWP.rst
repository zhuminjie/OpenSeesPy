.. include:: sub.txt

=========================================================
CFSSSWP Steel-Sheathed Cold-formed Steel Shear Wall Panel
=========================================================

.. function:: uniaxialMaterial('CFSSSWP', matTag,height, width, fuf, fyf, tf, Af, fus, fys, ts, np, ds, Vs, sc, dt, openingArea, openingLength)
   :noindex:

   This command is used to construct a uniaxialMaterial model that simulates the hysteresis response (Shear strength-lateral Displacement) of a Steel-Sheathed Cold-Formed Steel Shear Wall Panel (CFS-SWP). The hysteresis model has smooth curves and takes into account the strength and stiffness degradation, as well as pinching effect.

   This uniaxialMaterial gives results in Newton and Meter units, for strength and displacement, respectively.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``height`` |float|                    SWP's height (mm)
   ``width`` |float|                     SWP's width (mm)
   ``fuf`` |float|                       Tensile strength of framing members (MPa)
   ``fyf`` |float|                       Yield strength of framing members (MPa)
   ``tf`` |float|                        Framing thickness (mm)
   ``Af`` |float|                        Framing cross section area (mm2)
   ``fus`` |float|                       Tensile strength of steel sheet sheathing (MPa)
   ``fys`` |float|                       Yield strength of steel sheet sheathing (MPa)
   ``ts`` |float|                        Sheathing thickness (mm)
   ``np`` |float|                        Sheathing number (one or two sides sheathed)
   ``ds`` |float|                        Screws diameter (mm)
   ``Vs`` |float|                        Screws shear strength (N)
   ``sc`` |float|                        Screw spacing on the SWP perimeter (mm)
   ``dt`` |float|                        Anchor bolt's diameter (mm)
   ``openingArea`` |float|               Total area of openings (mm2)
   ``openingLength`` |float|             Cumulative length of openings (mm)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/CFSSSWP>`_
