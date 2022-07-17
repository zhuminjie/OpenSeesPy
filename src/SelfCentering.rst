.. include:: sub.txt

=============================
SelfCentering Material
=============================

.. function:: uniaxialMaterial('SelfCentering', matTag, k1, k2, sigAct, beta, epsSlip=0, epsBear=0, rBear=k1)
   :noindex:

   This command is used to construct a uniaxial self-centering (flag-shaped) material object with optional non-recoverable slip behaviour and an optional stiffness increase at high strains (bearing behaviour).

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``k1`` |float|                        Initial Stiffness
   ``k2`` |float|                        Post-Activation Stiffness (0<   ``k2``<   ``k1``)
   ``sigAct`` |float|                    Forward Activation Stress/Force
   ``beta`` |float|                      Ratio of Forward to Reverse Activation Stress/Force
   ``epsSlip`` |float|                   slip Strain/Deformation (if    ``epsSlip`` = 0, there will be no slippage)
   ``epsBear`` |float|                   Bearing Strain/Deformation (if    ``epsBear`` = 0, there will be no bearing)
   ``rBear`` |float|                     Ratio of Bearing Stiffness to Initial Stiffness    ``k1``
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/SelfCentering_Material>`_
