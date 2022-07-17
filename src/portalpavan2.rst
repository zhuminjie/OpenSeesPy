.. include:: sub.txt

=====================================================================================
 2D Portal Frame with Units- Multiple Support Dynamic EQ Ground Motion-acctimeseries
=====================================================================================


::

   Converted to openseespy by: Pavan Chigullapally
                         University of Auckland
                         Email: pchi893@aucklanduni.ac.nz


#. To run Uniaxial Inelastic Material, Fiber Section, Nonlinear Mode, MultipleSupport Earthquake ground motion
#. First import the :download:`InelasticFiberSectionPortal2Dframe.py </pyExamples/EarthquakeExamples/Example4/InelasticFiberSectionPortal2Dframe.py>`
#. Upto gravity loading is already in this script and run the current script
#. To run EQ ground-motion analysis (:download:`ReadRecord.py </pyExamples/EarthquakeExamples/Example4/ReadRecord.py>`, :download:`H-E12140.AT2</pyExamples/EarthquakeExamples/Example4/H-E12140.AT2>` needs to be downloaded into the same directory)
#. MultipleSupport Earthquake ground motion (different acceleration input at specified support nodes) -- two nodes here
#. The problem description can be found `here <http://opensees.berkeley.edu/wiki/index.php/Examples_Manual>`_ (example:4)
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/EarthquakeExamples/Example4/Example4b.py>`.



.. literalinclude:: /pyExamples/EarthquakeExamples/Example4/Example4b.py
   :linenos:


