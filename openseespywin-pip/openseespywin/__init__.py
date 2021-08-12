import ctypes
import sys

# only work for 64 bit system
if sys.maxsize < 2**31:
    raise RuntimeError('64 bit system is required')

# platform dependent
if sys.platform.startswith('win'):

    if sys.version_info[0] == 3 and sys.version_info[1] == 8:
        dll_path = ''
        for path in sys.path:
            if 'DLLs' in path:
                dll_path = path
                break
        ctypes.cdll.LoadLibrary(dll_path + '\\tcl86t.dll')

        try:
            from openseespywin.opensees import *
            from openseespywin.version import *
        except:
            raise RuntimeError('Failed to import openseespy on Windows.')
    else:
        raise RuntimeError(
            'Python version 3.8 is needed for Windows')

else:

    raise RuntimeError('This package is for Windows only')
