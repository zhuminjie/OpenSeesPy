.. include:: sub.txt

=========================
 Postprocessing Modules
=========================

.. toctree::
    :maxdepth: 1
    :hidden:

    plotcmds
    ops_vis

This is the main page for listing OpenSeesPy postprocessing modules.
For commands and documentation check their corresponding subpages.

There are two OpenSees plotting modules:

#. :doc:`plotcmds`
#. :doc:`ops_vis`

These modules also contain helper functions and other postprocessing
commands preparing data for plotting.

Note that you can use both modules at the same time (even the same
function name e.g. ``plot_model()``) in a single OpenSeesPy script by
distinguishing them as follows: ::

   	import openseespy.opensees as ops
	import openseespy.postprocessing.Get_Rendering as opsplt
	import openseespy.postprocessing.ops_vis as opsv
	# ...
	opsplt.plot_model()  # command from Get_Rendering module
	opsv.plot_model()  # command from ops_vis module
