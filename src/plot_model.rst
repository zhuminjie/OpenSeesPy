.. include:: sub.txt

=========================
 plot_model command
=========================

.. function:: postprocessing.Get_Rendering.plot_model(<"nodes">,<"elements">,<Model="ModelName">)

   Once the model is built, it can be visualized using this command. By default Node and element tags are not displayed.
   Matplotlib and Numpy are required. No analysis is required in order to visualize the model. 
   
   To visualize an OpenSees model from an existing database (using ``createdODB()`` command), the optional argument 
   Model="ModelName" should be used. The command will read the model data from folder **ModelName_ODB**. 
    
   ========================= =============================================================
   ``"nodes"``    |str|       Displays the node tags on the model. (optional)
   ``"elements"`` |str|       Displays the element tags on the model. (optional)
   ``ModelName``  |str|       Displays the model saved in a database named "ModelName_ODB" (optional)
   ========================= =============================================================

 
    Input arguments to diaplay node and element tags can be used in any combination. 

   ``plot_model()``                       
         Displays the model using data from the active OpenSeesPy model with no node and element tags on it.
		 
   ``plot_model("nodes")``  
         Displays the model using data from the active OpenSeesPy model with only node tags on it.
   
   ``plot_model("elements")`` 
         Displays the model using data from the active OpenSeesPy model with only element tags on it.

   ``plot_model("nodes","elements")`` 
         Displays the model using data from the active OpenSeesPy model with both node and element tags on it.

   ``plot_model("nodes",Model="ModelName")`` 
         Displays the model using data from an existing database "ModelName_ODB" with only node tags on it.



   
