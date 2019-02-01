import sys

# only work for 64 bit system
if sys.maxsize < 2**31:
    raise RuntimeError('64 bit system is required')

# python 3.6 is required
if sys.version_info[0] < 3:
    raise RuntimeError('Python version >= 3.6 is required')

if sys.version_info[1] < 6:
    raise RuntimeError('Python version >= 3.6 is required')

# platform dependent
if sys.platform.startswith('linux'):

    from openseespy.opensees.linux.opensees import *

elif sys.platform.startswith('win'):

    if sys.version_info[1] == 6:

        from openseespy.opensees.winpy36.opensees import *

    else:

        from openseespy.opensees.winpy37.opensees import *

elif sys.platform.startswith('darwin'):

    raise RuntimeError('Mac OS X is not supported yet')


else:

    raise RuntimeError(sys.platform+' is not supported yet')


