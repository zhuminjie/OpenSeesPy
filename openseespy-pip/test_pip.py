import subprocess

from build_pip import install_pip

install_pip()

subprocess.run(
    ['pytest', '--pyargs', 'openseespy.test']
)
