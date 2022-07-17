.. include:: sub.txt

===================
 Linear TimeSeries
===================

.. function:: timeSeries('Linear', tag, '-factor', factor=1.0, '-tStart', tStart=0.0)
   :noindex:

   This command is used to construct a TimeSeries object in which the load factor applied is linearly proportional to the time in the domain, i.e.

   :math:`\lambda = f(t) = cFactor * (t-tStart)`. (0 if t < tStart)

   ========================   =============================================================
   ``tag`` |int|              unique tag among TimeSeries objects
   ``factor`` |float|         Linear factor (optional)
   ``tStart`` |float|         start time (optional)
   ========================   =============================================================

