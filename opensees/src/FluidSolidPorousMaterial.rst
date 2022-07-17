.. include:: sub.txt

============================
 FluidSolidPorousMaterial
============================

.. function:: nDMaterial('FluidSolidPorous', matTag, nd, soilMatTag, combinedBulkModul, pa=101.0)
   :noindex:

   FluidSolidPorous material couples the responses of two phases: fluid and solid. The fluid phase response is only volumetric and linear elastic. The solid phase can be any NDMaterial. This material is developed to simulate the response of saturated porous media under fully undrained condition.

   ================================   ===========================================================================
   ``matTag`` |int|                   integer tag identifying material
   ``nd`` |float|                     Number of dimensions, 2 for plane-strain, and 3 for 3D analysis.
   ``soilMatTag`` |int|               The material number for the solid phase material (previously defined).
   ``combinedBulkModul`` |float|      Combined undrained bulk modulus :math:`B_c`
                                      relating changes in pore pressure and volumetric
				      strain, may be approximated by:

				      :math:`B_c \approx B_f /n`

				      where :math:`B_f` is the bulk modulus of fluid
				      phase (2.2x106 kPa (or 3.191x105 psi) for water),
				      and :math:`n` the initial porosity.

   ``pa`` |float|                     Optional atmospheric pressure for
                                      normalization (typically 101 kPa in SI units,
				      or 14.65 psi in English units)
   ================================   ===========================================================================



See also `notes <http://opensees.berkeley.edu/wiki/index.php/FluidSolidPorousMaterial>`_
