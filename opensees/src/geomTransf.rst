.. include:: sub.txt

=====================
 geomTransf commands
=====================

.. function:: geomTransf(transfType, transfTag, *transfArgs)

   The geometric-transformation command is used to construct a coordinate-transformation (CrdTransf) object, which transforms beam element stiffness and resisting force from the basic system to the global-coordinate system. The command has at least one argument, the transformation type.

   ================================   ===========================================================================
   ``transfType`` |str|               geomTransf type
   ``transfTag`` |int|                geomTransf tag.
   ``transfArgs`` |list|              a list of geomTransf arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   transfType = 'Linear'
   transfTag = 1
   transfArgs = []
   geomTransf(transfType, transfTag, *transfArgs)



The following contain information about available ``transfType``:


#. :doc:`LinearTransf`
#. :doc:`pdelta`
#. :doc:`corotational`


.. toctree::
   :maxdepth: 2
   :hidden:

   LinearTransf
   pdelta
   corotational
