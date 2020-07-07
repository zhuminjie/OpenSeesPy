import os, pathlib
import pytest


TestDirs = ['model_ODB','IndividualTests', 'SteelFrame2D_OBD_Animation',
            'Shell3D_OBD_Animation','FibreSection2D_OBD' ]

testStatus = [None]*len(TestDirs)

baseDir = pathlib.Path.cwd()

for ii,  TestDir in enumerate(TestDirs):
    os.chdir( baseDir / TestDir )
    testStatus[ii] = pytest.main()
    

print()
print(testStatus)