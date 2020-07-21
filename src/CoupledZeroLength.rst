.. include:: sub.txt

=========================
CoupledZeroLength Element
=========================

.. function:: element('CoupledZeroLength', eleTag,*eleNodes, dirn1, dirn2, matTag, <rFlag=1>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``matTag`` |float|                    tags associated with previously-defined UniaxialMaterial
   ``dirn1``  ``dirn2`` |int|              the two directions, 1 through ndof.
   ``rFlag`` |float|                     optional, default = 0

                                         * ``rFlag`` = 0 NO RAYLEIGH DAMPING (default)
					 * ``rFlag`` = 1 include rayleigh damping

   ===================================   ===========================================================================

.. seealso::


   `Notes <dhttp://opensees.berkeley.edu/wiki/index.php/CoupledZeroLength_Element>`_
