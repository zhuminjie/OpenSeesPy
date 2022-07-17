.. include:: sub.txt

===========================
 Modified Newton Algorithm
===========================

.. function:: algorithm('ModifiedNewton',secant=False,initial=False)
   :noindex:

   Create a ModifiedNewton algorithm. The difference to Newton is that the tangent at the initial guess is used in the iterations, instead of the current tangent.

   ================================   =============================================================
   ``secant`` |bool|                  Flag to indicate to use secant stiffness. (optional)
   ``initial`` |bool|                 Flag to indicate to use initial stiffness.(optional)
   ================================   =============================================================
