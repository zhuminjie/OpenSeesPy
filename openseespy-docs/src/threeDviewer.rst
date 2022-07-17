.. include:: sub.txt

===========
 3D Viewer
===========

This document explains the cloud 3D viewer

Selection and Mouse
-----------------------------

The following mouse actions are available:

- Left button click

  Select an object in the viewer. When an object is selected,
  the color of the object becomes red, and information about
  the object is shown in a table in the viewer.

- Left button drag

  Rotate the model in the scene

- Right button

  Moving the model in the scene

- Scroll button

  Zoom the scene



Module editing
--------------

At the top of the viewer are the buttons.
From the left, icons will be shown to indicate
module editing, such as

.. image:: /_static/viewicons.png

The icons are the module icons which contain an
editor and the number on the icon shows how many
modules are changed for a particular module type.

Generate model
--------------

Right next to the module editing icons
are the ``Generate model`` button.

This button will generate the model defined in all the scripts
in modules shown in the module editing icons.

The order of modules that are run are
based on the actual order of the modules
shown in the left panel.


Generate one module
--------------------

Next to the ``Generate model`` button is the
``Generate one module`` button.

- This button will only generate the part of the model
  for the currently focused
  module.

- Initially, this button is disabled until one of the module
  is selected.

  .. image:: /_static/initialRunOne.png

- The name of the currently focused module will be
  displayed on the button. For example,

  .. image:: /_static/runOne.png

- To make a module currently focused, you
  can open the module and click
  in the editor.

- Once a module is run, all other models are kept except
  those are changed in the current model.


Run analysis
------------

Next to the ``Generate one module`` button
is the ``Run analysis``.

Unlike the ``Generate model`` which only generates the model,
the ``Run analysis`` actually runs the analysis with the generated
model. This button will generate model first if it's not done yet.

The outputs of analysis will be shown in the :doc:`outputModule` like
following::

  Running analysis ...

  <some outputs when generating the model>

  Solving ...

  Analysis outputs:

  <some outputs from the analysis>

  Analysis errors:

  <error information is there is error in the analysis>

  The analysis is done

When the analysis is done, the model will be updated
with results from the analysis.

Reset Camera
------------

The next button is the ``Reset Camera``.

.. image:: /_static/resetCamera.png

This button will reset the camera to its original state.
