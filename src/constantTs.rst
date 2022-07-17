.. include:: sub.txt

=====================
 Constant TimeSeries
=====================

.. function:: timeSeries('Constant', tag, '-factor', factor=1.0)
   :noindex:

   This command is used to construct a TimeSeries object in which the load factor applied remains constant and is independent of the time in the domain, i.e. :math:`\lambda = f(t) = C`.
      
   ================================   ===========================================================================
   ``tag`` |int|                      unique tag among TimeSeries objects.
   ``factor`` |float|                 the load factor applied (optional)
   ================================   ===========================================================================
