.. include:: sub.txt

================
 Newmark Method
================

.. function:: integrator('Newmark',gamma,beta,'-form', form)
   :noindex:

   Create a Newmark integrator.

   ========================   =============================================================
   ``gamma`` |float|          :math:`\gamma` factor.
   ``beta`` |float|           :math:`\beta` factor.
   ``form`` |str|             Flag to indicate which variable to be used as primary
                              variable (optional)

                              * ``'D'`` -- displacement (default)
                              * ``'V'`` -- velocity
                              * ``'A'`` -- acceleration
   ========================   =============================================================

   #. If the accelerations are chosen as the unknowns and :math:`\beta` is chosen as 0, the formulation results in the fast but conditionally stable explicit Central Difference method. Otherwise the method is implicit and requires an iterative solution process.
   #. Two common sets of choices are

      #. Average Acceleration Method (:math:`\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{4}`)
      #. Linear Acceleration Method (:math:`\gamma=\tfrac{1}{2}, \beta = \tfrac{1}{6}`)

   #. :math:`\gamma > \tfrac{1}{2}` results in numerical damping proportional to :math:`\gamma - \tfrac{1}{2}`
   #. The method is second order accurate if and only if :math:`\gamma=\tfrac{1}{2}`
   #. The method is unconditionally stable for  :math:`\beta >= \frac{\gamma}{2} >= \tfrac{1}{4}`
