.. include:: sub.txt

==============================
 Plotting OpenSees Tcl Output
==============================

OpenSees Tcl users can also take advantage of the plotting functions of OpenSeesPy `Get_Rendering` library. In order to do that, a Tcl script 
``Get_Rendering.tcl`` to create an output database is used. First the user need to source `Get_Rendering.tcl` into the OpenSees tcl model file and then 
call the procedure to create an output database. This procedure does what ``createODB()`` does in OpenSeesPy. Once the output database is created, users 
can call plot_model(), plot_modeshape(), plot_deformedshape() and animate_deformedshape() commands. Compatibility with other commands will be 
added in the next release.

Download the Tcl script here :download:`Get_Rendering.tcl </pyExamples/Get_Rendering.tcl>`.

.. function :: createODB "ModelName" "LoadCaseName" Nmodes

   ==========================  ======================================================================================
   ``ModelName``     |str|      Name of the model the user wants to save database with. Folder name will be `ModelName_ODB`
   ``LoadCaseName``  |str|      ``"none"`` or ``"LoadCaseName"``. Name of the subfolder to save load case output data. 
   ``Nmodes``        |int|      ``0`` or ``Nmodes (int)``. Number of modes to be saved for visualization.
   ==========================  ======================================================================================

**Note:** To record modeshape data, this procedure utilizes an internal Eigenvalue analysis. Make sure your model is well defined to avoid errors.

Example: Here is a minimal example of how to use Get_Rendering.tcl.

:: 

  # source the script in the beginning of the Tcl script.
  source Get_Rendering.tcl
  
  # create model here. 
  # define nodes, elements etc.
  # Once the model definition is finished, call the procedure to record the first 3 modeshapes.
  # When recording modeshapes, use "none" for the loadCaseName.
  
  createODB "3DBuilding" "none"  3
  
  # The above command will save all the data in a folder named "3DBuilding_ODB" and ...
  # ... a sub-folder "Modeshapes".
  
  # Now to record data from a dynamic loadcase, assign a name for load case folder and ...
  # ... the number 0 to Nmodes to avoid performing Eigenvalue analysis again.
  
  createODB "3DBuilding" "Dynamic" 0
  
  # The above command will save the node displacement data to a sub-folder "Dynamic" in ...
  # ... the "3DBuilding_ODB" folder.
  
Now open a python terminal or Jupyter notebook and type the following. Make sure you install the latest version of OpenSeesPy first.
Or, put the following lines in a Python script and run. 

::

  import openseespy.postprocessing.Get_Rendering as opsplt

  # render the model with node and element tags on it
  opsplt.plot_model("nodes","elements",Model=3DBuilding")

  # plot mode shape 2 with a scale factor of 100
  opsplt.plot_modeshape(2, 100, Model="3DBuilding")
  
  # animate the deformed shape for dynaic analysis and save it as a 3DBuilding.mp4 file.
  opsplt.animate_deformedshape(Model="3DBuilding", LoadCase="Dynamic", dt=0.01, Movie="3DBuilding")
  
All figures are interactive and can be saved as a .png file from the plot window.