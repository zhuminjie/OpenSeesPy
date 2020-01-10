import subprocess
import shutil
import os
import os.path

linux = './openseespy/opensees/linux/'
so = '../openseespy/SRC/interpreter/opensees.so'

if os.path.exists(linux+'opensees.so'):
    os.remove(linux+'opensees.so')
if os.path.exists(linux+'lib'):
    shutil.rmtree(linux+'lib')

shutil.copy(so, linux)
os.mkdir(linux+'lib')

p = subprocess.run(
    ["ldd", so], capture_output=True)

for line in p.stdout.decode('utf-8').split('\n'):
    i = line.find('/')
    j = line.find(' ', i)
    if i < 0 or j < 0 or i >= j:
        continue

    print('copying '+line[i:j]+' ....')
    shutil.copy(line[i:j], linux+'lib/')