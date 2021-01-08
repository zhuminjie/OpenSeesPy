import subprocess
import shutil
import os
import os.path
import sys


def build_docker(push, upload_test, tag, test, version):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # copy pip
    if not os.path.exists('openseespy-pip'):
        shutil.copytree('../openseespy-pip', 'openseespy-pip')

    # copy opensees
    if not os.path.exists('opensees'):
        shutil.copytree('../opensees', 'opensees')

    # version
    if not version:
        about = {}
        with open('openseespy-pip/openseespy/version.py') as fp:
            exec(fp.read(), about)
        version = about['version']

    with open('openseespy-pip/openseespy/version.py', 'w') as fd:
        fd.write(f'version = "{version}"')

    # tag
    if tag:
        subprocess.run(['docker',
                        'build', '--target', 'centos-packages',
                        '-t', f'centos-packages', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'centos-petsc',
                        '-t', f'centos-petsc', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'centos-openseespy',
                        '-t', f'centos-openseespy:{version}', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'centos-pip',
                        '-t', f'centos-pip:{version}', '.'])

    # upload to test.pypi
    if upload_test:
        subprocess.run(['docker', 'container', 'run',
                        '-it', '--rm', f'centos-pip:{version}',
                        'python3.8', 'build_pip.py',
                        'upload-test', 'python3.8'])

    # test different Linux systems
    if test:
        subprocess.run(['docker',
                        'build', '--target', test, '-t', test, '.'])

    # push to dockerHub
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
    upload_test = False
    version = None
    tag = False
    test = None
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == 'push':
            push = True
        elif sys.argv[i] == 'upload-test':
            upload_test = True
        elif sys.argv[i] == 'tag':
            tag = True
        elif sys.argv[i].startswith('test'):
            test = sys.argv[i]
        elif sys.argv[i].startswith('v'):
            version = sys.argv[i][1:]

    build_docker(push, upload_test, tag, test, version)
