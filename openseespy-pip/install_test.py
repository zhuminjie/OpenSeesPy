import subprocess

from build_pip import copy_linux_library, build_pip, upload_pip_test, clean_pip


copy_linux_library('../../opensees/SRC/interpreter/opensees.so')
build_pip()
upload_pip_test()
clean_pip()
