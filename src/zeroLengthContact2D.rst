.. include:: sub.txt

=========================
zeroLengthContact Element
=========================

.. function:: element('zeroLengthContact2D', eleTag,*eleNodes,Kn, Kt, mu, '-normal', Nx, Ny)
   :noindex:

   This command is used to construct a zeroLengthContact2D element, which is Node-to-node frictional contact element used in two dimensional analysis and three dimensional analysis:



   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of a constrained and a retained nodes
   ``Kn`` |float|                        Penalty in normal direction
   ``Kt`` |float|                        Penalty in tangential direction
   ``mu`` |float|                        friction coefficient
   ===================================   ===========================================================================


.. function:: element('zeroLengthContact3D', eleTag,*eleNodes,Kn, Kt, mu, c, dir)
   :noindex:

   This command is used to construct a zeroLengthContact3D element, which is Node-to-node frictional contact element used in two dimensional analysis and three dimensional analysis:



   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of a constrained and a retained nodes
   ``Kn`` |float|                        Penalty in normal direction
   ``Kt`` |float|                        Penalty in tangential direction
   ``mu`` |float|                        friction coefficient
   ``c`` |float|                         cohesion (not available in 2D)
   ``dir`` |int|                         Direction flag of the contact plane (3D), it can be:

                                         * 1 Out normal of the master plane pointing to +X direction
					 * 2 Out normal of the master plane pointing to +Y direction
					 * 3 Out normal of the master plane pointing to +Z direction
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContact_Element>`_
