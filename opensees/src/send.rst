.. include:: sub.txt

=====================
 send command
=====================

.. function:: send('-pid', pid, *data)

   Send information to another processor.

   ===================================   ===========================================================================
   ``pid`` |int|                         ID of processor where data is sent to
   ``data`` |listi|                      can be a list of integers
   ``data`` |listf|                      can be a list of floats
   ``data`` |str|                        can be a string
   ===================================   ===========================================================================


.. note::

  :doc:`send` and :doc:`recv` must match and the order of calling both
  commands matters.