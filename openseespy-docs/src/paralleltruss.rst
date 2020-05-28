.. include:: sub.txt

========================
 Parallel Truss Example
========================


#. The source code is shown below, which can be downloaded :download:`here </pyExamples/paralleltruss.py>`.
#. Run the source code with 2 processors

::

  mpiexec -np 2 python paralleltruss.py

the outputs look like

::

  Node 4:  [[72.0, 96.0], [0.5300927771322836, -0.17789363846931772]]
  Node 4:  [[72.0, 96.0], [0.5300927771322836, -0.17789363846931772]]
  Node 4:  [[72.0, 96.0], [1.530092777132284, -0.19400676316761836]]
  Node 4:  [[72.0, 96.0], [1.530092777132284, -0.19400676316761836]]
  opensees.msg: TIME(sec) Real: 0.208238

  opensees.msg: TIME(sec) Real: 0.209045

  Process 0 Terminating
  Process 1 Terminating


The script is shown below

.. literalinclude:: /pyExamples/paralleltruss.py
   :linenos:

