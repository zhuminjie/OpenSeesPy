.. include:: sub.txt

========================
 Hello World Example 2
========================


#. The source code is shown below, which can be downloaded :download:`here </pyExamples/hello2.py>`.
#. Run the source code with 4 processors

::

  mpiexec -np 4 python hello2.py

the outputs look like

::

  Random:
  Hello from 2
  Hello from 1
  Hello from 3

  Ordered:
  Hello from 1
  Hello from 2
  Hello from 3

  Broadcasting:
  Hello from 0
  Hello from 0
  Hello from 0
  Process 3 Terminating
  Process 2 Terminating
  Process 1 Terminating
  Process 0 Terminating


The script is shown below

.. literalinclude:: /pyExamples/hello2.py
   :linenos:

