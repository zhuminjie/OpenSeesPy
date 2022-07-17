.. include:: sub.txt

==================
 Pulse TimeSeries
==================

.. function:: timeSeries('Pulse',tag,tStart,tEnd,period,'-width',width=0.5,'-shift',shift=0.0,'-factor',factor=1.0,'-zeroShift',zeroShift=0.0)
   :noindex:

   This command is used to construct a TimeSeries object in which the load factor is some pulse function of the time in the domain.

   .. math::

      \lambda = f(t) = 
      \begin{cases}
          cFactor+zeroShift, &  k < width\\
	  zeroshift, & k < 1\\
	  0.0, & otherwise
      \end{cases}

   .. math::

      k = \frac{t+shift-tStart}{period}-floor(\frac{t+shift-tStart}{period})

   ========================   =============================================================
   ``tag`` |int|              unique tag among TimeSeries objects.
   ``tStart`` |float|         Starting time of non-zero load factor.
   ``tEnd`` |float|           Ending time of non-zero load factor.
   ``period`` |float|         Characteristic period of pulse.
   ``width`` |float|          Pulse width as a fraction of the period. (optinal)
   ``shift`` |float|          Phase shift in seconds. (optional)
   ``factor`` |float|         Load factor. (optional)
   ``zeroShift`` |float|      Zero shift. (optional)
   ========================   =============================================================

