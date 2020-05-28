.. include:: sub.txt

================
 remove command
================

.. function:: remove(type,tag)

   This commmand is used to remove components from the model.

   ========================   ===========================================================================
   ``type`` |str|             type of the object, ``'ele'``, ``'loadPattern'``, ``'parameter'``, ``'node'``, ``'timeSeries'``, ``'sp'``, ``'mp'``.
   ``tag`` |int|              tag of the object
   ========================   ===========================================================================


.. function:: remove('recorders')
   :noindex:

   Remove all recorder objects.


.. function:: remove('sp', nodeTag, dofTag, patternTag)
   :noindex:

   Remove a sp object based on node

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag
   ``dof`` |int|              dof the sp constrains
   ``patternTag`` |int|       pattern tag, (optional)
   ========================   ===========================================================================
