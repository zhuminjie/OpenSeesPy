.. include:: sub.txt

======================================================
 2D Column - Dynamic EQ Ground Motion
======================================================

::

   Converted to openseespy by: Pavan Chigullapally
                         University of Auckland
                         Email: pchi893@aucklanduni.ac.nz


#. EQ ground motion with gravity- uniform excitation of structure
#. All units are in kip, inch, second
#. Note: In this example, all input values for Example 1a are replaced by variables. The objective of this example is to demonstrate the use of variables in defining
#. The OpenSees input and also to run various tests and algorithms at once to increase the chances of convergence
#. To run EQ ground-motion analysis (:download:`BM68elc.acc</pyExamples/EarthquakeExamples/Example2a/BM68elc.acc>` needs to be downloaded into the same directory)
#. The detailed problem description can be found `here <http://opensees.berkeley.edu/wiki/index.php/Examples_Manual>`_  (example:2a)
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/EarthquakeExamples/Example2a/Example2a.py>`.



.. literalinclude:: /pyExamples/EarthquakeExamples/Example2a/Example2a.py
   :linenos:
