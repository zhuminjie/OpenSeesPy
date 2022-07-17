.. include:: sub.txt

====================
 RCCircular Section
====================

.. function:: section('RCCircularSection',secTag,coreMatTag,coverMatTag,steelMatTag,d,cover_depth,Ab,NringsCore,NringsCover,Nwedges,Nsteel,'-GJ',GJ <or '-torsion',matTag>)
   :noindex:

   This command allows the user to construct an RCCircularSection object, which is an encapsulated fiber representation of a circular reinforced concrete section with core and confined regions of concrete.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``coreMatTag`` |int|               tag of uniaxialMaterial assigned to each fiber in the core region
   ``coverMatTag`` |int|              tag of uniaxialMaterial assigned to each fiber in the cover region
   ``steelMatTag`` |int|              tag of uniaxialMaterial assigned to each reinforcing bar
   ``d`` |float|                      section radius
   ``cover_depth`` |float|            cover depth (assumed uniform around perimeter)
   ``Ab`` |float|                     area of each reinforcing bar
   ``NringsCore`` |int|               number of fiber rings in the core
   ``NringsCover`` |int|              number of fiber rings in the cover
   ``Nwedges`` |int|                  number of fiber wedges for the section
   ``Nsteel`` |int|                   number of reinforcing bars
   ``GJ`` |float|                     secton torsional stiffness
   ``matTag`` |int|                   tag of uniaxialMaterial assigned to section torsion response
   ================================   ===========================================================================

.. note::

   One of the -GJ or the -torsion inputs is required
   
   For more general reinforced concrete section definitions, use the Fiber Section command.
