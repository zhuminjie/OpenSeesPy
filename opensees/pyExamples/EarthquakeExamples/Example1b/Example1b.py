# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:29:26 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
# Example 1b. portal frame in 2D
#This is a simple model of an elastic portal frame with EQ ground motion and gravity loading. Here the structure is excited using uniform excitation load pattern
# all units are in kip, inch, second
#To run EQ ground-motion analysis (BM68elc.acc needs to be downloaded into the same directory).
#the detailed problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual  (example: 1b)
# --------------------------------------------------------------------------------------------------
# elasticBeamColumn ELEMENT
#	OpenSees (Tcl) code by:	Silvia Mazzoni & Frank McKenna, 2006

#
#    ^Y
#    |
#    3_________(3)________4       __ 
#    |                                    |          | 
#    |                                    |          |
#    |                                    |          |
#  (1)                                 (2)       LCol
#    |                                    |          |
#    |                                    |          |
#    |                                    |          |
#  =1=                               =2=      _|_  -------->X
#    |----------LBeam------------|
#

# SET UP -----------------------------------------------------------------------------

import openseespy.opensees as op
#import the os module
import os
op.wipe()

#########################################################################################################################################################################

#########################################################################################################################################################################
op.model('basic', '-ndm', 2, '-ndf', 3) 

#to create a directory at specified path with name "Data"
os.chdir('C:\\Opensees Python\\OpenseesPy examples')

#this will create the directory with name 'Data' and will update it when we rerun the analysis, otherwise we have to keep deleting the old 'Data' Folder
dir = "C:\\Opensees Python\\OpenseesPy examples\\Data-1b"
if not os.path.exists(dir):
    os.makedirs(dir)

#this will create just 'Data' folder    
#os.mkdir("Data-1b")
    
#detect the current working directory
#path1 = os.getcwd()
#print(path1)

h = 432.0
w  =  504.0

op.node(1, 0.0, 0.0)
op.node(2, h, 0.0)
op.node(3, 0.0, w)
op.node(4, h, w)

op.fix(1, 1,1,1)
op.fix(2, 1,1,1)
op.fix(3, 0,0,0)
op.fix(4, 0,0,0)

op.mass(3, 5.18, 0.0, 0.0)
op.mass(4, 5.18, 0.0, 0.0)  

op.geomTransf('Linear', 1)
A = 3600000000.0
E = 4227.0
Iz = 1080000.0

A1 = 5760000000.0
Iz1 = 4423680.0
op.element('elasticBeamColumn', 1, 1, 3, A, E, Iz, 1)
op.element('elasticBeamColumn', 2, 2, 4, A, E, Iz, 1)
op.element('elasticBeamColumn', 3, 3, 4, A1, E, Iz1, 1)

op.recorder('Node', '-file', 'Data-1b/DFree.out','-time', '-node', 3,4, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-1b/DBase.out','-time', '-node', 1,2, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-1b/RBase.out','-time', '-node', 1,2, '-dof', 1,2,3, 'reaction')
#op.recorder('Drift', '-file', 'Data-1b/Drift.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Element', '-file', 'Data-1b/FCol.out','-time', '-ele', 1,2, 'globalForce')
op.recorder('Element', '-file', 'Data-1b/DCol.out','-time', '-ele', 3, 'deformations')

#defining gravity loads
op.timeSeries('Linear', 1)
op.pattern('Plain', 1, 1)
op.eleLoad('-ele', 3, '-type', '-beamUniform', -7.94)

op.constraints('Plain')
op.numberer('Plain')
op.system('BandGeneral')
op.test('NormDispIncr', 1e-8, 6)
op.algorithm('Newton')
op.integrator('LoadControl', 0.1)
op.analysis('Static')
op.analyze(10)
    
op.loadConst('-time', 0.0)

#applying Dynamic Ground motion analysis
op.timeSeries('Path', 2, '-dt', 0.01, '-filePath', 'BM68elc.acc', '-factor', 1.0)
op.pattern('UniformExcitation', 2, 1, '-accel', 2) #how to give accelseriesTag?

eigen = op. eigen('-fullGenLapack', 1)
import math
power = math.pow(eigen, 0.5)
betaKcomm = 2 * (0.02/power)

op.rayleigh(0.0, 0.0, 0.0, betaKcomm)

op.wipeAnalysis()
op.constraints('Plain')
op.numberer('Plain')
op.system('BandGeneral')
op.test('NormDispIncr', 1e-8, 10)
op.algorithm('Newton')
op.integrator('Newmark', 0.5, 0.25)
op.analysis('Transient')
op.analyze(1000, 0.02)

u3 = op.nodeDisp(3, 1)
print("u2 = ", u3)

op.wipe()