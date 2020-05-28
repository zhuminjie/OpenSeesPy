.. include:: sub.txt

.. _PFEM-System:

==========
 PFEM SOE
==========

.. function:: system('PFEM','-compressible','-mumps')
   :noindex:

   Create a incompressible PFEM system of equations using the Umfpack solver


   ========================   ===========================================================================
   ``-compressible``          Solve using a quasi-incompressible formulation. (optional)
   ``-mumps``                 Solve using the MUMPS solver. (optional, not supported on Windows)
   ========================   ===========================================================================
