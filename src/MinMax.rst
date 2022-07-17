.. include:: sub.txt

===================
MinMax Material
===================

.. function:: uniaxialMaterial('MinMax', matTag, otherTag, '-min', minStrain=1e-16, '-max', maxStrain=1e16)
   :noindex:


   This command is used to construct a MinMax material object. This stress-strain behaviour for this material is provided by another material. If however the strain ever falls below or above certain threshold values, the other material is assumed to have failed. From that point on, values of 0.0 are returned for the tangent and stress.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``otherTag`` |float|                  tag of the other material
   ``minStrain`` |float|                 minimum value of strain. optional default = -1.0e16.
   ``maxStrain`` |float|                 max value of strain. optional default = 1.0e16.
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/MinMax_Material>`_
