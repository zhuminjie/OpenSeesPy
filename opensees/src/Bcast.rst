.. include:: sub.txt

=====================
 Bcast command
=====================

.. function:: Bcast(*data)

   Broadcast information from processor 0 to all processors.

   ===================================   ===========================================================================
   ``data`` |listi|                      can be a list of integers
   ``data`` |listf|                      can be a list of floats
   ``data`` |str|                        can be a string
   ===================================   ===========================================================================

.. note::

  Run the same command to receive data sent from pid = 0.
  
  For example, 
.. code-block:: python

   if pid == 0:

     data1 = []
     data2 = []

     ops.Bcast(*data1)
     ops.Bcast(*data2)

   if pid != 0:
     data1 = ops.Bcast()
     data2 = ops.Bcast()
