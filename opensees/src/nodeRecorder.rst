.. include:: sub.txt

   
=====================
node recorder command
=====================

.. function:: recorder('Node','-file',filename,'-xml',filename,'-binary',filename,'-tcp',inetAddress,port,'-precision',nSD=6,'-timeSeries',tsTag,'-time','-dT',deltaT=0.0,'-closeOnWrite','-node',*nodeTags=[],'-nodeRange',startNode,endNode,'-region',regionTag,'-dof',*dofs=[],respType)
   :noindex:

   The Node recorder type records the response of a number of nodes at every converged step.

   ===========================   =====================================================================================================================================================
   ``filename`` |str|            name of file to which output is sent. file output is either in xml format (``'-xml'`` option), 
                                 textual (``'-file'`` option) or binary (``'-binary'`` option) which must pre-exist.
   ``inetAddr`` |str|            ip address, "xx.xx.xx.xx", of remote machine to which data is sent. (optional)
   ``port`` |int|                port on remote machine awaiting tcp. (optional)
   ``nSD`` |int|                 number of significant digits (optional)
   ``'-time'`` |str|             using this option places domain time in first entry of each data line, default is to have time ommitted, (optional)
   ``'-closeOnWrite'`` |str|     using this option will instruct the recorder to invoke a close on the data handler after every timestep. 
                                 If this is a file it will close the file on every step and then re-open it for the next step. 
                                 Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) 
   ``deltaT`` |float|            time interval for recording. will record when next step is ``deltaT`` greater than last recorder step. 
                                 (optional, default: records at every time step)
   ``tsTag`` |int|               the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional)  
   ``nodeTags`` |listi|          list of tags of nodes whose response is being recorded (optional)
   ``startNode`` |int|           tag for start node whose response is being recorded (optional)
   ``endNode`` |int|             tag for end node whose response is being recorded (optional)     
   ``regionTag`` |int|           a region tag; to specify all nodes in the previously defined region. (optional)
   ``dofs`` |listi|              the specified dof at the nodes whose response is requested.                                            
   ``resType`` |lists|           a string indicating response required. Response types are given in table below
   
                                 * ``'disp'``     displacement
                                 * ``'vel'``      velocity
                                 * ``'accel'``    acceleration
                                 * ``'incrDisp'`` incremental displacement
                                 * ``'reaction'`` nodal reaction
                                 * ``'eigen i'``  eigenvector for mode i
                                 * ``'rayleighForces'`` damping forces
   ===========================   =====================================================================================================================================================

.. note::

   Only one of ``'-file'``, ``'-xml'``, ``'-binary'``, ``'-tcp'`` will be used. If multiple specified last option is used.
