.. include:: sub.txt

============================
 plot_deformedshape command
============================

.. function:: postprocessing.Get_Rendering.plot_deformedshape(Model="ModelName", LoadCase="LoadCaseName", <tstep = -1>, <scale = 10>, <overlap='no'>)

   Displays the deformed shape of the structure by reading data from a saved output database.

   ========================  =============================================================================================
   ``ModelName``     |str|     Name of the model to read data from output database, created with `createODB()` command.
   ``LoadCaseName`` |str|      Name of the subfolder with load case output data.
   ``tstep``        |float|    Approximate time of the analysis at which deformed shape is to be displaced. (optional, default is the last step)
   ``scale`` |int|             Scale factor for to display mode shape. (optional, default is 10)
   ``overlap``  |str|          "yes" to overlap the deformed shape with the original structure. (optional, default is "no")
   ========================  =============================================================================================


   
Examples: 
    
   ``plot_deformedshape(Model="TwoSpan_Bridge", LoadCase="Dynamic_GM1")``
                 Displays the deformedshape of structure by reading data from `TwoSpan_Bridge_ODB` with a sub-folder `Dynamic_GM1` at the last analysis step (default) with a default scale factor of 10.


   ``plot_deformedshape(Model="TwoSpan_Bridge", LoadCase="Dynamic_GM1", tstep=24.0, scale=50, overlap="yes")``
                 Displays the deformedshape of structure by reading data from `TwoSpan_Bridge_ODB` with a sub-folder `Dynamic_GM1` at the analysis time closest to 24.0 sec with a scale factor of 50, overlapped with the original structure shape.


.. image:: /_static/plot_deformedshape_output.png