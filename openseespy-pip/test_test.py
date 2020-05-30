import subprocess

from build_pip import install_pip_test

install_pip_test()

subprocess.run(
    ['pytest', '--pyargs', 'openseespy.test']
)
