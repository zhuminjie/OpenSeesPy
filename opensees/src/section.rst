.. include:: sub.txt

==================
 section commands
==================

.. function:: section(secType, secTag, *secArgs)

   This command is used to construct a SectionForceDeformation object, hereto referred to as Section, which represents force-deformation (or resultant stress-strain) relationships at beam-column and plate sample points.

   ================================   ===========================================================================
   ``secType`` |str|                  section type
   ``secTag`` |int|                   section tag.
   ``secArgs`` |list|                 a list of section arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   secType = 'Elastic'
   secTag = 1
   secArgs = [E, A, Iz]
   section(secType, secTag, *secArgs)



The following contain information about available ``secType``:

#. :doc:`elasticSection`
#. :doc:`fibersection`
#. :doc:`ndfiber`
#. :doc:`wfsection2d`
#. :doc:`rcsection2d`
#. :doc:`rccircularsection`
#. :doc:`parallelsection`
#. :doc:`sectionaggregator`
#. :doc:`uniaxialsection`
#. :doc:`elasticMembranePlateSection`
#. :doc:`plateFiberSection`
#. :doc:`bidirectionalSection`
#. :doc:`isolatorsection`
#. :doc:`LayeredShell`

.. toctree::
   :maxdepth: 2
   :hidden:

   elasticSection
   fibersection
   fiberThermalsection
   ndfiber
   wfsection2d
   rcsection2d
   rccircularsection
   parallelsection
   sectionaggregator
   uniaxialsection
   elasticMembranePlateSection
   plateFiberSection
   bidirectionalSection
   isolatorsection
   LayeredShell
