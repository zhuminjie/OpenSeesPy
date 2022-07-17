.. include:: sub.txt

=====================
 integrator commands
=====================

.. function:: integrator(intType, *intArgs)
   :noindex:

   This command is used to construct the Integrator object. The Integrator object determines the meaning of the terms in the system of equation object Ax=B.

   The Integrator object is used for the following:

   * determine the predictive step for time t+dt
   * specify the tangent matrix and residual vector at any iteration
   * determine the corrective step based on the displacement increment dU

   ================================   ===========================================================================
   ``intType`` |str|                  integrator type
   ``intArgs`` |list|                 a list of integrator arguments
   ================================   ===========================================================================

The following contain information about available ``intType``:

Static integrator objects
-------------------------


#. :doc:`loadControl`
#. :doc:`displacementControl`
#. :doc:`ParallelDisplacementControl`
#. :doc:`minUnbalDispNorm`
#. :doc:`arcLength`


.. toctree::
   :maxdepth: 2
   :hidden:

   loadControl
   displacementControl
   ParallelDisplacementControl
   minUnbalDispNorm
   arcLength

Transient integrator objects
----------------------------


#. :doc:`centralDifference`
#. :doc:`newmark`
#. :doc:`hht`
#. :doc:`generalizedAlpha`
#. :doc:`trbdf2`
#. :doc:`explicitDifference`
#. :ref:`PFEM-Integrator`


.. toctree::
   :maxdepth: 2
   :hidden:

   centralDifference
   newmark
   hht
   generalizedAlpha
   trbdf2
   explicitDifference


