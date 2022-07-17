.. include:: sub.txt

==============
record command
==============

.. function:: record()

   This command is used to cause all the recorders to do a record on the current state of the model.


.. note:: 
   A record is issued after every successfull static or transient analysis step. Sometimes the user may need the record to be issued on more occasions than this, 
   for example if the user is just looking to record the eigenvectors after an eigen command or for example the user wishes to include the state of the model 
   at time 0.0 before any analysis has been completed.