.. include:: sub.txt

========================
 Rectangular TimeSeries
========================

.. function:: timeSeries('Rectangular', tag,tStart,tEnd,'-factor',factor=1.0)
   :noindex:
   
   This command is used to construct a TimeSeries object in which the load factor is constant for a specified period and 0 otherwise, i.e.

   .. math::

      \lambda = f(t) = 
      \begin{cases}
          cFactor, &  tStart<=t<=tEnd\\
	  0.0, & otherwise
      \end{cases}

   ========================   =============================================================
   ``tag`` |int|              unique tag among TimeSeries objects.
   ``tStart`` |float|         Starting time of non-zero load factor.
   ``tEnd`` |float|           Ending time of non-zero load factor.
   ``factor`` |float|         Load factor. (optional)
   ========================   =============================================================
