.. include:: sub.txt

===================
 loadConst command
===================

.. function:: loadConst('-time', pseudoTime)

   This command is used to set the loads constant in the domain and to also set the time in the domain. When setting the loads constant, the procedure will invoke setLoadConst() on all LoadPattern objects which exist in the domain at the time the command is called.

   ========================   ===========================================================================
   ``pseudoTime`` |float|     Time domain is to be set to (optional)
   ========================   ===========================================================================


.. note::

   Load Patterns added afer this command is invoked are not set to constant.
