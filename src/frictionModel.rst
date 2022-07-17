.. include:: sub.txt

========================
 frictionModel commands
========================

.. function:: frictionModel(frnType, frnTag, *frnArgs)

   The frictionModel command is used to construct a friction model object, which specifies the behavior of the coefficient of friction in terms of the absolute sliding velocity and the pressure on the contact area. The command has at least one argument, the friction model type.

   ================================   ===========================================================================
   ``frnType`` |str|                  frictionModel type
   ``frnTag`` |int|                   frictionModel tag.
   ``frnArgs`` |list|                 a list of frictionModel arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   frnType = 'Coulomb'
   frnTag = 1
   frnArgs = [mu]
   frictionModel(frnType, frnTag, *frnArgs)



The following contain information about available ``frnType``:


#. :doc:`Coulomb`
#. :doc:`veldependent`
#. :doc:`velnormal`
#. :doc:`velpressure`
#. :doc:`velmulti`


.. toctree::
   :maxdepth: 2
   :hidden:

   Coulomb
   veldependent
   velnormal
   velpressure
   velmulti
