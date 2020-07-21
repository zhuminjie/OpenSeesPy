.. include:: sub.txt

=========================
 PlaneStressUserMaterial
=========================

.. function:: nDMaterial('PlaneStressUserMaterial', matTag, nstatevs, nprops, fc, ft, fcu, epsc0, epscu, epstu, stc)
   :noindex:

   This command is used to create the multi-dimensional concrete material model that is based on the damage mechanism and smeared crack model.

   ================================   ===========================================================================
   ``nstatevs`` |int|                 number of state/history variables (usually 40)
   ``nprops`` |int|                   number of material properties (usually 7)
   ``matTag`` |int|                   integer tag identifying material
   ``fc`` |float|                     concrete compressive strength at 28 days (positive)
   ``ft`` |float|                     concrete tensile strength (positive)
   ``fcu`` |float|                    concrete crushing strength (negative)
   ``epsc0`` |float|                  concrete strain at maximum strength (negative)
   ``epscu`` |float|                  concrete strain at crushing strength (negative)
   ``epstu`` |float|                  ultimate tensile strain (positive)
   ``stc`` |float|                    shear retention factor
   ================================   ===========================================================================
