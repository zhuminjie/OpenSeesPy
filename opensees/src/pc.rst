.. include:: sub.txt

============================
 pressureConstraint command
============================

.. function::  pressureConstraint(nodeTag, pNodeTag)

   Create a pressure constraint for incompressible flow.

   ========================   ===========================================================================
   ``nodeTag`` |int|          tag of node to be constrained
   ``pNodeTag`` |int|         tag of extra pressure node, which
	                      must exist before calling this command
   ========================   ===========================================================================

For example, 

.. code-block:: python

   ops.node(1, 0.0, 0.0)
   ops.node(2, 0.0, 0.0, '-ndf', 1)
   ops.pressureConstraint(1, 2)

