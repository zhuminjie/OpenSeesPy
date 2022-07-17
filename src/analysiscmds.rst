.. include:: sub.txt

===================
 Analysis Commands
===================

In OpenSees, an analysis is an object which is composed by the aggregation of component objects. It is the component objects which define the type of analysis that is performed on the model. The component classes, as shown in the figure below, consist of the following:

#. ConstraintHandler -- determines how the constraint equations are enforced in the analysis -- how it handles the boundary conditions/imposed displacements
#. DOF_Numberer -- determines the mapping between equation numbers and degrees-of-freedom
#. Integrator -- determines the predictive step for time t+dt
#. SolutionAlgorithm -- determines the sequence of steps taken to solve the non-linear equation at the current time step
#. SystemOfEqn/Solver -- within the solution algorithm, it specifies how to store and solve the system of equations in the analysis
#. Convergence Test -- determines when convergence has been achieved.


Analysis commands

#. :doc:`constraints`
#. :doc:`numberer`
#. :doc:`system`
#. :doc:`test`
#. :doc:`algorithm`
#. :doc:`integrator`
#. :doc:`analysis`
#. :doc:`eigen`
#. :doc:`analyze`


.. toctree::
   :maxdepth: 1
   :hidden:

   constraints
   numberer
   system
   test
   algorithm
   integrator
   analysis
   eigen
   analyze

