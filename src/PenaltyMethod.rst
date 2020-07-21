.. include:: sub.txt

================
 Penalty Method
================

.. function:: constraints('Penalty',alphaS=1.0,alphaM=1.0)
   :noindex:

   This command is used to construct a Penalty constraint handler, which enforces the constraints using the penalty method. The following is the command to construct a penalty constraint handler:

   ================================   ===========================================================================
   ``alphaS`` |float|                 :math:`\alpha_S` factor on single points.
   ``alphaM`` |float|                 :math:`\alpha_M` factor on multi-points.
   ================================   ===========================================================================

.. note::

   The degree to which the constraints are enforced is dependent on the penalty values chosen. Problems can arise if these values are too small (constraint not enforced strongly enough) or too large (problems associated with conditioning of the system of equations).
