.. include:: sub.txt

=================
 ops_vis module
=================

.. toctree::
    :maxdepth: 1
    :hidden:

    ops_vis_plot_model
    ops_vis_plot_defo
    ops_vis_plot_mode_shape
    ops_vis_section_force_diagram_2d
    ops_vis_section_force_diagram_3d
    ops_vis_plot_stress_2d
    ops_vis_plot_extruded_model_rect_section_3d
    ops_vis_anim_defo
    ops_vis_anim_mode
    ops_vis_plot_fiber_section
    ops_vis_fib_sec_list_to_cmds
    ops_vis_quad_sig_out_per_node

The ``ops_vis`` module is an OpenSeesPy plotting module, however it
also includes many helper functions required to prepare data for
plotting. To use it in OpenSees Python scripts, your ``.py`` file
should start as follows: ::

	import openseespy.opensees as ops
	import openseespy.postprocessing.ops_vis as opsv
	import matplotlib.pyplot as plt

The main commands related to various aspects of OpenSees model
visualization are as follows:

#. :doc:`ops_vis_plot_model`
#. :doc:`ops_vis_plot_defo`
#. :doc:`ops_vis_plot_mode_shape`
#. :doc:`ops_vis_section_force_diagram_2d`
#. :doc:`ops_vis_section_force_diagram_3d`
#. :doc:`ops_vis_plot_stress_2d`
#. :doc:`ops_vis_plot_extruded_model_rect_section_3d`
#. :doc:`ops_vis_anim_defo`
#. :doc:`ops_vis_anim_mode`
#. :doc:`ops_vis_plot_fiber_section`

Other helper functions include:

#. :doc:`ops_vis_fib_sec_list_to_cmds`
#. :doc:`ops_vis_quad_sig_out_per_node`

Notes:

- matplotlib's ``plt.axis('equal')`` does not work for 3d plots
  therefore right angles are not guaranteed to be 90 degrees on the
  plots

- ``plot_fiber_section`` is inspired by Matlab ``plotSection.zip``
  written by D. Vamvatsikos available at
  http://users.ntua.gr/divamva/software.html
