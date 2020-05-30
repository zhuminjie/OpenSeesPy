.. include:: sub.txt

=====================
 recv command
=====================

.. function:: recv('-pid', pid)

   Receive information from another processor.

   ===================================   ===========================================================================
   ``pid`` |int|                         ID of processor where data is received from
   ``pid`` |str|                         if ``pid`` is ``'ANY'``, the processor can
                                         receive data from any processor.
   ===================================   ===========================================================================


.. note::

  :doc:`send` and :doc:`recv` must match and the order of calling both
  commands matters.