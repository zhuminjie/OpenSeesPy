import subprocess
import shutil
import os
import os.path
import sys
import glob


def copy_linux_library(so, copy_dep=True):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # replace new libraries
    linux = './openseespy/opensees/linux/'

    if os.path.exists(so):
        if os.path.exists(linux+'opensees.so'):
            os.remove(linux+'opensees.so')
        shutil.copy(so, linux)

        if copy_dep:
            # get dependent library for linux
            p = subprocess.run(
                ["ldd", so], capture_output=True)

            for line in p.stdout.decode('utf-8').split('\n'):
                i = line.find('/')
                j = line.find(' ', i)
                if i < 0 or j < 0 or i >= j:
                    continue

                find = False
                if line[i:j].find('gfortran') >= 0:
                    find = True
                elif line[i:j].find('blas') >= 0:
                    find = True
                elif line[i:j].find('stdc++') >= 0:
                    find = True
                elif line[i:j].find('gcc') >= 0:
                    find = True
                elif line[i:j].find('quadmath') >= 0:
                    find = True
                elif line[i:j].find('gomp') >= 0:
                    find = True
                elif line[i:j].find('mpi') >= 0:
                    find = True

                if find:
                    print('copying '+line[i:j]+' to '+linux+'lib/')
                    shutil.copy(line[i:j], linux+'lib/')


def copy_win_library(pyd):
    win = './openseespy/opensees/win/'
    if os.path.exists(pyd):
        if os.path.exists(win+'opensees.pyd'):
            os.remove(win+'opensees.pyd')
        shutil.copy(pyd, win)


def copy_mac_library(so):

    mac = './openseespy/opensees/mac/'
    if os.path.exists(so):
        if os.path.exists(mac+'opensees.so'):
            os.remove(mac+'opensees.so')
        # for f in glob.glob(mac+'lib/*.dylib'):
        #     os.remove(f)

        shutil.copy(so, mac)

        # get dependent library for linux
        # p = subprocess.run(
        #     ["otool", "-L", so], capture_output=True)

        # for line in p.stdout.decode('utf-8').split('\n'):
        #     i = line.find('/')
        #     j = line.find(' ', i)
        #     if i < 0 or j < 0 or i >= j:
        #         continue

        #     print('copying '+line[i:j]+' to '+mac+'lib/')
        #     shutil.copy(line[i:j], mac+'lib/')
        #     lib_name = line[i:j].split('/')
        #     lib_name = lib_name[-1]
        #     if lib_name == 'Python':
        #         continue
        #     print('changing rpath from '+line[i:j]+' to lib/'+lib_name)
        #     subprocess.run(
        #         ['install_name_tool', '-change', line[i:j],
        #             '@loader_path/lib/'+lib_name, mac+'opensees.so']
        #     )

        # if os.path.exists(mac+'lib/Python'):
        #     os.remove(mac+'lib/Python')


def build_pip(pyexe='python', use_zip=False):

    # clean folders
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])

    # update tools
    subprocess.run([pyexe, '-m', 'pip', 'install', '--upgrade',
                    'setuptools', 'wheel', 'twine', 'pytest'])

    # compile wheel
    if use_zip:
        subprocess.run([pyexe, 'setup.py', 'bdist', '--format=zip'])
    else:
        subprocess.run([pyexe, 'setup.py', 'bdist_wheel'])


def upload_pip(pyexe='python'):
    # upload
    subprocess.run([pyexe, '-m', 'twine', 'upload', 'dist/*'])


def clean_pip():
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])


def upload_pip_test(pyexe='python'):
    # upload
    subprocess.run([pyexe, '-m', 'twine', 'upload',
                    '--repository', 'testpypi', 'dist/*'])


def install_pip_test(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run([pyexe, '-m', 'pip',  'install', '--pre', '--no-cache-dir', '--index-url',
                    'https://test.pypi.org/simple/', 'openseespy'])


def install_pip(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespy'])
    subprocess.run([pyexe, '-m', 'pip', 'install',
                    '--pre', '--no-cache-dir', 'openseespy'])

# commands:
#
# pyexe - python excutable
#
# build pip
# build_pip pyexe build use_zip/no_zip
# use_zip - build the package to a zip file
# no_zip - build the package to a wheel file
#
# upload to testpypi
# build_pip pyexe upload-test
#
# upload to pypi
# build_pip pyexe upload
#
# test package from testpypi
# build_pip pyexe test-test
#
# test package from pypi
# build_pip pyexe test
#

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('build_pip pyexe cmd')
        exit()

    pyexe = sys.argv[1]

    if sys.argv[2] == 'build':
        if len(sys.argv) < 4:
            print('buld_pip pyexe build use_zip/no_zip')
            exit()

        use_zip = False
        if sys.argv[3] == 'use_zip':
            use_zip = True

        # copy_linux_library(so, copy_dep=copy_dep)
        # copy_win_library(pyd)
        # copy_mac_library(macso)
        build_pip(pyexe, use_zip=use_zip)

    elif sys.argv[2] == 'upload-test':

        if len(sys.argv) < 3:
            print('buld_pip pyexe upload-test')
            exit()
        upload_pip_test(pyexe)

    elif sys.argv[2] == 'upload':

        if len(sys.argv) < 3:
            print('buld_pip pyexe upload')
            exit()

        upload_pip(pyexe)

    elif sys.argv[2] == 'test-test':

        if len(sys.argv) < 3:
            print('buld_pip pyexe test-test')
            exit()

        install_pip_test(pyexe)
        subprocess.run(['pytest', '--pyargs', 'openseespy.test'])

    elif sys.argv[2] == 'test':

        if len(sys.argv) < 3:
            print('buld_pip pyexe test')
            exit()

        install_pip(pyexe)
        subprocess.run(['pytest', '--pyargs', 'openseespy.test'])
