.. include:: sub.txt

========================
 Hello World Example 1
========================


#. The source code is shown below, which can be downloaded :download:`here </pyExamples/hello.py>`.
#. Run the source code with 4 processors

::

  mpiexec -np 4 python hello.py

the outputs look like

::

  Hello World Process: 1
  Hello World Process: 2
  Hello World Process: 0
  Total number of processes: 4
  Hello World Process: 3
  Process 1 Terminating
  Process 2 Terminating
  Process 0 Terminating
  Process 3 Terminating


The script is shown below

.. literalinclude:: /pyExamples/hello.py
   :linenos:

