.. include:: sub.txt

==================
 rayleigh command
==================

.. function:: rayleigh(alphaM, betaK, betaKinit, betaKcomm)

   This command is used to assign damping to all previously-defined elements and nodes. When using rayleigh damping in OpenSees, the damping matrix for an element or node, D is specified as a combination of stiffness and mass-proportional damping matrices:

   .. math::

      D = \alpha_M * M + \beta_K * K_{curr} + \beta_{Kinit} * K_{init} + \beta_{Kcomm} * K_{commit}

   ========================   =============================================================
   ``alphaM`` |float|         factor applied to elements or nodes mass matrix
   ``betaK`` |float|          factor applied to elements current stiffness matrix.
   ``betaKinit`` |float|      factor applied to elements initial stiffness matrix.
   ``betaKcomm`` |float|      factor applied to elements committed stiffness matrix.
   ========================   =============================================================
