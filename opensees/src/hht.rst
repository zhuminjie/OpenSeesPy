.. include:: sub.txt

=============================
 Hilber-Hughes-Taylor Method
=============================

.. function:: integrator('HHT',alpha,gamma=1.5-alpha,beta=(2-alpha)^2/4)
   :noindex:

   Create a Hilber-Hughes-Taylor (HHT) integrator. This is an implicit method that allows for energy dissipation and second order accuracy (which is not possible with the regular Newmark object). Depending on choices of input parameters, the method can be unconditionally stable.

   ========================   =============================================================
   ``alpha`` |float|          :math:`\alpha` factor.
   ``gamma`` |float|          :math:`\gamma` factor. (optional)
   ``beta`` |float|           :math:`\beta` factor. (optional)
   ========================   =============================================================

   #. Like Mewmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
   #. :math:`\alpha` = 1.0 corresponds to the Newmark method.
   #. :math:`\alpha` should be between 0.67 and 1.0. The smaller the :math:`\alpha` the greater the numerical damping.
   #. :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is second order accurate and unconditionally stable when :math:`\alpha` is :math:`\tfrac{2}{3} <= \alpha <= 1.0`. The defaults are:

      :math:`\beta = \frac{(2 - \alpha)^2}{4}`

      and

      :math:`\gamma = \frac{3}{2} - \alpha`
