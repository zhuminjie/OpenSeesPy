import subprocess
import shutil
import os
import os.path
import sys


def build_docker(version, setup, compile, upload, test_platform, test_type, push):

  # change to script's folder
  os.chdir(os.path.dirname(os.path.abspath(__file__)))

  # copy pip
  shutil.rmtree('openseespy-pip')
  shutil.copytree('../openseespy-pip', 'openseespy-pip')
  shutil.rmtree('openseespylinux-pip')
  shutil.copytree('../openseespylinux-pip', 'openseespylinux-pip')

  # copy opensees
  shutil.rmtree('opensees')
  shutil.copytree('../opensees', 'opensees')

  # version
  if not version:
    about = {}
    with open('openseespylinux-pip/openseespylinux/version.py') as fp:
      exec(fp.read(), about)
    version = about['version']

  with open('openseespylinux-pip/openseespylinux/version.py', 'w') as fd:
    fd.write(f'version = "{version}"')

  # setup environment
  if setup:
    subprocess.run(['docker',
                    'build', '--target', 'centos-packages',
                    '-t', f'centos-packages', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'centos-petsc',
                    '-t', f'centos-petsc', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'centos-openseespy-code',
                    '-t', f'centos-openseespy-code:{version}', '.'])

  # compile
  if compile:
    subprocess.run(['docker',
                    'build', '--target', 'centos-openseespy',
                    '-t', f'centos-openseespy:{version}', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'centos-pip',
                    '-t', f'centos-pip:{version}', '.'])
    subprocess.run(['docker',
                    'build', '--target', 'centos-pip-bash',
                    '-t', f'centos-pip-bash', '.'])
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
                    'build', '--target', 'test-ubuntu-16.04',
                    '-t', f'test-ubuntu-16.04', '.'])
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
    # subprocess.run(['docker', 'image',
    #                 'push', tag_openseespy])
    # subprocess.run(['docker', 'image',
    #                 'push', tag_notebook])


# commands:
#
# test and test-platform can be mixed
# version can be ignored, then
# the version in version.py is used
#
# manually set the version number
# build_docker v#.#.#.#
#
# create all docker images needed
# build_docker setup
#
# compile openseespy and build pip
# build_docker compile
#
# upload the package to testpypi
# build_docker upload-test
#
# upload the package to pypi
# build_docker upload
#
# test the package from testpypi
# build_docker test-test
#
# test the package from pypi
# build_docker test
#
# clear the docker
# build_docker clear
#
# test the package on a platform
# build_docker test-all
# build_docker test-centos-7.5.1804
# build_docker test-centos-7
# build_docker test-centos-8
# build_docker test-ubuntu-16.04
# build_docker test-ubuntu-18.04
# build_docker test-ubuntu-20.04
# build_docker test-debian
# build_docker test-dedora
#
if __name__ == "__main__":
  # version, tag, upload, test_platform, test_type, push
  version = None
  setup = False
  compile = False
  upload = False
  test_platform = None
  test_type = 'test-test'
  push = False
  for i in range(1, len(sys.argv)):
    if sys.argv[i] == 'push':
      push = True
    elif sys.argv[i] == 'setup':
      setup = True
    elif sys.argv[i] == 'compile':
      compile = True
    elif sys.argv[i] == 'test':
      test_type = 'test'
    elif sys.argv[i].startswith('upload'):
      upload = sys.argv[i]
    elif sys.argv[i].startswith('test-'):
      test_platform = sys.argv[i]
    elif sys.argv[i].startswith('v'):
      version = sys.argv[i][1:]
    elif sys.argv[i] == 'clear':
      subprocess.run(['docker',
                      'system', 'prune', '-a', ])

  build_docker(version, setup, compile, upload, test_platform, test_type, push)
