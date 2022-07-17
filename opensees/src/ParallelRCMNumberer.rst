.. include:: sub.txt

=========================
 Parallel RCM Numberer
=========================

.. function:: numberer('ParallelRCM')
   :noindex:

   This command is used to construct a parallel version
   of RCM degree-of-freedom numbering object to provide the mapping between the degrees-of-freedom at the nodes and the equation numbers. A Plain numberer just takes whatever order the domain gives it nodes and numbers them, this ordering is both dependent on node numbering and size of the model.


   Use this command only for parallel model.

.. warning::

   Don't use this command if model is not parallel, for example,
   parametric study.
