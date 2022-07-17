.. include:: sub.txt

==========================================
 Multi-Linear Velocity Dependent Friction
==========================================

.. function:: frictionModel('VelDepMultiLinear',frnTag,'-vel',*velPoints,'-frn',*frnPoints)
   :noindex:

   This command is used to construct a VelDepMultiLinear friction model object. The friction-velocity relationship is given by a multi-linear curve that is define by a set of points. The slope given by the last two specified points on the positive velocity axis is extrapolated to infinite positive velocities. Velocity and friction points need to be equal or larger than zero (no negative values should be defined). The number of provided velocity points needs to be equal to the number of provided friction points.

   ================================   ===========================================================================
   ``frnTag`` |int|                   unique friction model tag
   ``velPoints`` |listf|              list of velocity points along friction-velocity curve
   ``frnPoints`` |listf|              list of friction points along friction-velocity curve
   ================================   ===========================================================================
