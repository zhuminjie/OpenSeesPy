.. include:: sub.txt

===================
Fatigue Material
===================

.. function:: uniaxialMaterial('Fatigue', matTag, otherTag, '-E0', E0=0.191, '-m', m=-0.458, '-min', min=-1e16, '-max', max=1e16)
   :noindex:

   The fatigue material uses a modified rainflow cycle counting algorithm to accumulate damage in a material using Miner's Rule. Element stress/strain relationships become zero when fatigue life is exhausted.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``otherTag`` |float|                  Unique material object integer tag for the material that is being wrapped
   ``E0`` |float|                        Value of strain at which one cycle will cause failure (default 0.191)
   ``m`` |float|                         Slope of Coffin-Manson curve in log-log space (default -0.458)
   ``min`` |float|                       Global minimum value for strain or deformation (default -1e16)
   ``max`` |float|                       Global maximum value for strain or deformation (default 1e16)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Fatigue_Material>`_
