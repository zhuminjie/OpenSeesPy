.. include:: sub.txt

===========================
 UniformExcitation Pattern
===========================

.. function:: pattern('UniformExcitation',patternTag,dir,'-disp',dispSeriesTag,'-vel',velSeriesTag,'-accel',accelSeriesTag,'-vel0',vel0,'-fact',fact)
   :noindex:
   
   The UniformExcitation pattern allows the user to apply a uniform excitation to a model acting in a certain direction. The command is as follows:

   ========================   =============================================================
   ``patternTag`` |int|       unique tag among load patterns
   ``dir`` |int|              direction in which ground motion acts
      
                              #. corresponds to translation along the global X axis
			      #. corresponds to translation along the global Y axis
			      #. corresponds to translation along the global Z axis
			      #. corresponds to rotation about the global X axis
			      #. corresponds to rotation about the global Y axis
			      #. corresponds to rotation about the global Z axis
			      
   ``dispSeriesTag`` |int|    tag of the TimeSeries series defining the displacement
                              history. (optional)
   ``velSeriesTag`` |int|     tag of the TimeSeries series defining the velocity
                              history. (optional)
   ``accelSeriesTag`` |int|   tag of the TimeSeries series defining the acceleration
                              history. (optional)
   ``vel0`` |float|           the initial velocity (optional, default=0.0)
   ``fact`` |float|           constant factor (optional, default=1.0)
   ========================   =============================================================


.. note::

   #. The responses obtained from the nodes for this type of excitation are RELATIVE values, and not the absolute values obtained from a multi-support case.
   #. must set one of the disp, vel or accel time series 

