.. include:: sub.txt

=========================
Twenty Node Brick Element
=========================

The element is used to construct a twenty-node three dimensional element object



.. function:: element('20NodeBrick', eleTag,*eleNodes,matTag, bf1, bf2, bf3, massDen)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of twenty element nodes, input order is shown in notes below
   ``matTag`` |int|                      material tag associated with previsouly-defined NDMaterial object
   ``bf1``  ``bf2``  ``bf3`` |float|     body force in the direction of global coordinates x, y and z
   ``massDen`` |float|                   mass density (mass/volume)
   ===================================   ===========================================================================

.. note::

   The valid queries to a 20NodeBrick element when creating an ElementRecorder object are 'force,' 'stiffness,' stress', 'gausspoint' or 'plastic'. The output is given as follows:



   #. 'stress'

      the six stress components from each Gauss points are output by the order: sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_xz,sigma_yz

   #. 'gausspoint'

      the coordinates of all Gauss points are printed out

   #. 'plastic'

      the equivalent deviatoric plastic strain from each Gauss point is output in the same order as the coordinates are printed

.. seealso::


   `Notes <http://opensees.berkeley.edu/OpenSees/manuals/usermanual/734.htm>`_
