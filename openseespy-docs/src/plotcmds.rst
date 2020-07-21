.. include:: src/sub.txt

=========================
 Postprocessing Commands
=========================

The source code is maintained by `Anurag Upadhyay <https://github.com/u-anurag>`_ from University of Utah.

**For Developers** : If you are interested in developing visualization functions and contributing to ``Get_Rendering`` library, please go through :doc:`Plotting_Development_Guide` to understand the existing code. This will be helpful in reducing changes while merging the new codes.

Model visualization is an ongoing development to make OpenSeesPy more user friendly.
It utilizes `Matplotlib 3.0 <https://matplotlib.org>`_ library to plot 2D and 3D models in a dedicated interactive window. You can use click-and-hold to change the view angle and zoom the plot. The model image can be saved with the desired orientation directly from the interactive plot window. If you did not install matplotlib using Anaconda, you will have to install PyQt or PySide to enable an interactive window (`Matplotlib Dependencies <https://matplotlib.org/users/installing.html>`_).  

**Animation**: To save the animation movie as .mp4 file, `FFmpeg <https://www.ffmpeg.org/about.html>`_ codecs are required.

When using Spyder IDE and Jupyter notebook, the default setting is to produce a static, inline plot which is not
interactive. To change that, write the command **%matplotlib qt** in the Ipython console and then execute the model plotting commands. This will produce an interactive plot in a dedicated window.


See the example :doc:`ModelRendering` for a sample script.

Following elements are supported:

    * 2D and 3D Beam-Column Elements
    * 2D and 3D Quad Elements
    * 2D and 3D Tri Elements
    * 8 Node Brick Elements
    * Tetrahedron Elements (to be added)

The following two commands are needed to visualize the model, as shown below:

::

   #Change plot backend to Qt. ONLY if you are using an Ipython console (e.g. Spyder)
   %matplotlib qt
   
   #Change plot backend to 'Nbagg' if using in Jupyter notebook to get an interactive, inline plot.
   %matplotlib notebook
   
   # import OpenSeesPy rendering module
   import openseespy.postprocessing.Get_Rendering as opsplt
   
   # render the model after defining all the nodes and elements
   opsplt.plot_model()

   # plot mode shape
   opsplt.plot_modeshape(3)
   

.. image:: /_static/ModelVisualization_Intro.png

Following are commands and development guide related to model visualization:

#. :doc:`createODB`
#. :doc:`saveFiberData2D`
#. :doc:`plot_model`
#. :doc:`plot_modeshape`
#. :doc:`plot_deformedshape`
#. :doc:`plot_fiberResponse2D`
#. :doc:`animate_deformedshape`
#. :doc:`animate_fiberResponse2D`
#. :doc:`plotting_OpenSeesTcl`
#. :doc:`Plotting_Development_Guide`

.. toctree::
   :maxdepth: 1
   :hidden:

   createODB
   saveFiberData2D
   plot_model
   plot_modeshape
   plot_deformedshape
   plot_fiberResponse2D
   animate_deformedshape
   animate_fiberResponse2D
   plotting_OpenSeesTcl
   Plotting_Development_Guide



