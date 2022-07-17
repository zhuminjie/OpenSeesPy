.. include:: sub.txt

.. _PVDRecorder:
   
====================
pvd recorder command
====================

.. function:: recorder('PVD',filename,'-precision',precision=10,'-dT',dT=0.0,*res)
   :noindex:

   Create a PVD recorder.

   ========================   =============================================================
   ``filename`` |str|         the name for ``filename.pvd`` and ``filename/`` directory,
                              which must pre-exist.
   ``precision`` |int|        the precision of data. (optional)
   ``dT`` |float|             the time interval for recording. (optional)
   ``res`` |lists|            a list of |str| of responses to be recorded, (optional)

                              * ``'disp'``
			      * ``'vel'``
			      * ``'accel'``
			      * ``'incrDisp'``
			      * ``'reaction'``
			      * ``'pressure'``
			      * ``'unbalancedLoad'``
			      * ``'mass'``
			      * ``'eigen'``
   ========================   =============================================================

