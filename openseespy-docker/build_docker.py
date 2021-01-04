import subprocess
import shutil
import os
import os.path
import sys


def build_docker(push=False):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # version
    about = {}
    with open('../openseespy-pip/openseespy/version.py') as fp:
        exec(fp.read(), about)
    version = about['version']

    # tag
    subprocess.run(['docker',
                    'build', '--target', 'ubuntu-petsc',
                    '-t', f'ubuntu-petsc:{version}', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'ubuntu-openseespy',
                    '-t', f'ubuntu-openseespy:{version}', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'ubuntu-pip',
                    '-t', f'ubuntu-pip:{version}', '.'])
    # subprocess.run(['docker',
    #                 'build', '--target', 'ubuntu-install',
    #                 '-t', f'zhuminjie/openseespy:{version}', '.'])
    # subprocess.run(['docker',
    #                 'build', '--target', 'ubuntu-notebook',
    #                 '-t', f'zhuminjie/openseespy:{version}-notebook', '.'])

    # if push:
    #     subprocess.run(['docker', 'login'])
    #     subprocess.run(['docker', 'image',
    #                     'push', tag_openseespy])
    #     subprocess.run(['docker', 'image',
    #                     'push', tag_notebook])


if __name__ == "__main__":
    push = False
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == 'push':
            push = True
    build_docker(push)
