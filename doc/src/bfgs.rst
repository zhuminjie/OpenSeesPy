.. include:: sub.txt

================
 BFGS Algorithm
================

.. function:: algorithm('BFGS',secant=False,initial=False,count=10)
   :noindex:

   Create a BFGS algorithm.  The BFGS method is one of the most effective matrix-update or quasi Newton methods for iteration on a nonlinear system of equations. The method computes new search directions at each iteration step based on the initial jacobian, and subsequent trial solutions. The unlike regular Newton does not require the tangent matrix be reformulated and refactored at every iteration, however unlike ModifiedNewton it does not rely on the tangent matrix from a previous iteration.

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
   ``count`` |int|                    Number of iterations. (optional)
   ================================   =============================================================
