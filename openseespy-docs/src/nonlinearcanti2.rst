.. include:: sub.txt

=============================================================
 Nonlin Canti Col Inelstc Uniaxial Mat in Fiber Sec - Dyn EQ
=============================================================


::

   Converted to openseespy by: Pavan Chigullapally
                         University of Auckland
                         Email: pchi893@aucklanduni.ac.nz



#. EQ ground motion with gravity- uniform excitation of structure
#. In this example, the Uniaxial Section of Example 2b is replaced by a fiber section. Inelastic uniaxial materials are used in this example,
#. Which are assigned to each fiber, or patch of fibers, in the section.
#. In this example the axial and flexural behavior are coupled, a characteristic of the fiber section.
#. The nonlinear/inelastic behavior of a fiber section is defined by the stress-strain response of the uniaxial materials used to define it.
#. To run EQ ground-motion analysis (:download:`BM68elc.acc</pyExamples/EarthquakeExamples/Example2c/BM68elc.acc>` needs to be downloaded into the same directory)
#. The problem description can be found `here <http://opensees.berkeley.edu/wiki/index.php/Examples_Manual>`_ (example:2c)
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/EarthquakeExamples/Example2c/Example2c.py>`.



.. literalinclude:: /pyExamples/EarthquakeExamples/Example2c/Example2c.py
   :linenos:
