.. include:: sub.txt


==================
printModel command
==================

.. function:: printModel('-file',filename,'-JSON','-node','-flag',flag,*nodes=[],*eles=[])

   This command is used to print output to screen or file.

   ===========================   =====================================================================================================================================================
   ``filename`` |str|            name of file to which output is sent, by default, print to the screen. (optional)
   ``'-JSON'`` |str|             print to a JSON file. (optional)
   ``'-node'`` |str|             print node information. (optional)
   ``flag`` |int|                integer flag to be sent to the print() method, depending on the node and element type (optional)
   ``nodes`` |listi|             a list of nodes tags to be printed, default is to print all, (optional)
   ``eles`` |listi|              a list of element tags to be printed, default is to print all, (optional)
   ===========================   =====================================================================================================================================================

.. note::

   This command was called ``print`` in Tcl. Since ``print`` is a built-in function in Python, it is renamed to ``printModel``.
