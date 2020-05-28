.. include:: sub.txt

================
 ProfileSPD SOE
================

.. function:: system('ProfileSPD')
   :noindex:

   This command is used to construct a profileSPDSOE linear system of equation object. As the name implies, this class is used for symmetric positive definite matrix systems. The matrix is stored as shown below in a 1 dimensional array with only those values below the first non-zero row in any column being stored. This is sometimes also referred to as a skyline storage scheme.
