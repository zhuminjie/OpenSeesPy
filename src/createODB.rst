.. include:: sub.txt

=========================
 Create Output Database 
=========================

.. function:: postprocessing.Get_Rendering.createODB(ModelName, <LoadCaseName>, <Nmodes=0>, <deltaT=0.0>, <recorders=[]>)

   This command creates an Output Database for the active model with an option to save a specific load case output.
   The command **must** be called while the model is built, but before the main analysis is run.
   An output database with name ModelName_ODB is created in the current directory with node and element information
   in it. See the example below.
   
   **Note:** The support to visualize stress, strain and element forces using ``recorders=[]`` argument in this command is not yet provided.
   These functionalities will be provided in the next release of the ``Get_Rendering plotting`` library.
   Input arguments are as follows,
   
   ==========================  ===============================================================================
   ``ModelName``     |str|      Name of the model the user wants to save database with.
   ``LoadCaseName`` |str|      Name of the subfolder to save load case output data.(Optional)
   ``Nmodes``        |int|      Number of modes to be saved for visualization.(Optional)
   ``deltaT``        |float|    Timesteps at which output to be saved. Default is 0.0. (optional)
   ``recorders``     |list|     (NOT AVAILABLE YET) List of recorders to be saved for the loadcase. (optional)  
   ==========================  ===============================================================================

Here is a simple example:

::

   createODB("TwoSpan_Bridge", Nmodes=3)

   
The above command will create,

* a folder named **TwoSpan_Bridge_ODB** containing the information on the nodes and elements to visualize the structure in future without using a OpenSeesPy model file.
* a sub-folder named **ModeShapes** containing information on modeshapes and modal periods.
* no output from any loadcase will be saved saved in this case even if the analysis is run in the script since there is no argument for "LoadCaseName" is provided.
   

Here is another example command to be used when recording data from a load case.

::

   createODB("TwoSpan_Bridge","Dynamic_GM1", Nmodes=3, deltaT=0.5)

   
The above command should be used right before running a load case analysis in the OpenSeesPy script and will create,

 * a folder named **TwoSpan_Bridge_ODB** containing the information on the nodes and elements to visualize the structure in future without using a OpenSeesPy model file.
 * a sub-folder named **Dynamic_GM1** containing the information on node displacement data to plot deformed shape.
 * a sub-folder named **ModeShapes** containing information on modeshapes and modal periods.
 * the node displacement data will be saved at closest time-steps at each 0.05 sec interval. 
   

   
