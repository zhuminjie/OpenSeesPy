.. include:: sub.txt

==========================
 Trigonometric TimeSeries
==========================

.. function:: timeSeries('Trig', tag, tStart,tEnd,period,'-factor',factor=1.0,'-shift',shift=0.0,'-zeroShift',zeroShift=0.0)
   :noindex:

   This command is used to construct a TimeSeries object in which the load factor is some trigonemtric function of the time in the domain

   .. math::

      \lambda = f(t) = 
      \begin{cases}
          cFactor * sin(\frac{2.0\pi(t-tStart)}{period}+\phi), &  tStart<=t<=tEnd\\
          0.0, & otherwise
      \end{cases}

      \phi = shift - \frac{period}{2.0\pi} * \arcsin(\frac{zeroShift}{cFactor})

   ========================   =============================================================
   ``tag`` |int|              unique tag among TimeSeries objects.
   ``tStart`` |float|         Starting time of non-zero load factor.
   ``tEnd`` |float|           Ending time of non-zero load factor.
   ``period`` |float|         Characteristic period of sine wave.
   ``shift`` |float|          Phase shift in radians. (optional)
   ``factor`` |float|         Load factor. (optional)
   ``zeroShift`` |float|      Zero shift. (optional)
   ========================   =============================================================

