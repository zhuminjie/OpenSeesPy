.. include:: sub.txt

======================
 nodeResponse command
======================

.. function:: nodeResponse(nodeTag, dof, responseID)

   Returns the responses at a specified node. To get reactions (id=6), must call the ``reactions`` command before
   this command.

   ========================   ===========================================================================
   ``nodeTag`` |int|          node tag.
   ``dof`` |int|              specific dof of the response
   ``responseID`` |int|       the id of responses:

	                      * Disp = 1
			      * Vel = 2
			      * Accel = 3
			      * IncrDisp = 4
			      * IncrDeltaDisp = 5
			      * Reaction = 6
			      * Unbalance = 7
			      * RayleighForces = 8
   ========================   ===========================================================================
