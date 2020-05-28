.. include:: sub.txt

=========================
 Isolator2spring Section
=========================

.. function:: section('Isolator2spring',matTag,tol,k1,Fyo,k2o,kvo,hb,PE,Po=0.0)
   :noindex:

   This command is used to construct an Isolator2spring section object, which represents the buckling behavior of an elastomeric bearing for two-dimensional analysis in the lateral and vertical plane. An Isolator2spring section represents the resultant force-deformation behavior of the bearing, and should be used with a zeroLengthSection element. The bearing should be constrained against rotation.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``tol`` |float|                    tolerance for convergence of the element state. Suggested value: E-12 to E-10. OpenSees will warn if convergence is not achieved, however this usually does not prevent global convergence.
   ``k1`` |float|                     initial stiffness for lateral force-deformation
   ``Fyo`` |float|                    nominal yield strength for lateral force-deformation
   ``k2o`` |float|                    nominal postyield stiffness for lateral force-deformation
   ``kvo`` |float|                    nominal stiffness in the vertical direction
   ``hb`` |float|                     total height of elastomeric bearing
   ``PE`` |float|                     Euler Buckling load for the bearing
   ``Po`` |float|                     axial load at which nominal yield strength is achieved (optional)
   ================================   ===========================================================================
