.. include:: sub.txt

.. _BgPVDRecorder:
   
===========================
background recorder command
===========================

.. function:: recorder('BgPVD',filename,'-precision',precision=10,'-dT',dT=0.0,*res)
   :noindex:

   Create a PVD recorder for background mesh. This recorder is same as the
   PVD recorder, but will be automatically called in background mesh and
   is able to record wave height and velocity.

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

