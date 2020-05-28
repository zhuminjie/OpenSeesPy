.. include:: sub.txt

============
 energyIncr
============

.. function:: test('EnergyIncr',tol,iter,pFlag=0,nType=2)
   :noindex:

   Create a EnergyIncr test, which uses the dot product of the solution vector and norm of the right hand side of the matrix equation to determine if convergence has been reached.

   ======================   =============================================================
   ``tol`` |float|          Tolerance criteria used to check for convergence.
   ``iter`` |int|           Max number of iterations to check
   ``pFlag`` |int|          Print flag (optional):

                            * 0 print nothing.
		            * 1 print information on norms each time ``test()`` is invoked.
			    * 2 print information on norms and number of iterations at end of successful test.
			    * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
			    * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.

   ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
   ======================   =============================================================


   * When using the Penalty method additional large forces to enforce the penalty functions exist on the right hand side, making convergence using this test usually impossible (even though solution might have converged).
   * When using the Lagrange method to enforce the constraints, the Lagrange multipliers appear in the solution vector.
