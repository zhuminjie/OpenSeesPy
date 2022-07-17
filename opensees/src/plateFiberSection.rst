.. include:: sub.txt

=====================
 Plate Fiber Section
=====================

.. function:: section('PlateFiber',secTag,matTag,h)
   :noindex:

   This command allows the user to construct a MembranePlateFiberSection object, which is a section that numerically integrates through the plate thickness with "fibers" and is appropriate for plate and shell analysis.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``matTag`` |int|                   nDMaterial tag to be assigned to each fiber
   ``h`` |float|                      plate thickness
   ================================   ===========================================================================
