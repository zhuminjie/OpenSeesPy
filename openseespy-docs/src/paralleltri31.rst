.. include:: sub.txt

========================
 Parallel Tri31 Example
========================


#. The source code is shown below, which can be downloaded :download:`here </pyExamples/paralleltri31.py>`.
#. Run the source code with 4 processors

::

  mpiexec -np 4 python paralleltri31.py

the outputs look like

::

  opensees.msg: TIME(sec) Real: 0.177647

  opensees.msg: TIME(sec) Real: 0.187682

  opensees.msg: TIME(sec) Real: 0.193193

  opensees.msg: TIME(sec) Real: 0.19473

  opensees.msg: TIME(sec) Real: 14.4652

  Node 4 [-0.16838893553441528, -2.88399389660282]

  opensees.msg: TIME(sec) Real: 14.4618

  opensees.msg: TIME(sec) Real: 14.4619

  opensees.msg: TIME(sec) Real: 14.4948

  Process 0 Terminating
  Process 1 Terminating
  Process 2 Terminating
  Process 3 Terminating


The script is shown below

.. literalinclude:: /pyExamples/paralleltri31.py
   :linenos:

