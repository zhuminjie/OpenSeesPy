.. include:: sub.txt

======================
 constraints commands
======================

.. function:: constraints(constraintType, *constraintArgs)

   This command is used to construct the ConstraintHandler object. The ConstraintHandler object determines how the constraint equations are enforced in the analysis. Constraint equations enforce a specified value for a DOF, or a relationship between DOFs.

   ================================   ===========================================================================
   ``constraintType`` |str|           constraints type
   ``constraintArgs`` |list|          a list of constraints arguments
   ================================   ===========================================================================


The following contain information about available ``constraintType``:


#. :doc:`PlainConstraint`
#. :doc:`LagrangeMultipliers`
#. :doc:`PenaltyMethod`
#. :doc:`TransformationMethod`


.. toctree::
   :maxdepth: 2
   :hidden:

   PlainConstraint
   LagrangeMultipliers
   PenaltyMethod
   TransformationMethod
