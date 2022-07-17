.. include:: sub.txt

=============================
 Velocity Dependent Friction
=============================

.. function:: frictionModel('VelDependent',frnTag,muSlow,muFast,transRate)
   :noindex:

   This command is used to construct a VelDependent friction model object. It is useful for modeling the behavior of `PTFE <http://en.wikipedia.org/wiki/Polytetrafluoroethylene>`_ or PTFE-like materials sliding on a stainless steel surface. For a detailed presentation on the velocity dependence of such interfaces please refer to Constantinou et al. (1999).

   ================================   ===========================================================================
   ``frnTag`` |int|                   unique friction model tag
   ``muSlow`` |float|                 coefficient of friction at low velocity
   ``muFast`` |float|                 coefficient of friction at high velocity
   ``transRate`` |float|              transition rate from low to high velocity
   ================================   ===========================================================================

.. math::

   \mu = {\mu _{fast}} - \left( {{\mu _{fast}} - {\mu _{slow}}} \right) \cdot {e^{ - transRate\, \cdot \,\left| v \right|}}

REFERENCE:

Constantinou, M.C., Tsopelas, P., Kasalanati, A., and Wolff, E.D. (1999). "Property modification factors for seismic isolation bearings". Report MCEER-99-0012, Multidisciplinary Center for Earthquake Engineering Research, State University of New York.
