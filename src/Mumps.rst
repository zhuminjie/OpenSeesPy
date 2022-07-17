.. include:: sub.txt

==============
 MUMPS Solver
==============

.. function:: system('Mumps','-ICNTL14',icntl14=20.0,'-ICNTL7',icntl7=7)
   :noindex:

   Create a system of equations using the Mumps solver


   ========================   ===========================================================================
   ``icntl14``                controls the percentage increase in the estimated working space (optional)
   ``icntl7``                 computes a symmetric permutation (ordering) to determine the pivot order to
                              be used for the factorization in case of sequential analysis (optional)

                              * 0: AMD
                              * 1: set by user
                              * 2: AMF
                              * 3: SCOTCH
                              * 4: PORD
                              * 5: Metis
                              * 6: AMD with QADM
                              * 7: automatic
   ========================   ===========================================================================


   Use this command only for parallel model.

.. warning::

   Don't use this command if model is not parallel, for example,
   parametric study.
