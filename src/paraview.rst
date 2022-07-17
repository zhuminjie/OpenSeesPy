.. include:: sub.txt


===========================================
 Paraview in `DesignSafe`_
===========================================

`DesignSafe`_ provides paraview for viewing OpenSeesPy results:

.. tip::
   * Make sure the steps in :doc:`designsaferun` are completed.

.. tip::
   * Go to ``Workspace`` and select ``Visualizaion`` and ``Paraview``.

   .. image:: /_static/paraview.png

.. tip::
   * In the Job Submission windows, you should select ``Working Directory``,
     ``Maximum job runtime``, ``Job name``, and ``Node Count``, and click
     ``Run``.

   .. image:: /_static/paraviewjob.png

.. tip::
   * You can see the job status on the right

   .. image:: /_static/jobstatus.png


.. tip::
   * Wait until see this windows and connect to Paraview

   .. image:: /_static/jobstart.png


.. tip::
   * Now open the pvd file in Paraview

   .. image:: /_static/paraviewopen.png


.. tip::
   * Initially, you see nothing
   * Check the ``Pipeline Browser``
   * Click on the eye left to the file in ``Pipeline Browser``

   .. image:: /_static/pipeline.png


.. tip::
   * Change the ``Solid Color`` to other variables
   * Change ``Surface`` to ``Surface With Edges``

   .. image:: /_static/paraviewcolor.png
