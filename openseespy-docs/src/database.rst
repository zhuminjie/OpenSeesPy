.. include:: sub.txt


================
database command
================

.. function:: database(type, dbName)

   Create a database.

   ===========================   =====================================================================================================================================================
   ``type`` |str|                database type:

	                         * ``'File'`` - outputs database into a file
				 * ``'MySQL'`` - creates a SQL database
				 * ``'BerkeleyDB'`` - creates a BerkeleyDB database
   ``dbName`` |str|              database name.
   ===========================   =====================================================================================================================================================
