.. include:: sub.txt

================================================================================
Bond SP01 - - Strain Penetration Model for Fully Anchored Steel Reinforcing Bars
================================================================================

.. function:: uniaxialMaterial('Bond_SP01', matTag, Fy, Sy, Fu, Su, b, R)
   :noindex:

   This command is used to construct a uniaxial material object for capturing strain penetration effects at the column-to-footing, column-to-bridge bent caps, and wall-to-footing intersections. In these cases, the bond slip associated with strain penetration typically occurs along a portion of the anchorage length. This model can also be applied to the beam end regions, where the strain penetration may include slippage of the bar along the entire anchorage length, but the model parameters should be chosen appropriately.

   This model is for fully anchored steel reinforcement bars that experience bond slip along a portion of the anchorage length due to strain penetration effects, which are usually the case for column and wall longitudinal bars anchored into footings or bridge joints

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``Fy`` |float|                        Yield strength of the reinforcement steel
   ``Sy`` |float|                        Rebar slip at member interface under yield stress. (see NOTES below)
   ``Fu`` |float|                        Ultimate strength of the reinforcement steel
   ``Su`` |float|                        Rebar slip at the loaded end at the bar fracture strength
   ``b`` |float|                         Initial hardening ratio in the monotonic slip vs. bar stress response (0.3~0.5)
   ``R`` |float|                         Pinching factor for the cyclic slip vs. bar response (0.5~1.0)
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/Bond_SP01_-_-_Strain_Penetration_Model_for_Fully_Anchored_Steel_Reinforcing_Bars>`_
