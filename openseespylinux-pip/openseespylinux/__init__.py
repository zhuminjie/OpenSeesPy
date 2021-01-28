
import sys

# only work for 64 bit system
if sys.maxsize < 2**31:
    raise RuntimeError('64 bit system is required')

# platform dependent
if sys.platform.startswith('linux'):

    try:
        from openseespylinux.opensees import *
        from openseespylinux.version import *
    except:
        raise RuntimeError('Failed to import openseespy on Linux.')

else:

    raise RuntimeError('This package is for Linux only.')
