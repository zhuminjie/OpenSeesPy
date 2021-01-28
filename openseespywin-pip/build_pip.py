import subprocess
import shutil
import os
import os.path
import sys
import glob


def copy_win_library(pyd):

    # change to script's folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # replace new libraries
    win = './openseespywin/'

    if os.path.exists(pyd):
        if os.path.exists(win+'opensees.pyd'):
            os.remove(win+'opensees.pyd')
        shutil.copy(pyd, win)


def build_pip(pyexe='python', use_zip=False):

    # clean folders
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespywin.egg-info'])

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
    subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespywin.egg-info'])


def upload_pip_test(pyexe='python'):
    # upload
    subprocess.run([pyexe, '-m', 'twine', 'upload',
                    '--repository', 'testpypi', 'dist/*'])


def install_pip_test(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespywin'])
    subprocess.run([pyexe, '-m', 'pip',  'install', '--pre', '--no-cache-dir', '--index-url',
                    'https://test.pypi.org/simple/', 'openseespywin'])


def install_pip(pyexe='python'):
    subprocess.run([pyexe, '-m', 'pip', 'uninstall', '-y', 'openseespywin'])
    subprocess.run([pyexe, '-m', 'pip', 'install',
                    '--pre', '--no-cache-dir', 'openseespywin'])


# commands:
#
# pyexe - python excutable
#
# build pip
# build_pip pyexe build pyd use_zip/no_zip
# pyd - path to opensees.pyd
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
        if len(sys.argv) < 5:
            print('buld_pip pyexe build pyd use_zip/no_zip')
            exit()

        pyd = sys.argv[3]
        use_zip = False
        if sys.argv[4] == 'use_zip':
            use_zip = True

        clean_pip()
        copy_win_library(pyd)
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
        subprocess.run(['pytest', '--pyargs', 'openseespywin.test'])

    elif sys.argv[2] == 'test':

        if len(sys.argv) < 3:
            print('buld_pip pyexe test')
            exit()

        install_pip(pyexe)
        subprocess.run(['pytest', '--pyargs', 'openseespywin.test'])
