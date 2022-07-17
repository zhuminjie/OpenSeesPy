.. include:: sub.txt

==========================
 Generalized Alpha Method
==========================

.. function:: integrator('GeneralizedAlpha',alphaM,alphaF,gamma=0.5+alphaM-alphaF,beta=(1+alphaM-alphaF)^2/4)
   :noindex:

   Create a GeneralizedAlpha integrator. This is an implicit method that like the HHT method allows for high frequency energy dissipation and second order accuracy, i.e. :math:`\Delta t^2`. Depending on choices of input parameters, the method can be unconditionally stable.

   ========================   =============================================================
   ``alphaM`` |float|         :math:`\alpha_M` factor.
   ``alphaF`` |float|         :math:`\alpha_F` factor.
   ``gamma`` |float|          :math:`\gamma` factor. (optional)
   ``beta`` |float|           :math:`\beta` factor. (optional)
   ========================   =============================================================

   #. Like Newmark and all the implicit schemes, the unconditional stability of this method applies to linear problems. There are no results showing stability of this method over the wide range of nonlinear problems that potentially exist. Experience indicates that the time step for implicit schemes in nonlinear situations can be much greater than those for explicit schemes.
   #. :math:`\alpha_M` = 1.0, :math:`\alpha_F` = 1.0 produces the Newmark Method.
   #. :math:`\alpha_M` = 1.0 corresponds to the :meth:`integrator.HHT` method.
   #. The method is second-order accurate provided :math:`\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F`
   #. The method is unconditionally stable provided :math:`\alpha_M >= \alpha_F >= \tfrac{1}{2}, \beta>=\tfrac{1}{4} +\tfrac{1}{2}(\gamma_M - \gamma_F)`
   #. :math:`\gamma` and :math:`\beta` are optional. The default values ensure the method is unconditionally stable, second order accurate and high frequency dissipation is maximized.

      The defaults are:

      :math:`\gamma = \tfrac{1}{2} + \alpha_M - \alpha_F`

      and

      :math:`\beta = \tfrac{1}{4}(1 + \alpha_M - \alpha_F)^2`
