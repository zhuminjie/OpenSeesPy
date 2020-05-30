.. include:: sub.txt

==============
 LayeredShell
==============

.. function:: section('LayeredShell', sectionTag, nLayers, *mats)
   :noindex:

   This command will create the section of the multi-layer shell element, including the multi-dimensional concrete, reinforcement material and the corresponding thickness.

   ================================   ===========================================================================
   ``sectionTag`` |int|               unique tag among sections
   ``nLayers`` |int|                  total numbers of layers
   ``mats`` |list|                    a list of material tags and thickness, ``[[mat1,thk1], ..., [mat2,thk2]]``
   ================================   ===========================================================================
