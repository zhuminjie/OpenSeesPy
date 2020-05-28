.. include:: sub.txt

=============
 LoadControl
=============

.. function:: integrator('LoadControl',incr,numIter=1,minIncr=incr,maxIncr=incr)
   :noindex:

   Create a OpenSees LoadControl integrator object.

   ========================   =============================================================
   ``incr`` |float|           Load factor increment :math:`\lambda`.
   ``numIter`` |int|          Number of iterations the user would
		              like to occur in the solution algorithm. (optional)
   ``minIncr`` |float|        Min stepsize the user will allow :math:`\lambda_{min}`.
		              (optional)
   ``maxIncr`` |float|        Max stepsize the user will allow :math:`\lambda_{max}`.
		              (optional)
   ========================   =============================================================

   #. The change in applied loads that this causes depends on the active load pattern (those load pattern not set constant) and the loads in the load pattern. If the only active load acting on the Domain are in load pattern with a Linear time series with a factor of 1.0, this integrator is the same as the classical load control method.
   #. The optional arguments are supplied to speed up the step size in cases where convergence is too fast and slow down the step size in cases where convergence is too slow.
