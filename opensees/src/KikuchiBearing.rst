.. include:: sub.txt

======================
KikuchiBearing Element
======================

This command is used to construct a KikuchiBearing element object, which is defined by two nodes. This element consists of multiple shear spring model (MSS) and multiple normal spring model (MNS).



.. function:: element('KikuchiBearing', eleTag,*eleNodes,'-shape', shape,'-size', size, totalRubber, <'-totalHeight', totalHeight>,'-nMSS', nMSS,'-matMSS', matMSSTag, <'-limDisp', limDisp>,'-nMNS', nMNS,'-matMNS', matMNSTag, <'-lambda', lambda>, <'-orient',<x1, x2, x3>, yp1, yp2, yp3>, <'-mass', m>, <'-noPDInput'>, <'-noTilt'>, <'-adjustPDOutput', ci, cj>, <'-doBalance', limFo, limFi, nIter>)
   :noindex:

   ===========================================   ===========================================================================
   ``eleTag`` |int|                              unique element object tag
   ``eleNodes`` |listi|                          a list of two element nodes
   ``shape`` |float|                             following shapes are available: round, square
   ``size`` |float|                              diameter (round shape), length of edge (square shape)
   ``totalRubber`` |float|                       total rubber thickness
   ``totalHeight`` |float|                       total height of the bearing (defaulut: distance between iNode and jNode)
   ``nMSS`` |int|                                number of springs in MSS = nMSS
   ``matMSSTag`` |int|                           matTag for MSS
   ``limDisp`` |float|                           minimum deformation to calculate equivalent coefficient of MSS (see note 1)
   ``nMNS`` |int|                                number of springs in MNS = nMNS*nMNS (for round and square shape)
   ``matMNSTag`` |int|                           matTag for MNS
   ``lambda`` |float|                            parameter to calculate compression modulus distribution on MNS (see note 2)
   ``x1``  ``x2``  ``x3`` |float|                vector components in global coordinates defining local x-axis
   ``yp1``  ``yp2``  ``yp3`` |float|             vector components in global coordinates defining vector yp which lies in the local x-y plane for the element
   ``m`` |float|                                 element mass
   ``'-noPDInput'`` |str|                        not consider P-Delta moment
   ``'-noTilt'`` |str|                           not consider tilt of rigid link
   ``ci``  ``cj`` |float|                        P-Delta moment adjustment for reaction force (default:    ``ci`` =0.5,    ``cj`` =0.5)
   ``limFo``  ``limFi``  ``nIter`` |float|       tolerance of external unbalanced force (   ``limFo``), tolorance of internal unbalanced force (   ``limFi``), number of iterations to get rid of internal unbalanced force (   ``nIter``)
   ===========================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/KikuchiBearing_Element>`_
