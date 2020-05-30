.. include:: sub.txt

====================
 algorithm commands
====================

.. function:: algorithm(algoType, *algoArgs)

   This command is used to construct a SolutionAlgorithm object, which determines the sequence of steps taken to solve the non-linear equation.

   ================================   ===========================================================================
   ``algoType`` |str|                 algorithm type
   ``algoArgs`` |list|                a list of algorithm arguments
   ================================   ===========================================================================

The following contain information about available ``algoType``:

#. :doc:`linearAlgo`
#. :doc:`newton`
#. :doc:`newtonLineSearch`
#. :doc:`modifiedNewton`
#. :doc:`krylovNewton`
#. :doc:`secantNewton`
#. :doc:`raphsonNewton`
#. :doc:`periodicNewton`
#. :doc:`bfgs`
#. :doc:`broyden`


.. toctree::
   :maxdepth: 2
   :hidden:

   linearAlgo
   newton
   newtonLineSearch
   modifiedNewton
   krylovNewton
   secantNewton
   raphsonNewton
   periodicNewton
   bfgs
   broyden
