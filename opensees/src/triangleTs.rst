.. include:: sub.txt

=======================
 Triangular TimeSeries
=======================

.. function:: timeSeries('Triangle',tag,tStart,tEnd,period,'-factor',factor=1.0,'-shift',shift=0.0,'-zeroShift',zeroShift=0.0)
   :noindex:

   This command is used to construct a TimeSeries object in which the load factor is some triangular function of the time in the domain.
      
   .. math::

      \lambda = f(t) = 
      \begin{cases}
          slope*k*period+zeroShift, & k < 0.25\\
	  cFactor-slope*(k-0.25)*period+zeroShift, & k < 0.75\\
	  -cFactor+slope*(k-0.75)*period+zeroShift, & k < 1.0\\
	  0.0, & otherwise
      \end{cases}

   .. math::
      
      slope = \frac{cFactor}{period/4}
      
      k = \frac{t+\phi-tStart}{period}-floor(\frac{t+\phi-tStart}{period})
      
      \phi = shift - \frac{zeroShift}{slope}

   ========================   =============================================================
   ``tag`` |int|              unique tag among TimeSeries objects.
   ``tStart`` |float|         Starting time of non-zero load factor.
   ``tEnd`` |float|           Ending time of non-zero load factor.
   ``period`` |float|         Characteristic period of sine wave.
   ``shift`` |float|          Phase shift in radians. (optional)
   ``factor`` |float|         Load factor. (optional)
   ``zeroShift`` |float|      Zero shift. (optional)
   ========================   =============================================================



