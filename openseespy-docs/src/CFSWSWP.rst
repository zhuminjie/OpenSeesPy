.. include:: sub.txt

========================================================
CFSWSWP Wood-Sheathed Cold-Formed Steel Shear Wall Panel
========================================================

.. function:: uniaxialMaterial('CFSWSWP', matTag,height, width, fut, tf, Ife, Ifi, ts, np, ds, Vs, sc, nc, type, openingArea, openingLength)
   :noindex:

   This command is used to construct a uniaxialMaterial model that simulates the hysteresis response (Shear strength-Lateral displacement) of a wood-sheathed cold-formed steel shear wall panel (CFS-SWP). The hysteresis model has smooth curves and takes into account the strength and stiffness degradation, as well as pinching effect.

   This uniaxialMaterial gives results in Newton and Meter units, for strength and displacement, respectively.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``height`` |float|                    SWP's height (mm)
   ``width`` |float|                     SWP's width (mm)
   ``fut`` |float|                       Tensile strength of framing members (MPa)
   ``tf`` |float|                        Framing thickness (mm)
   ``Ife`` |float|                       Moment of inertia of the double end-stud (mm4)
   ``Ifi`` |float|                       Moment of inertia of the intermediate stud (mm4)
   ``ts`` |float|                        Sheathing thickness (mm)
   ``np`` |float|                        Sheathing number (one or two sides sheathed)
   ``ds`` |float|                        Screws diameter (mm)
   ``Vs`` |float|                        Screws shear strength (N)
   ``sc`` |float|                        Screw spacing on the SWP perimeter (mm)
   ``nc`` |float|                        Total number of screws located on the SWP perimeter
   ``type`` |int|                        Integer identifier used to define wood sheathing type (DFP=1, OSB=2, CSP=3)
   ``openingArea`` |float|               Total area of openings (mm2)
   ``openingLength`` |float|             Cumulative length of openings (mm)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/CFSWSWP>`_
