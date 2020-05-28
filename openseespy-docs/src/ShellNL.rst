.. include:: sub.txt

=======
ShellNL
=======

.. function:: element('ShellNL', eleTag,*eleNodes,secTag)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of nine element nodes, input is the typical, firstly four corner nodes counter-clockwise, then mid-side nodes counter-clockwise and finally the central node
   ``secTag`` |int|                      tag associated with previously-defined SectionForceDeformation object. currently can be a ``'PlateFiberSection'``, a ``'ElasticMembranePlateSection'`` and a ``'LayeredShell'`` section

   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ShellNL>`_
