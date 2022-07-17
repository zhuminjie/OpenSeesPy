.. include:: sub.txt

=========
ShellDKGT
=========

This command is used to construct a ShellDKGT element object, which is a triangular shell element based on the theory of generalized conforming element.


.. function:: element('ShellDKGT', eleTag,*eleNodes,secTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of three element nodes in clockwise or counter-clockwise order
   ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellDKGT>`_
