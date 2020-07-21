.. include:: sub.txt

=====================
 RC Section
=====================

.. function:: section('RCSection2d',secTag,coreMatTag,coverMatTag,steelMatTag,d,b,cover_depth,Atop,Abot,Aside,Nfcore,Nfcover,Nfs)
   :noindex:

   This command allows the user to construct an RCSection2d object, which is an encapsulated fiber representation of a rectangular reinforced concrete section with core and confined regions of concrete and single top and bottom layers of reinforcement appropriate for plane frame analysis.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``coreMatTag`` |int|               tag of uniaxialMaterial assigned to each fiber in the core region
   ``coverMatTag`` |int|              tag of uniaxialMaterial assigned to each fiber in the cover region
   ``steelMatTag`` |int|              tag of uniaxialMaterial assigned to each reinforcing bar
   ``d`` |float|                      section depth
   ``b`` |float|                      section width
   ``cover_depth`` |float|            cover depth (assumed uniform around perimeter)
   ``Atop`` |float|                   area of reinforcing bars in top layer
   ``Abot`` |float|                   area of reinforcing bars in bottom layer
   ``Aside`` |float|                  area of reinforcing bars on intermediate layers
   ``Nfcore`` |float|                 number of fibers through the core depth
   ``Nfcover`` |float|                number of fibers through the cover depth
   ``Nfs`` |float|                    number of bars on the top and bottom rows of reinforcement (Nfs-2 bars will be placed on the side rows)
   ================================   ===========================================================================

.. note::

   For more general reinforced concrete section definitions, use the Fiber Section command.
