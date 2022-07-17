.. include:: sub.txt

======================
 system commands
======================

.. function:: system(systemType, *systemArgs)

   This command is used to construct the LinearSOE and LinearSolver objects to store and solve the system of equations in the analysis.

   ================================   ===========================================================================
   ``systemType`` |str|               system type
   ``systemArgs`` |list|              a list of system arguments
   ================================   ===========================================================================


The following contain information about available ``systemType``:

#. :doc:`BandGen`
#. :doc:`BandSPD`
#. :doc:`ProfileSPD`
#. :doc:`SuperLU`
#. :doc:`UmfPack`
#. :doc:`FullGeneral`
#. :doc:`SparseSYM`
#. :ref:`PFEM-System`
#. :doc:`Mumps`


.. toctree::
   :maxdepth: 2
   :hidden:

   BandGen
   BandSPD
   ProfileSPD
   SuperLU
   UmfPack
   FullGeneral
   SparseSYM
   Mumps


