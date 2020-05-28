.. include:: sub.txt

=====================
 timeSeries commands
=====================




.. function:: timeSeries(tsType, tsTag, *tsArgs)

   
   This command is used to construct a TimeSeries object which represents the relationship between the time in the domain, :math:`t`, and the load factor applied to the loads, :math:`\lambda`, in the load pattern with which the TimeSeries object is associated, i.e. :math:`\lambda = F(t)`.


   ================================   ===========================================================================
   ``tsType`` |str|                   time series type.
   ``tsTag`` |int|                    time series tag.
   ``tsArgs`` |list|                  a list of time series arguments
   ================================   ===========================================================================

	      



The following contain information about available ``tsType``:

#. :doc:`constantTs`
#. :doc:`linearTs`
#. :doc:`trigTs`
#. :doc:`triangleTs`
#. :doc:`rectTs`
#. :doc:`pulseTs`
#. :doc:`pathTs`

.. toctree::
   :maxdepth: 2
   :hidden:

   constantTs
   linearTs
   trigTs
   triangleTs
   rectTs
   pulseTs
   pathTs
