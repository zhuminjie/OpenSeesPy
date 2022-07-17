.. include:: sub.txt

=============================================================
 Cantilever 2D Column with Units-Static Pushover
=============================================================


::

   Converted to openseespy by: Pavan Chigullapally
                         University of Auckland
                         Email: pchi893@aucklanduni.ac.nz


#. To run Uniaxial Inelastic Material, Fiber Section, Nonlinear Mode, Static Pushover Analysis
#. First import the :download:`InelasticFiberSection.py </pyExamples/EarthquakeExamples/Example3/InelasticFiberSection.py>` (upto gravity loading is already in this script) and run the current script
#. To run EQ ground-motion analysis :download:`BM68elc.acc </pyExamples/EarthquakeExamples/Example3/BM68elc.acc>` needs to be downloaded into the same directory)
#. Same acceleration input at all nodes restrained in specified direction (uniform acceleration input at all support nodes)
#. The problem description can be found `here <http://opensees.berkeley.edu/wiki/index.php/Examples_Manual>`_ (example:3)
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/EarthquakeExamples/Example3/Example3b.py>`.



.. literalinclude:: /pyExamples/EarthquakeExamples/Example3/Example3b.py
   :linenos:


