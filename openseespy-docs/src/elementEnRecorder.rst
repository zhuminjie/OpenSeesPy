.. include:: sub.txt

   
=================================
element envelope recorder command
=================================

.. function:: recorder('EnvelopeElement','-file',filename,'-xml',filename,'-binary',filename,'-precision',nSD=6,'-timeSeries',tsTag,'-time','-dT',deltaT=0.0,'-closeOnWrite','-ele',*eleTags=[],'-eleRange',startEle,endEle,'-region',regionTag,*args)
   :noindex:

   The Envelope Element recorder type records the response of a number of elements at every converged step. The response recorded is element-dependent and also depends on the arguments which are passed to the setResponse() element method. When the object is terminated, through the use of a wipe, exit, or remove the object will output the min, max and absolute max values on 3 seperate lines of the output file for each quantity.

   ===========================   =====================================================================================================================================================
   ``filename`` |str|            name of file to which output is sent. file output is either in xml format (``'-xml'`` option), 
                                 textual (``'-file'`` option) or binary (``'-binary'`` option) which must pre-exist.
   ``nSD`` |int|                 number of significant digits (optional)
   ``'-time'`` |str|             using this option places domain time in first entry of each data line, default is to have time ommitted, (optional)
   ``'-closeOnWrite'`` |str|     using this option will instruct the recorder to invoke a close on the data handler after every timestep. 
                                 If this is a file it will close the file on every step and then re-open it for the next step. 
                                 Note, this greatly slows the execution time, but is useful if you need to monitor the data during the analysis. (optional) 
   ``deltaT`` |float|            time interval for recording. will record when next step is ``deltaT`` greater than last recorder step. 
                                 (optional, default: records at every time step)
   ``tsTag`` |int|               the tag of a previously constructed TimeSeries, results from node at each time step are added to load factor from series (optional)  
   ``eleTags`` |listi|           list of tags of elements whose response is being recorded (optional)
   ``startEle`` |int|            tag for start node whose response is being recorded (optional)
   ``endEle`` |int|              tag for end node whose response is being recorded (optional)     
   ``regionTag`` |int|           a region tag; to specify all nodes in the previously defined region. (optional)
   ``args`` |list|               arguments which are passed to the setResponse() element method
   ===========================   =====================================================================================================================================================

.. note::

   The setResponse() element method is dependent on the element type, and is described with the :meth:`element` Command.
