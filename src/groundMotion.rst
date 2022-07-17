.. include:: sub.txt

=====================
 Plain Ground Motion
=====================

.. function:: groundMotion(gmTag,'Plain','-disp',dispSeriesTag,'-vel',velSeriesTag,'-accel',accelSeriesTag,'-int',tsInt='Trapezoidal','-fact',factor=1.0)

   This command is used to construct a plain GroundMotion object. Each GroundMotion object is associated with a number of TimeSeries objects, which define the acceleration, velocity and displacement records for that ground motion. T


   ========================   =============================================================
   ``gmTag`` |int|            unique tag among ground motions in load pattern
   ``dispSeriesTag`` |int|    tag of the TimeSeries series defining the displacement
                              history. (optional)
   ``velSeriesTag`` |int|     tag of the TimeSeries series defining the velocity
                              history. (optional)
   ``accelSeriesTag`` |int|   tag of the TimeSeries series defining the acceleration
                              history. (optional)
   ``tsInt`` |str|            ``'Trapezoidal'`` or ``'Simpson'``
                              numerical integration method
   ``factor`` |float|         constant factor. (optional)
   ========================   =============================================================


.. note::

   #. The displacements are the ones used in the ImposedMotions to set nodal response.
   #. If only the acceleration TimeSeries is provided, numerical integration will be used to determine the velocities and displacements.
   #. For earthquake excitations it is important that the user provide the displacement time history, as the one generated using the trapezoidal method will not provide good results.
   #. Any combination of the acceleration, velocity and displacement time-series can be specified.
