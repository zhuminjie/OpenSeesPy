.. include:: sub.txt

=========================
 saveFiberData2D command 
=========================

.. function:: postprocessing.Get_Rendering.saveFiberData2D(ModelName, LoadCaseName, eleNumber, sectionNumber, deltaT = 0.0)

   This command creates saves the fiber output of a particulat section in a non-linear beam-column element to a sub-folder named
   "LoadCaseName" inside the output database folder "ModelName_ODB". This output data can be visualized using ``plot_fiberResponse2D()`` 
   and ``animate_fiberResponse2D()`` commands.
   
   ==========================  ===============================================================================
   ``ModelName``    |str|      Name of the model the user wants to save database with.
   ``LoadCaseName`` |str|      Name of the subfolder to save load case output data.
   ``eleNumber``    |int|      Tag of the element with a fiber section assigned.
   ``sectionNumber`` |float|   Tag of the section where the fiber response is to be recorded.
   ``deltaT``      |list|      Timesteps at which output to be saved. Default is 0.0. (optional)  
   ==========================  ===============================================================================

Here is a simple example:

::

   saveFiberData2D("TwoSpan_Bridge", "Pushover", 101, 2)

The above command will create,

* a folder named **TwoSpan_Bridge_ODB** and a sub-folder named **LoadCaseName** if they are not already there.
* save fiber response of the section with a tag 2 of element with a tag 101 in the LoadCaseName folder.   

   
