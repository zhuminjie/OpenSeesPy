.. include:: sub.txt

===================
 SAWS Material
===================

.. function:: uniaxialMaterial('SAWS', matTag, F0, FI, DU, S0, R1, R2, R3, R4, alpha, beta)
   :noindex:

   This file contains the class definition for SAWSMaterial. SAWSMaterial provides the implementation of a one-dimensional hysteretic model develeped as part of the CUREe Caltech wood frame project.

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``F0`` |float|                        Intercept strength of the shear wall spring element for the asymtotic line to the envelope curve F0 > FI > 0
   ``FI`` |float|                        Intercept strength of the spring element for the pinching branch of the hysteretic curve. (FI > 0).
   ``DU`` |float|                        Spring element displacement at ultimate load. (DU > 0).
   ``S0`` |float|                        Initial stiffness of the shear wall spring element (S0 > 0).
   ``R1`` |float|                        Stiffness ratio of the asymptotic line to the spring element envelope curve. The slope of this line is R1 S0. (0 < R1 < 1.0).
   ``R2`` |float|                        Stiffness ratio of the descending branch of the spring element envelope curve. The slope of this line is R2 S0. ( R2 < 0).
   ``R3`` |float|                        Stiffness ratio of the unloading branch off the spring element envelope curve. The slope of this line is R3 S0. ( R3 1).
   ``R4`` |float|                        Stiffness ratio of the pinching branch for the spring element. The slope of this line is R4 S0. ( R4 > 0).
   ``alpha`` |float|                     Stiffness degradation parameter for the shear wall spring element. (ALPHA > 0).
   ``beta`` |float|                      Stiffness degradation parameter for the spring element. (BETA > 0).
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SAWS_Material>`_
