import os, pathlib
import pytest


PlotTestDirs = ['IndividualTests', 'SteelFrame2D_OBD_Animation',
                'Shell3D_OBD_Animation','FibreSection2D_OBD' ]

testStatus = [None]*len(PlotTestDirs)

baseDir = pathlib.Path.cwd()
plotDir = 

for ii,  TestDir in enumerate(TestDirs):
    os.chdir( baseDir / TestDir )
    testStatus[ii] = pytest.main()
    

print()
print(testStatus)
