.. include:: sub.txt

======================
 Lagrange Multipliers
======================

.. function:: constraints('Lagrange',alphaS=1.0,alphaM=1.0)
   :noindex:

   This command is used to construct a LagrangeMultiplier constraint handler, which enforces the constraints by introducing Lagrange multiplies to the system of equation. The following is the command to construct a plain constraint handler:

   ================================   ===========================================================================
   ``alphaS`` |float|                 :math:`\alpha_S` factor on single points.
   ``alphaM`` |float|                 :math:`\alpha_M` factor on multi-points.
   ================================   ===========================================================================

.. note::

   The Lagrange multiplier method introduces new unknowns to the system of equations. The diagonal part of the system corresponding to these new unknowns is 0.0. This ensure that the system IS NOT symmetric positive definite.
