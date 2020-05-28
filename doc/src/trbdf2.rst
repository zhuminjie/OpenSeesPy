.. include:: sub.txt

========
 TRBDF2
========

.. function:: integrator('TRBDF2')
   :noindex:

      Create a TRBDF2 integrator. The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. It does this in an attempt to conserve energy and momentum, something Newmark does not always do.

   As opposed to dividing the time-step in 2 as outlined in the `Bathe2007`_, we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the `Bathe2007`_.
