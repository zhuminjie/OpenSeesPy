import subprocess

from build_pip import copy_library, build_pip, upload_pip_test, clean_pip


copy_library('../OpenSees/SRC/interpreter/opensees.so',
             '../OpenSees/SRC/interpreter/opensees.pyd')
build_pip()
upload_pip_test()
clean_pip()