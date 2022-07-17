.. include:: sub.txt

==================================
 Parallel Parametric Study Example
==================================


#. The source code is shown below, which can be downloaded :download:`here </pyExamples/paralleltruss2.py>`.
#. Run the source code with 2 processors

::

  mpiexec -np 2 python paralleltruss2.py

the outputs look like

::

  Processor 0
  Node 4 (E = 3000.0 ) Disp : [0.5300927771322836, -0.17789363846931766]
  Processor 1

  Node 4 (E = 6000.0 ) Disp : [0.2650463885661418, -0.08894681923465883]


  Process 1 Terminating
  Process 0 Terminating


The script is shown below

.. literalinclude:: /pyExamples/paralleltruss2.py
   :linenos:

