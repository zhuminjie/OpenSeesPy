import subprocess
import shutil
import os
import os.path
import sys
import glob


def update_version(version):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # pull from OpenSees main repo
    subprocess.run(['git', 'subtree', 'pull', '--prefix',
                    'opensees', 'https://github.com/OpenSees/OpenSees',
                    'master', '--squash'])

    # pull from OpenSeesPyDoc main repo
    subprocess.run(['git', 'subtree', 'pull', '--prefix',
                    'openseespy-docs',
                    'https://github.com/zhuminjie/OpenSeesPyDoc',
                    'master', '--squash'])

    # change pip version
    with open('openseespy-pip/openseespy/version.py', 'w') as fd:
        fd.write(f'version = "{version}"')
    with open('openseespylinux-pip/openseespylinux/version.py', 'w') as fd:
        fd.write(f'version = "{version}"')
    with open('openseespywin-pip/openseespywin/version.py', 'w') as fd:
        fd.write(f'version = "{version}"')

    # commit pip version
    subprocess.run(['git', 'add', 'openseespy-pip'])
    subprocess.run(['git', 'add', 'openseespylinux-pip'])
    subprocess.run(['git', 'add', 'openseespywin-pip'])
    subprocess.run(['git', 'commit', '-m',
                    f'update version {version}'])

    # push to github
    subprocess.run(['git', 'push'])

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('update_version version')
        exit()

    version = sys.argv[1]

    update_version(version)
