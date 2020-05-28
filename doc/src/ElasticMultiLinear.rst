.. include:: sub.txt

===========================
ElasticMultiLinear Material
===========================

.. function:: uniaxialMaterial('ElasticMultiLinear', matTag, eta=0.0, '-strain', *strain, '-stress', *stress)
   :noindex:


   This command is used to construct a multi-linear elastic uniaxial material object. The nonlinear stress-strain relationship is given by a multi-linear curve that is define by a set of points. The behavior is nonlinear but it is elastic. This means that the material loads and unloads along the same curve, and no energy is dissipated. The slope given by the last two specified points on the positive strain axis is extrapolated to infinite positive strain. Similarly, the slope given by the last two specified points on the negative strain axis is extrapolated to infinite negative strain. The number of provided strain points needs to be equal to the number of provided stress points.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``eta`` |float|                       damping tangent (optional, default=0.0)
   ``strain`` |listf|                    list of strain points along stress-strain curve
   ``stress`` |listf|                    list of stress points along stress-strain curve
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ElasticMultiLinear_Material>`_
