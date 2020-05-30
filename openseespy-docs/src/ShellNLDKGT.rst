.. include:: sub.txt

===========
ShellNLDKGT
===========

This command is used to construct a ShellNLDKGT element object accounting for the geometric nonlinearity of large deformation using the updated Lagrangian formula, which is developed based on the ShellDKGT element.


.. function:: element('ShellNLDKGT', eleTag,*eleNodes,secTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of three element nodes in clockwise or counter-clockwise order around the element
   ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellNLDKGT>`_
