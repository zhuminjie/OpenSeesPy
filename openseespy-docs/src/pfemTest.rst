.. include:: sub.txt

.. _PFEM-Test:

=============
 PFEM test
=============

.. function:: test('PFEM',tolv,tolp,tolrv,tolrp,tolrelv,tolrelp,iter,maxincr,pFlag=0,nType=2)
   :noindex:

   Create a PFEM test, which check both increments and residual for
   velocities and pressures.

   ======================   =========================================================================
   ``tolv`` |float|         Tolerance for velocity increments
   ``tolp`` |float|         Tolerance for pressure increments
   ``tolrv`` |float|        Tolerance for velocity residual
   ``tolrp`` |float|        Tolerance for pressure residual
   ``tolrv`` |float|        Tolerance for relative velocity increments
   ``tolrp`` |float|        Tolerance for relative pressure increments
   ``iter`` |int|           Max number of iterations to check
   ``maxincr`` |int|        Max times for error increasing
   ``pFlag`` |int|          Print flag (optional):

                            * 0 print nothing.
		            * 1 print information on norms each time ``test()`` is invoked.
			    * 2 print information on norms and number of iterations at end of successful test.
			    * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
			    * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.

   ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
   ======================   =========================================================================
