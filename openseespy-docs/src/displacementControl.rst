.. include:: sub.txt

=====================
 DisplacementControl
=====================

.. function:: integrator('DisplacementControl',nodeTag,dof,incr,numIter=1,dUmin=incr,dUmax=incr)
   :noindex:

   Create a DisplacementControl integrator.  In an analysis step with Displacement Control we seek to determine the time step that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.

   ========================   =============================================================
   ``nodeTag`` |int|               tag of node whose response controls solution
   ``dof`` |int|              Degree of freedom at the node,
		              1 through ndf.
   ``incr`` |float|           First displacement increment :math:`\Delta U_{dof}`.
   ``numIter`` |int|          Number of iterations the user would
		              like to occur in the solution algorithm. (optional)
   ``minIncr`` |float|        Min stepsize the user will allow :math:`\Delta U_{min}`.
		              (optional)
   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\Delta U_{max}`.
		              (optional)
   ========================   =============================================================
