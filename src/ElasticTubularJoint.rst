.. include:: sub.txt

===========================
ElasticTubularJoint Element
===========================

This command is used to construct an ElasticTubularJoint element object, which models joint flexibility of tubular joints in two dimensional analysis of any structure having tubular joints.



.. function:: element('ElasticTubularJoint', eleTag,*eleNodes,Brace_Diameter, Brace_Angle, E, Chord_Diameter, Chord_Thickness, Chord_Angle)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of two element nodes
   ``Brace_Diameter`` |float|            outer diameter of brace
   ``Brace_Angle`` |float|               angle between brace and chord axis 0 < Brace_Angle < 90
   ``E`` |float|                         Young's Modulus
   ``Chord_Diameter`` |float|            outer diameter of chord
   ``Chord_Thickness`` |float|           thickness of chord
   ``Chord_Angle`` |float|               angle between chord axis and global x-axis 0 < Chord_Angle < 180
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ElasticTubularJoint_Element>`_
