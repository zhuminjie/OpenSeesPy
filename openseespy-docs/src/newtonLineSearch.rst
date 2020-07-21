.. include:: sub.txt

=========================
 Newton with Line Search
=========================

.. function:: algorithm('NewtonLineSearch',Bisection=False,Secant=False,RegulaFalsi=False,InitialInterpolated=False,tol=0.8,maxIter=10,minEta=0.1,maxEta=10.0)
   :noindex:

   Create a NewtonLineSearch algorithm. Introduces line search to the Newton algorithm to solve the nonlinear residual equation.

   ================================   =============================================================
   ``Bisection`` |bool|               Flag to use Bisection line search. (optional)
   ``Secant`` |bool|                  Flag to use Secant line search. (optional)
   ``RegulaFalsi`` |bool|             Flag to use RegulaFalsi line search. (optional)
   ``InitialInterpolated`` |bool|     Flag to use InitialInterpolated line search.(optional)
   ``tol`` |float|                    Tolerance for search. (optional)
   ``maxIter`` |float|                Max num of iterations to try. (optional)
   ``minEta`` |float|                 Min :math:`\eta` value. (optional)
   ``maxEta`` |float|                 Max :math:`\eta` value. (optional)
   ================================   =============================================================
