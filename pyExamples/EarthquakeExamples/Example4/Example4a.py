# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:12:06 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
# Example4. 2D Portal Frame--  Dynamic EQ input analysis

#To run Uniaxial Inelastic Material, Fiber Section, Nonlinear Mode, Uniform Earthquake Excitation:First import the InelasticFiberSectionPortal2Dframe.py
#(upto gravity loading is already in this script) and run the current script
#To run EQ ground-motion analysis (ReadRecord.py, H-E12140.AT2 needs to be downloaded into the same directory)
#Same acceleration input at all nodes restrained in specified direction (uniform acceleration input at all support nodes)
#the problem description can be found here: 
#http://opensees.berkeley.edu/wiki/index.php/Examples_Manual and http://opensees.berkeley.edu/wiki/index.php/OpenSees_Example_4._Portal_Frame(example: 4)
# --------------------------------------------------------------------------------------------------
#	OpenSees (Tcl) code by:	Silvia Mazzoni & Frank McKenna, 2006
##########################################################################################################################################################################
import openseespy.opensees as op
#import the os module
#import os
import math
op.wipe()
##########################################################################################################################################################################

from InelasticFiberSectionPortal2Dframe import *
#applying Dynamic Ground motion analysis
Tol = 1e-8
maxNumIter = 10
GMdirection = 1
GMfact = 1.5
GMfatt = g*GMfact
DtAnalysis = 0.01*sec # time-step Dt for lateral analysis
TmaxAnalysis = 10.0*sec # maximum duration of ground-motion analysis


Lambda = op.eigen('-fullGenLapack', 1) # eigenvalue mode 1
Omega = math.pow(Lambda, 0.5)
betaKcomm = 2 * (0.02/Omega)

xDamp = 0.02				# 2% damping ratio
alphaM = 0.0				# M-prop. damping; D = alphaM*M	
betaKcurr = 0.0		# K-proportional damping;      +beatKcurr*KCurrent
betaKinit = 0.0 # initial-stiffness proportional damping      +beatKinit*Kini

op.rayleigh(alphaM,betaKcurr, betaKinit, betaKcomm) # RAYLEIGH damping

# Set some parameters
record = 'H-E12140'

import ReadRecord
# Permform the conversion from SMD record to OpenSees record
dt, nPts = ReadRecord.ReadRecord(record+'.at2', record+'.dat')
#print(dt, nPts)

# Uniform EXCITATION: acceleration input
IDloadTag = 400			# load tag
op.timeSeries('Path', 2, '-dt', dt, '-filePath', record+'.dat', '-factor', GMfatt)
op.pattern('UniformExcitation', IDloadTag, GMdirection, '-accel', 2) 

op.wipeAnalysis()
op.constraints('Transformation')
op.numberer('RCM')
op.system('BandGeneral')
#op.test('EnergyIncr', Tol, maxNumIter)
#op.algorithm('ModifiedNewton')
#NewmarkGamma = 0.5
#NewmarkBeta = 0.25
#op.integrator('Newmark', NewmarkGamma, NewmarkBeta)
#op.analysis('Transient')


#Nsteps =  int(TmaxAnalysis/ DtAnalysis)
#
#ok = op.analyze(Nsteps, DtAnalysis)

tCurrent = op.getTime()

# for gravity analysis, load control is fine, 0.1 is the load factor increment (http://opensees.berkeley.edu/wiki/index.php/Load_Control)

test = {1:'NormDispIncr', 2: 'RelativeEnergyIncr', 3:'EnergyIncr', 4: 'RelativeNormUnbalance',5: 'RelativeNormDispIncr', 6: 'NormUnbalance'}
algorithm = {1:'KrylovNewton', 2: 'SecantNewton' , 3:'ModifiedNewton' , 4: 'RaphsonNewton',5: 'PeriodicNewton', 6: 'BFGS', 7: 'Broyden', 8: 'NewtonLineSearch'}

tFinal = nPts*dt

#tFinal = 10.0*sec
time = [tCurrent]
u3 = [0.0]
u4 = [0.0]
ok = 0
while tCurrent < tFinal:
#    ok = op.analyze(1, .01)     
    for i in test:
        for j in algorithm: 
            if j < 4:
                op.algorithm(algorithm[j], '-initial')
                
            else:
                op.algorithm(algorithm[j])
            while ok == 0 and tCurrent < tFinal:
                    
                op.test(test[i], Tol, maxNumIter)        
                NewmarkGamma = 0.5
                NewmarkBeta = 0.25
                op.integrator('Newmark', NewmarkGamma, NewmarkBeta)
                op.analysis('Transient')
                ok = op.analyze(1, .01)
                
                if ok == 0 :
                    tCurrent = op.getTime()                
                    time.append(tCurrent)
                    u3.append(op.nodeDisp(3,1))
                    u4.append(op.nodeDisp(4,1))
                    print(test[i], algorithm[j], 'tCurrent=', tCurrent)

        
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.plot(time, u3)
plt.ylabel('Horizontal Displacement of node 3 (in)')
plt.xlabel('Time (s)')
plt.savefig('Horizontal Disp at Node 3 vs time.jpeg', dpi = 500)
plt.show()

plt.figure(figsize=(8,8))
plt.plot(time, u4)
plt.ylabel('Horizontal Displacement of node 4 (in)')
plt.xlabel('Time (s)')
plt.savefig('Horizontal Disp at Node 4 vs time.jpeg', dpi = 500)
plt.show() 


op.wipe()