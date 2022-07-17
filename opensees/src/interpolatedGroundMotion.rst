.. include:: sub.txt

============================
 Interpolated Ground Motion
============================

.. function:: groundMotion(gmTag,'Interpolated',*gmTags,'-fact',facts)
   :noindex:

   This command is used to construct an interpolated GroundMotion object, where the motion is determined by combining several previously defined ground motions in the load pattern.


   ========================   =============================================================
   ``gmTag`` |int|            unique tag among ground motions in load pattern
   ``gmTags`` |listi|         the tags of existing ground motions in pattern to be used for interpolation
   ``facts`` |listf|          the interpolation factors. (optional)
   ========================   =============================================================
