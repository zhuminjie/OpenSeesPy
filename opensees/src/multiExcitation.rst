.. include:: sub.txt

==================================
 Multi-Support Excitation Pattern
==================================

.. function:: pattern('MultipleSupport', patternTag)
   :noindex:

   The Multi-Support pattern allows similar or different prescribed ground motions to be input at various supports in the structure. In OpenSees, the prescribed motion is applied using single-point constraints, the single-point constraints taking their constraint value from user created ground motions.
   
   ===================================   ===========================================================================
   ``patternTag`` |int|                  integer tag identifying pattern
   ===================================   ===========================================================================


.. note::

   #. The results for the responses at the nodes are the ABSOLUTE values, and not relative values as in the case of a UniformExciatation.
   #. The non-homogeneous single point constraints require an appropriate choice of constraint handler.



.. toctree::
   :maxdepth: 2

   groundMotion
   interpolatedGroundMotion
   imposedMotion
