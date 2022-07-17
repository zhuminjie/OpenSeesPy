.. include:: sub.txt

===========================================
Engineered Cementitious Composites Material
===========================================

.. function:: uniaxialMaterial('ECC01', matTag, sigt0, epst0, sigt1, epst1, epst2, sigc0, epsc0, epsc1, alphaT1, alphaT2, alphaC, alphaCU, betaT, betaC)
   :noindex:

   This command is used to construct a uniaxial Engineered Cementitious Composites (ECC)material object based on the ECC material model of Han, et al. (see references). Reloading in tension and compression is linear.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``sigt0`` |float|                     tensile cracking stress
   ``epst0`` |float|                     strain at tensile cracking stress
   ``sigt1`` |float|                     peak tensile stress
   ``epst1`` |float|                     strain at peak tensile stress
   ``epst2`` |float|                     ultimate tensile strain
   ``sigc0`` |float|                     compressive strength (see NOTES)
   ``epsc0`` |float|                     strain at compressive strength (see NOTES)
   ``epsc1`` |float|                     ultimate compressive strain (see NOTES)
   ``alphaT1`` |float|                   exponent of the unloading curve in tensile strain hardening region
   ``alphaT2`` |float|                   exponent of the unloading curve in tensile softening region
   ``alphaC`` |float|                    exponent of the unloading curve in the compressive softening
   ``alphaCU`` |float|                   exponent of the compressive softening curve (use 1 for linear softening)
   ``betaT`` |float|                     parameter to determine permanent strain in tension
   ``betaC`` |float|                     parameter to determine permanent strain in compression
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Engineered_Cementitious_Composites_Material>`_
