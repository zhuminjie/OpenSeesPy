.. include:: sub.txt

=========================
 RaphsonNewton Algorithm
=========================

.. function:: algorithm('RaphsonNewton',iterate='current',increment='current')
   :noindex:

   Create a RaphsonNewton algorithm which uses Raphson accelerator.

   ================================   =============================================================
   ``iterate`` |str|                  Tangent to iterate on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ``increment`` |str|                Tangent to increment on,
		                      ``'current'``, ``'initial'``, ``'noTangent'`` (optional)
   ================================   =============================================================
