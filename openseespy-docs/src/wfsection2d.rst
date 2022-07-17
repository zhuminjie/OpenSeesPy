.. include:: sub.txt

=====================
 Wide Flange Section
=====================

.. function:: section('WFSection2d',secTag,matTag,d,tw,bf,tf,Nfw,Nff)
   :noindex:

   This command allows the user to construct a WFSection2d object, which is an encapsulated fiber representation of a wide flange steel section appropriate for plane frame analysis.

   ================================   ===========================================================================
   ``secTag`` |int|                   unique section tag
   ``matTag`` |int|                   tag of uniaxialMaterial assigned to each fiber
   ``d`` |float|                      section depth
   ``tw`` |float|                     web thickness
   ``bf`` |float|                     flange width
   ``tf`` |float|                     flange thickness
   ``Nfw`` |float|                    number of fibers in the web
   ``Nff`` |float|                    number of fibers in each flange
   ================================   ===========================================================================

.. note::

   The section dimensions ``d``, ``tw``, ``bf``, and ``tf`` can be found in the AISC steel manual.
