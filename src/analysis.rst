.. include:: sub.txt

==================
 analysis command
==================

.. function:: analysis(analysisType)

   This command is used to construct the Analysis object, which defines what type of analysis is to be performed.



   * determine the predictive step for time t+dt
   * specify the tangent matrix and residual vector at any iteration
   * determine the corrective step based on the displacement increment dU

   ================================   ===========================================================================
   analysisType |str|                 char string identifying type of analysis object
                                      to be constructed. Currently 3 valid options:

				      #. ``'Static'`` - for static analysis
				      #. ``'Transient'`` - for transient analysis constant time step
				      #. ``'VariableTransient'`` - for transient analysis with variable time step
				      #. ``'PFEM'`` - for :ref:`PFEM-Analysis`.
   ================================   ===========================================================================

.. note::

   If the component objects are not defined before hand, the command automatically creates default component objects and issues warning messages to this effect. The number of warning messages depends on the number of component objects that are undefined.
