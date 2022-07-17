.. include:: sub.txt

========================
 rigidDiaphragm command
========================

.. function:: rigidDiaphragm(perpDirn, rNodeTag, *cNodeTags)

   Create a multi-point constraint between nodes.
   These objects will constraint certain degrees-of-freedom at the listed slave nodes to move as if in a rigid plane with the master node. To enforce this constraint, ``Transformation``
   constraint is recommended. 

	      
   ========================   ===========================================================================
   ``perpDirn`` |int|         direction perpendicular to the rigid plane (i.e. direction 3 corresponds to the 1-2 plane)
   ``rNodeTag`` |int|         integer tag identifying the master node
   ``cNodeTags`` |listi|      integar tags identifying the slave nodes
   ========================   ===========================================================================


