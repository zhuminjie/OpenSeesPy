.. include:: sub.txt

===============================
 animate_deformedshape command
===============================

.. function:: postprocessing.Get_Rendering.animate_deformedshape(Model='ModelName', LoadCase='LoadCaseName', 
                          dt = dT, <tStart = 0>, <tEnd = 0>, <scale = 10>, fps = 24, FrameInterval = 0, 
						  timeScale = 1, Movie='none')


   Displays an animation of the deformed structure by reading data from a saved output database. 
   The animation object should be stored as an variable in order for the animation to run.
   The input file should have approximately the same number of time between each step or the animation will appear to speed up or slow down.
   The time step for the input data can be controlled by passing the a recorder time step.
   
   For many larger models, the runtime of the code for each frame likely be larger than the frame interval, this will result in the animation running slower than the target fps.
   **ffmpeg** codecs are required to save the animation as a movie (.mp4).



   ========================  =============================================================================================
   ``ModelName``    |str|     Name of the model to read data from output database, created with `createODB()` command.
   ``LoadCaseName`` |str|     Name of the subfolder with load case output data.
   ``dT``        |float|      The time step between frames in the input file. 
   ``tStart``    |float|      The start time for animation. It can be approximate value and the program will find the closest matching time step. (optional, default is 0)
   ``tEnd``      |float|      The end time for animation. It can be approximate value and the program will find the closest matching time step. (optional, default is last step)
   ``scale`` |int|            Scale factor for to display mode shape. (optional, default is 10)
   ``fps`` |int|              The target frames per second to be displayed. (optional, The default is 24)
   ``FrameInterval`` |int|    The time interval between frames to be used. Used to update at intervals different than 1/fps. The default is 0. (optional)
   ``timeScale`` |int|        A scale factor that increase or decrease the time between animation frames. Will not improve results if the animation speed is governed by performance limited.(optional, default is 1)
   ``Movie`` |str|            Name of the movie file in the `LoadCadeName` folder if the user wants to save the animation as .mp4 file. (optional, default is "none")
   ========================  =============================================================================================

   
Examples: 

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/-inY2aDcT4c" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
::

   ani = animate_deformedshape(Model="TwoSpan_Bridge", LoadCase="Dynamic_GM1", dt=0.01)
   
The above command animates the deformedshape of structure by reading data from `TwoSpan_Bridge_ODB` with a sub-folder `Dynamic_GM1` at dt=0.01.

::

   ani = animate_deformedshape(Model="TwoSpan_Bridge", LoadCase="Dynamic_GM1",  dt=0.01, tStart=10.0, tEnd=20.0, 
                                                                         scale=50, Movie="Bridge_Dynamic")

The above command animates the deformedshape of structure by reading data from `TwoSpan_Bridge_ODB` with a sub-folder `Dynamic_GM1` at dt=0.01, starting at t=10.0 s and ending at t=20.0 s of the earthquake input, using a scale factor of 50. The animation movie will be saved as `Bridge_Dynamic.mp4` in the `Dynamic_GM1` sub-folder.
