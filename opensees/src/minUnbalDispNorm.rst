.. include:: sub.txt

======================================
 Minimum Unbalanced Displacement Norm
======================================

.. function:: integrator('MinUnbalDispNorm',dlambda1,Jd=1,minLambda=dlambda1,maxLambda=dlambda1,det=False)
   :noindex:

   Create a MinUnbalDispNorm integrator.

   ========================   ================================================================
   ``dlambda1`` |float|       First load increment (pseudo-time step) at the first
		              iteration in the next invocation of the analysis command.
   ``Jd`` |int|               Factor relating first load increment at subsequent
		              time steps. (optional)
   ``minLambda`` |float|      Min load increment. (optional)
   ``maxLambda`` |float|      Max load increment. (optional)
   ========================   ================================================================
