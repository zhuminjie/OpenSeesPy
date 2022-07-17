.. include:: sub.txt

=========================
 plot_modeshape command
=========================

.. function:: postprocessing.Get_Rendering.plot_modeshape(modeNumber,<scale>, <Model="modelName">)

   Any modeshape can be visualized using this command. There is no need to perform an eigen analysis exclusively since the command runs
   an eigen analysis internally. Matplotlib and Numpy are required.

   ======================   ====================================================================
   ``mode_number`` |int|     Mode number to visualize. For example: plot_modeshape(3).
   ``scale`` |int|           Scale factor for to display mode shape. (optional, default is 200)
   ``ModelName``  |str|      Displays the model saved in a database named "ModelName_ODB". (optional)
   ======================   ====================================================================


   
Example: 
    
   ``plot_modeshape(3, 300)``
                 Displays the 3rd modeshape using data from the active OpenSeesPy model with a scale factor of 300. This command should be called from an OpenSeesPy model script once the model is completed. The model should successfully work for Eigen value analysis. There is no need to create a database with `createODB()` command to use this option.


   ``plot_modeshape(3, 300, Model="TwoSpan_Bridge")``
                 Displays the 3rd modeshape using data from `TwoSpan_Bridge_ODB` database with a scale factor of 300. This command can be called from cmd, Ipython notebook or any Python IDE. An output database using `createODB()` has to be present in the current directory to use this command.
