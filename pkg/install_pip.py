import subprocess

from build_pip import copy_library, build_pip, upload_pip, clean_pip

copy_library('../OpenSeesPy/SRC/interpreter/opensees.so',
             '../OpenSeesPy/SRC/interpreter/opensees.pyd')
build_pip()
upload_pip()
clean_pip()
