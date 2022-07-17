.. include:: sub.txt

=====================
 NormDispOrUnbalance
=====================

.. function:: test('NormDispOrUnbalance',tolIncr,tolR,iter,pFlag=0,nType=2,maxincr=-1)
   :noindex:

   Create a NormDispOrUnbalance test, which check if both
   ``'NormUnbalance'`` and ``'normDispIncr'`` are converged.

   ======================   =============================================================
   ``tolIncr`` |float|      Tolerance for left hand solution increments
   ``tolIncr`` |float|      Tolerance for right hand residual
   ``iter`` |int|           Max number of iterations to check
   ``pFlag`` |int|          Print flag (optional):

                            * 0 print nothing.
		            * 1 print information on norms each time ``test()`` is invoked.
			    * 2 print information on norms and number of iterations at end of successful test.
			    * 4 at each step it will print the norms and also the :math:`\Delta U` and :math:`R(U)` vectors.
			    * 5 if it fails to converge at end of ``numIter`` it will print an error message **but return a successfull test**.

   ``nType`` |int|          Type of norm, (0 = max-norm, 1 = 1-norm, 2 = 2-norm). (optional)
   ``maxincr`` |int|        Maximum times of error increasing. (optional)
   ======================   =============================================================
