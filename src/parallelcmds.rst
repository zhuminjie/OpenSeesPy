.. include:: sub.txt

===================
 Parallel Commands
===================

The parallel commands are currently only
working in the Linux version.
The parallel OpenSeesPy is similar to OpenSeesMP, which
requires users to divide the model
to distributed processors.

You can still run the single-processor version as before.
To run the parallel version, you have
to install a MPI implementation, such as `mpich`_. Then
call your python scripts in the command line

::

  mpiexec -np np python filename.py


where ``np`` is the number of processors to be used,
``python`` is the python interpreter, and
``filename.py`` is the script name.

Inside the script, OpenSeesPy is still imported as

::

  import openseespy.opensees as ops

Common problems:

#. Unmatch send/recv will cause deadlock.
#. Writing to the same files at the same from different processors will cause race conditions.
#. Poor model decomposition will cause load imbalance problem.


Following are commands related to parallel computing:

#. :doc:`getPID`
#. :doc:`getNP`
#. :doc:`barrier`
#. :doc:`send`
#. :doc:`recv`
#. :doc:`Bcast`
#. :doc:`setStartNodeTag`
#. :doc:`domainChange`
#. :doc:`ParallelPlainNumberer`
#. :doc:`ParallelRCMNumberer`
#. :doc:`Mumps`
#. :doc:`ParallelDisplacementControl`
#. :doc:`partition`



.. toctree::
   :maxdepth: 1
   :hidden:

   getPID
   getNP
   barrier
   send
   recv
   Bcast
   setStartNodeTag
   domainChange
   partition




