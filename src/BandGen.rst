.. include:: sub.txt

=================
 BandGeneral SOE
=================

.. function:: system('BandGen')
   :noindex:

   This command is used to construct a BandGeneralSOE linear system of equation object. As the name implies, this class is used for matrix systems which have a banded profile. The matrix is stored as shown below in a 1dimensional array of size equal to the bandwidth times the number of unknowns. When a solution is required, the Lapack routines DGBSV and SGBTRS are used.
