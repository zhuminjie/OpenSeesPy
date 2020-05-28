.. include:: sub.txt

==================
 pattern commands
==================

.. function:: pattern(patternType, patternTag, *patternArgs)

The pattern command is used to construct a LoadPattern and add it to the Domain. Each LoadPattern in OpenSees has a TimeSeries associated with it. In addition it may contain ElementLoads, NodalLoads and SinglePointConstraints. Some of these SinglePoint constraints may be associated with GroundMotions.


================================   ===========================================================================
   ``patternType`` |str|           pattern type.
   ``patternTag`` |int|            pattern tag.
   ``patternArgs`` |list|          a list of pattern arguments
================================   ===========================================================================


The following contain information about available ``patternType``:


#. :doc:`plainPattern`
#. :doc:`uniformExcitation`
#. :doc:`multiExcitation`

.. toctree::
   :maxdepth: 2
   :hidden:

   plainPattern
   uniformExcitation
   multiExcitation
