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
    ops_vis_sig_out_per_node

``ops_vis`` is an OpenSeesPy postprocessing and plotting module
written by Seweryn Kokot (Opole University of Technology, Poland).

This module can be mainly useful for students when learning the
fundamentals of structural analysis (interpolated deformation of frame
structures (static images or animations), section force distribution
of frame structures, stress distribution in triangle, quadrilateral 2d
elements, orientation of frame members in 3d space, fibers of a cross
section, static and animated eigenvalue mode shapes etc.). This way,
we can lower the bar in teaching and learning OpenSees at earlier
years of civil engineering studies. However the visualization features
for OpenSees can also be helpful for research studies.

Note that OpenSeesPy contains another plotting module called
``Get_Rendering``, however ``ops_vis`` is an alternative with some
distinct features (on the other hand the ``Get_Rendering`` has other
features that ``ops_vis`` does not have), which for example allow us
to plot:

- interpolated deformation of frame structures,
- stresses of triangular and (four, eight and nine-node) quadrilateral
  2d elements (calculation of Huber-Mieses-Hencky equivalent stress,
  principal stresses),
- fibers of cross-sections,
- models with extruded cross sections
- animation of mode shapes.

To use ``ops_vis`` in OpenSees Python
scripts, your ``.py`` file should start as follows: ::

	import openseespy.opensees as ops
	import openseespy.postprocessing.ops_vis as opsv
	import matplotlib.pyplot as plt
	# ... your OpenSeesPy model and analysis commands ...
	opsv.plot_model()
	sfac = opsv.plot_defo()

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

Helper functions include:

#. :doc:`ops_vis_fib_sec_list_to_cmds`
#. :doc:`ops_vis_sig_out_per_node`

Notes:

- matplotlib's ``plt.axis('equal')`` does not work for 3d plots
  therefore right angles are not guaranteed to be 90 degrees on the
  plots

- ``plot_fiber_section`` is inspired by Matlab ``plotSection.zip``
  written by D. Vamvatsikos available at
  http://users.ntua.gr/divamva/software.html
