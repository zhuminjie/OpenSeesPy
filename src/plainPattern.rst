.. include:: sub.txt

===============
 Plain Pattern
===============

.. function:: pattern('Plain',patternTag,tsTag,'-fact',fact)
   :noindex:

   This commnand allows the user to construct a LoadPattern object. Each plain load pattern is associated with a TimeSeries object and can contain multiple NodalLoads, ElementalLoads and SP_Constraint objects. The command to generate LoadPattern object contains in { } the commands to generate all the loads and the single-point constraints in the pattern. To construct a load pattern and populate it, the following command is used:



   ========================   =============================================================
   ``patternTag`` |int|       unique tag among load patterns.
   ``tsTag`` |int|            the tag of the time series to be used in the load pattern
   ``fact`` |float|           constant factor. (optional)
   ========================   =============================================================


.. note::

   the commands below to generate all the loads and sp constraints will be
   included in last called pattern command.


.. toctree::
   :maxdepth: 2

   load
   eleload
   sp
