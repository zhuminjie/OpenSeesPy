.. include:: sub.txt

==================
 Newton Algorithm
==================

.. function:: algorithm('Newton',secant=False,initial=False,initialThenCurrent=False)
   :noindex:

   Create a Newton-Raphson algorithm. The Newton-Raphson method is the most widely used and most robust method for solving nonlinear algebraic equations.

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
   ``initialThenCurrent`` |bool|      Flag to indicate to use initial stiffness
		                      on first step, then use current stiffness
                                      for subsequent steps. (optional)
   ================================   =============================================================
