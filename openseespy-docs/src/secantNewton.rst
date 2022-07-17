.. include:: sub.txt

========================
 SecantNewton Algorithm
========================

.. function:: algorithm('SecantNewton',iterate='current',increment='current',maxDim=3)
   :noindex:

   Create a SecantNewton algorithm which uses the two-term update to accelerate the convergence of the ModifiedNewton.

   The default "cut-out" values recommended by Crisfield (R1=3.5, R2=0.3) are used.

   ================================   =============================================================
   ``iterate`` |str|                  Tangent to iterate on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``increment`` |str|                Tangent to increment on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``maxDim`` |int|                   Max number of iterations until
		                      the tangent is reformed and
                                      the acceleration restarts. (optional)
   ================================   =============================================================
