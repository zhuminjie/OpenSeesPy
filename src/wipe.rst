.. include:: sub.txt

==============
 wipe command
==============

.. function:: wipe()

   This command is used to destroy all constructed objects, i.e. all components of the model, all components of the analysis and all recorders.

   This command is used to start over without having to exit and restart the interpreter. It causes all elements, nodes, constraints, loads to be removed from the domain. In addition it deletes all recorders, analysis objects and all material objects created by the model builder.
