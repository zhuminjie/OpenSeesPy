.. include:: sub.txt

==================
 testNorm command
==================

.. function:: testNorm()

   Returns the norms from the convergence test for the last analysis step.

.. note::

   The size of norms will be equal to the max number of iterations specified. The first ``testIter`` of these will be non-zero, the remaining ones will be zero.
