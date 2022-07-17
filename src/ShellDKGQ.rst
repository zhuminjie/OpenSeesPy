.. include:: sub.txt

=========
ShellDKGQ
=========

This command is used to construct a ShellDKGQ element object, which is a quadrilateral shell element based on the theory of generalized conforming element.



.. function:: element('ShellDKGQ', eleTag,*eleNodes,secTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. Currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellDKGQ>`_
