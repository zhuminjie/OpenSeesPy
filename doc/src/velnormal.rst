.. include:: sub.txt

==============================================
 Velocity and Normal Force Dependent Friction
==============================================

.. function:: frictionModel('VelNormalFrcDep',frnTag,aSlow,nSlow,aFast,nFast,alpha0,alpha1,alpha2,maxMuFact)
   :noindex:

   This command is used to construct a VelNormalFrcDep friction model object.

   ================================   ===========================================================================
   ``frnTag`` |int|                   unique friction model tag
   ``aSlow`` |float|                  constant for coefficient of friction at low velocity
   ``nSlow`` |float|                  exponent for coefficient of friction at low velocity
   ``aFast`` |float|                  constant for coefficient of friction at high velocity
   ``nFast`` |float|                  exponent for coefficient of friction at high velocity
   ``alpha0`` |float|                 constant rate parameter coefficient
   ``alpha1`` |float|                 linear rate parameter coefficient
   ``alpha2`` |float|                 quadratic rate parameter coefficient
   ``maxMuFact`` |float|              factor for determining the maximum coefficient of friction. This value prevents the friction coefficient from exceeding an unrealistic maximum value when the normal force becomes very small. The maximum friction coefficient is determined from μFast, for example :math:`\mu \leq maxMuFac*μFast`.
   ================================   ===========================================================================
