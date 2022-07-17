.. include:: sub.txt

==================
 eigen command
==================

.. function:: eigen(solver='-genBandArpack', numEigenvalues)

   Eigen value analysis. Return a list of eigen values.

   ================================   ===========================================================================
   numEigenvalues |int|               number of eigenvalues required
   solver |str|                       optional string detailing type of solver: ``'-genBandArpack'``, ``'-symmBandLapack'``, ``'-fullGenLapack'``, (optional)
   ================================   ===========================================================================

.. note::

   #. The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, the nodeEigenvector command, or the Print command.
   #. The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.
