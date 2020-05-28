.. include:: sub.txt

===================
 Broyden Algorithm
===================

.. function:: algorithm('Broyden',secant=False,initial=False,count=10)
   :noindex:

   Create a Broyden algorithm for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
   ``count`` |int|                    Number of iterations. (optional)
   ================================   =============================================================
