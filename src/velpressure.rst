.. include:: sub.txt

==========================================
 Velocity and Pressure Dependent Friction
==========================================

.. function:: frictionModel('VelPressureDep',frnTag,muSlow,muFast0,A,deltaMu,alpha,transRate)
   :noindex:

   This command is used to construct a VelPressureDep friction model object.

   ================================   ===========================================================================
   ``frnTag`` |int|                   unique friction model tag
   ``muSlow`` |float|                 coefficient of friction at low velocity
   ``muFast0`` |float|                initial coefficient of friction at high velocity
   ``A`` |float|                      nominal contact area
   ``deltaMu`` |float|                pressure parameter calibrated from experimental data
   ``alpha`` |float|                  pressure parameter calibrated from experimental data
   ``transRate`` |float|              transition rate from low to high velocity
   ================================   ===========================================================================
