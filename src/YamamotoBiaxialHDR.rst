.. include:: sub.txt

==========================
YamamotoBiaxialHDR Element
==========================


This command is used to construct a YamamotoBiaxialHDR element object, which is defined by two nodes. This element can be used to represent the isotropic behavior of high-damping rubber bearing in the local y-z plane.


.. function:: element('YamamotoBiaxialHDR', eleTag,*eleNodes,Tp, DDo, DDi, Hr,<'-coRS`, cr, cs>,<'-orient`, *vecx, *vecyp>,<'-mass`, m>)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``Tp`` |int|                          compound type = 1 : X0.6R manufactured by Bridgestone corporation.
   ``DDo`` |float|                       outer diameter [m]
   ``DDi`` |float|                       bore diameter [m]
   ``Hr`` |float|                        total thickness of rubber layer [m] Optional Data
   ``cr``  ``cs`` |float|                coefficients for shear stress components of tau_r and tau_s
   ``vecx`` |listf|                      a list of vector components in global coordinates defining local x-axis (optional)
   ``vecyp`` |listf|                     a list of vector components in global coordinates defining vector yp which lies in the local x-y plane for the element.
   ``m`` |float|                         element mass [kg]
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/YamamotoBiaxialHDR_Element>`_
