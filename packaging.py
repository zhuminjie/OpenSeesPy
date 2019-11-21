import subprocess


print('updating setuptools, wheel twine...')
subprocess.run(['python3.7', '-m', 'pip', 'install', '--upgrade', 'setuptools', 'wheel', 'twine'])

print('removing build/ dist/ openseespy.egg-info/')
subprocess.run(['rm', '-fr', 'build', 'dist', 'openseespy.egg-info'])

print('generating package ...')
subprocess.run(['python3.7', 'setup.py', 'bdist_wheel'])

print('wheel generated:')
subprocess.run(['ls', 'dist'])

print('uploading to pip ...')
subprocess.run(['python3.7', '-m', 'twine', 'upload', 'dist/*'])
