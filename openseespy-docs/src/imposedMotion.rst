.. include:: sub.txt

============================
 Imposed Motion
============================

.. function:: imposedMotion(nodeTag, dof, gmTag)

   This command is used to construct an ImposedMotionSP constraint which is used to enforce the response of a dof at a node in the model. The response enforced at the node at any give time is obtained from the GroundMotion object associated with the constraint.


   ========================   =============================================================
   ``nodeTag`` |int|          tag of node on which constraint is to be placed
   ``dof`` |int|              dof of enforced response. Valid range is from 1 through ndf at node.
   ``gmTag`` |int|            pre-defined GroundMotion object tag
   ========================   =============================================================
