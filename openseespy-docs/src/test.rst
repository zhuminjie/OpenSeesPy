.. include:: sub.txt

======================
 test commands
======================

.. function:: test(testType, *testArgs)

   This command is used to construct the LinearSOE and LinearSolver objects to store and solve the test of equations in the analysis.

   ================================   ===========================================================================
   ``testType`` |str|                 test type
   ``testArgs`` |list|                a list of test arguments
   ================================   ===========================================================================


The following contain information about available ``testType``:

#. :doc:`normUnbalance`
#. :doc:`normDispIncr`
#. :doc:`energyIncr`
#. :doc:`relativeNormUnbalance`
#. :doc:`relativeNormDispIncr`
#. :doc:`relativeTotalNormDispIncr`
#. :doc:`relativeEnergyIncr`
#. :doc:`fixedNumIter`
#. :doc:`normDispAndUnbalance`
#. :doc:`normDispOrUnbalance`
#. :ref:`PFEM-Test`


.. toctree::
   :maxdepth: 2
   :hidden:

   normUnbalance
   normDispIncr
   energyIncr
   relativeNormUnbalance
   relativeNormDispIncr
   relativeTotalNormDispIncr
   relativeEnergyIncr
   fixedNumIter
   normDispAndUnbalance
   normDispOrUnbalance



