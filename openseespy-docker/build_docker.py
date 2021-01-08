import subprocess
import shutil
import os
import os.path
import sys


def build_docker(version, tag, upload, test_platform, test_type, push):

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
        subprocess.run(['docker',
                        'build', '--target', 'test-centos-7.5.1804',
                        '-t', f'test-centos-7.5.1804', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'test-centos-7',
                        '-t', f'test-centos-7', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'test-centos-8',
                        '-t', f'test-centos-8', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'test-ubuntu-18.04',
                        '-t', f'test-ubuntu-18.04', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'test-ubuntu-20.04',
                        '-t', f'test-ubuntu-20.04', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'test-debian',
                        '-t', f'test-debian', '.'])
        subprocess.run(['docker',
                        'build', '--target', 'test-fedora',
                        '-t', f'test-fedora', '.'])

    # upload
    if upload:
        subprocess.run(['docker', 'container', 'run',
                        '-it', '--rm', f'centos-pip:{version}',
                        upload])

    # test different Linux systems
    if test_platform and test_type:
        if test_platform == 'test-all':
            for platform in ["test-centos-7.5.1804",
                             "test-centos-7",
                             "test-centos-8",
                             "test-ubuntu-18.04",
                             "test-ubuntu-20.04",
                             "test-debian",
                             "test-fedora"]:
                subprocess.run(['docker', 'container', 'run',
                                '-it', '--rm', platform, test_type])
        else:
            subprocess.run(['docker', 'container', 'run',
                            '-it', '--rm', test_platform, test_type])

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


'''
upload:
    "upload", "upload-test"
test-type:
    "test", "test-test"
test-platform:
    "test-centos-7.5.1804",
    "test-centos-7"
    "test-centos-8"
    "test-ubuntu-18.04"
    "test-ubuntu-20.04"
    "test-debian"
    "test-fedora"
    "test-all"
'''
# procedure:
# tag with test version
# upload-test
# test test version
# tag with release version
# upload
# test release version
if __name__ == "__main__":
    # version, tag, upload, test_platform, test_type, push
    version = None
    tag = False
    upload = False
    test_platform = None
    test_type = 'test-test'
    push = False
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == 'push':
            push = True
        elif sys.argv[i] == 'tag':
            tag = True
        elif sys.argv[i] == 'test':
            test_type = 'test'
        elif sys.argv[i].startswith('upload'):
            upload = sys.argv[i]
        elif sys.argv[i].startswith('test-'):
            test_platform = sys.argv[i]
        elif sys.argv[i].startswith('v'):
            version = sys.argv[i][1:]

    build_docker(version, tag, upload, test_platform, test_type, push)
