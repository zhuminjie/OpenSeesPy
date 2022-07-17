.. include:: sub.txt

===========
ShellNLDKGQ
===========

This command is used to construct a ShellNLDKGQ element object accounting for the geometric nonlinearity of large deformation using the updated Lagrangian formula, which is developed based on the ShellDKGQ element.



.. function:: element('ShellNLDKGQ', eleTag,*eleNodes,secTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of four element nodes in counter-clockwise order
   ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section

   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellNLDKGQ>`_
