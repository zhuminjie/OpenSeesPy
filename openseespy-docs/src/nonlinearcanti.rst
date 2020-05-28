.. include:: sub.txt

===========================================================
 Nonlinear Canti Col Uniaxial Inelastic Section- Dyn EQ GM
===========================================================


::

   Converted to openseespy by: Pavan Chigullapally
                         University of Auckland
                         Email: pchi893@aucklanduni.ac.nz


#. EQ ground motion with gravity- uniform excitation of structure
#. The nonlinear beam-column element that replaces the elastic element of Example 2a requires the definition of the element cross section, or its behavior. In this example,
#. The Uniaxial Section used to define the nonlinear moment-curvature behavior of the element section is "aggregated" to an elastic response for the axial behavior to define
#. The required characteristics of the column element in the 2D model. In a 3D model, torsional behavior would also have to be aggregated to this section.
#. Note:In this example, both the axial behavior (typically elastic) and the flexural behavior (moment curvature) are defined indepenently and are then "aggregated" into a section.
#. This is a characteristic of the uniaxial section: there is no coupling of behaviors.
#. To run EQ ground-motion analysis (:download:`BM68elc.acc</pyExamples/EarthquakeExamples/Example2b/BM68elc.acc>` needs to be downloaded into the same directory)
#. The problem description can be found `here <http://opensees.berkeley.edu/wiki/index.php/Examples_Manual>`_ (example:2b)
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/EarthquakeExamples/Example2b/Example2b.py>`.



.. literalinclude:: /pyExamples/EarthquakeExamples/Example2b/Example2b.py
   :linenos:
