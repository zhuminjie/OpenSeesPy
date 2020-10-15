import subprocess
import sys

from build_pip import install_pip

pyexe = 'python'
if sys.platform.startswith('darwin'):
    pyexe = 'python3'

install_pip(pyexe)

subprocess.run(
    ['pytest', '--pyargs', 'openseespy.test']
)
