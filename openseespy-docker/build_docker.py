import subprocess
import shutil
import os
import os.path
import sys


def build_docker(push, upload, version):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # version
    if not version:
        about = {}
        with open('../openseespy-pip/openseespy/version.py') as fp:
            exec(fp.read(), about)
        version = about['version']

    with open('version.py', 'w') as fd:
        fd.write(f'version = "{version}"')

    # tag
    subprocess.run(['docker',
                    'build', '--target', 'ubuntu-petsc',
                    '-t', f'ubuntu-petsc', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'ubuntu-openseespy',
                    '-t', f'ubuntu-openseespy:{version}', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'ubuntu-pip',
                    '-t', f'ubuntu-pip:{version}', '.'])
    if upload:
        subprocess.run(['docker', 'container', 'run',
                        '-it', '--rm', f'ubuntu-pip:{version}',
                        '/usr/bin/python3.8', 'build_pip.py',
                        'upload-test', 'python3.8'])

    if push:
        subprocess.run(['docker',
                        'build', '--target', 'ubuntu-install',
                        '-t', f'zhuminjie/openseespy:{version}', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'ubuntu-notebook',
                        '-t', f'zhuminjie/openseespy:{version}-notebook', '.'])
        subprocess.run(['docker', 'login'])
        subprocess.run(['docker', 'image',
                        'push', tag_openseespy])
        subprocess.run(['docker', 'image',
                        'push', tag_notebook])


if __name__ == "__main__":
    push = False
    upload = False
    version = None
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == 'push':
            push = True
        elif sys.argv[i] == 'upload':
            upload = True
        else:
            l = sys.argv[i].split('.')
            num = True
            for n in l:
                if not n.isnumeric():
                    num = False
                    break
            if num:
                version = sys.argv[i]

    build_docker(push, upload, version)
