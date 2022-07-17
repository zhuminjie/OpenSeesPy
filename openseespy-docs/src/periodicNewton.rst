.. include:: sub.txt

==========================
 PeriodicNewton Algorithm
==========================

.. function:: algorithm('PeriodicNewton',iterate='current',increment='current',maxDim=3)
   :noindex:

   Create a PeriodicNewton algorithm using periodic accelerator.

   ================================   =============================================================
   ``iterate`` |str|                  Tangent to iterate on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``increment`` |str|                Tangent to increment on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``maxDim`` |int|                   Max number of iterations until
		                      the tangent is reformed and
                                      the acceleration restarts. (optional)
   ================================   =============================================================
