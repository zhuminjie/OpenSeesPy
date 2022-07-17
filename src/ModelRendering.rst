.. include:: sub.txt

=============================================================================
 A Procedure to Render 2D or 3D OpenSees Model and Mode Shapes
=============================================================================

.. note::

   Note that the ``openseespy.postprocessing.Get_Rendering`` module has been moved to its
   own respository at `here <https://github.com/u-anurag/vfo>`_. The following code may
   not work and please direct any questions to `Anurag Upadhyay <https://github.com/u-anurag>`_.

#. The source code is developed by `Anurag Upadhyay <https://github.com/u-anurag>`_ from University of Utah.
#. The source code can be downloaded :download:`here </pyExamples/3DFrame_Rendering.py>`.
#. Below is an example showing how to visualize an OpenSeesPy model.
#. Import by writing in the model file, "from openseespy.postprocessing.Get_Rendering import * ". (see line 11 in below example)
#. Plot the model by writing "plot_model()" after defining all the nodes and elements. (see line 115 in below example)
#. Plot mode shapes by writing "plot_modeshape(mode_number)" after performing the eigen analysis. (see line 114 in below example)
#. Update openseespy to the latest version to get this function.

.. image:: /_static/Model_Plot3D.png
.. image:: /_static/ModeShape_5_Plot3D.png

.. literalinclude:: /pyExamples/3DFrame_Rendering.py
   :linenos:
