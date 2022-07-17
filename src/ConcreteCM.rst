.. include:: sub.txt

==================
 ConcreteCM
==================

.. function:: uniaxialMaterial('ConcreteCM', matTag, fpcc, epcc, Ec, rc, xcrn, ft, et, rt, xcrp, mon, '-GapClose', GapClose=0)
   :noindex:

   This command is used to construct a uniaxialMaterial ConcreteCM (Kolozvari et al., 2015), which is a uniaxial hysteretic constitutive model for concrete developed by Chang and Mander (1994).

   ===================================   ===========================================================================
   ``matTag`` |int|                      integer tag identifying material
   ``fpcc`` |float|                      Compressive strength (:math:`f'_c`)
   ``epcc`` |float|                      Strain at compressive strength (:math:`\epsilon'_c`)
   ``Ec`` |float|                        Initial tangent modulus (:math:`E_c`)
   ``rc`` |float|                        Shape parameter in Tsai's equation defined for compression (:math:`r_c`)
   ``xcrn`` |float|                      Non-dimensional critical strain on compression
                                         envelope (:math:`\epsilon^{-}_{cr}`, where the envelope
					 curve starts following a straight line)
   ``ft`` |float|                        Tensile strength (:math:`f_t`)
   ``et`` |float|                        Strain at tensile strength (:math:`\epsilon_t`)
   ``rt`` |float|                        Shape parameter in Tsai's equation defined for tension (:math:`r_t`)
   ``xcrp`` |float|                      Non-dimensional critical strain on tension envelope
                                         (:math:`\epsilon^{+}_{cr}`, where the envelope curve
					 starts following a straight line - large value
					 [e.g., 10000] recommended when tension stiffening
					 is considered)
   ``mon``                               optional, monotonic stress-strain relationship only:  mon=1 (invoked in FSAM only), mon=0 (no impact since monotonic)
   ``'-GapClose'`` |str|                 optional, denote next parameter is ``GapClose``
   ``GapClose`` |float|                  optional, GapClose = 0, less gradual gap closure (default);
                                         GapClose = 1, more gradual gap closure
   ===================================   ===========================================================================

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ConcreteCM_-_Complete_Concrete_Model_by_Chang_and_Mander_(1994)>`_
