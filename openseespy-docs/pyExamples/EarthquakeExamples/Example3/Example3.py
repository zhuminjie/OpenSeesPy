# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:12:06 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
# Example 3. 2D Cantilever -- EQ ground motion
#To run Uniaxial Inelastic Material, Fiber Section, Nonlinear Mode, Uniform Earthquake Excitation:First import the InelasticFiberSection.py(upto gravity loading is already in this script)
#and run the current script
#To run EQ ground-motion analysis (BM68elc.acc needs to be downloaded into the same directory)
# Same acceleration input at all nodes restrained in specified direction (uniform acceleration input at all support nodes)
#the detailed problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual  (example: 3)
# --------------------------------------------------------------------------------------------------
#	OpenSees (Tcl) code by:	Silvia Mazzoni & Frank McKenna, 2006
##########################################################################################################################################################################
import openseespy.opensees as op
#import the os module
#import os
import math
op.wipe()
#########################################################################################################################################################################
import InelasticFiberSection
#applying Dynamic Ground motion analysis
Tol = 1e-8
GMdirection = 1
GMfile = 'BM68elc.acc'
GMfact = 1.0
Lambda = op.eigen('-fullGenLapack', 1) # eigenvalue mode 1
Omega = math.pow(Lambda, 0.5)
betaKcomm = 2 * (0.02/Omega)

xDamp = 0.02				# 2% damping ratio
alphaM = 0.0				# M-prop. damping; D = alphaM*M	
betaKcurr = 0.0		# K-proportional damping;      +beatKcurr*KCurrent
betaKinit = 0.0 # initial-stiffness proportional damping      +beatKinit*Kini

op.rayleigh(alphaM,betaKcurr, betaKinit, betaKcomm) # RAYLEIGH damping

# Uniform EXCITATION: acceleration input
IDloadTag = 400			# load tag
dt = 0.01			# time step for input ground motion
GMfatt = 1.0			# data in input file is in g Unifts -- ACCELERATION TH
maxNumIter = 10
op.timeSeries('Path', 2, '-dt', dt, '-filePath', GMfile, '-factor', GMfact)
op.pattern('UniformExcitation', IDloadTag, GMdirection, '-accel', 2) 

op.wipeAnalysis()
op.constraints('Transformation')
op.numberer('Plain')
op.system('BandGeneral')
op.test('EnergyIncr', Tol, maxNumIter)
op.algorithm('ModifiedNewton')

NewmarkGamma = 0.5
NewmarkBeta = 0.25
op.integrator('Newmark', NewmarkGamma, NewmarkBeta)
op.analysis('Transient')

DtAnalysis = 0.01 # time-step Dt for lateral analysis
TmaxAnalysis = 10.0 # maximum duration of ground-motion analysis

Nsteps =  int(TmaxAnalysis/ DtAnalysis)

ok = op.analyze(Nsteps, DtAnalysis)

tCurrent = op.getTime()

# for gravity analysis, load control is fine, 0.1 is the load factor increment (http://opensees.berkeley.edu/wiki/index.php/Load_Control)

test = {1:'NormDispIncr', 2: 'RelativeEnergyIncr', 4: 'RelativeNormUnbalance',5: 'RelativeNormDispIncr', 6: 'NormUnbalance'}
algorithm = {1:'KrylovNewton', 2: 'SecantNewton' , 4: 'RaphsonNewton',5: 'PeriodicNewton', 6: 'BFGS', 7: 'Broyden', 8: 'NewtonLineSearch'}

for i in test:
    for j in algorithm:

        if ok != 0:
            if j < 4:
                op.algorithm(algorithm[j], '-initial')
                
            else:
                op.algorithm(algorithm[j])
                
            op.test(test[i], Tol, 1000)
            ok = op.analyze(Nsteps, DtAnalysis)                            
            print(test[i], algorithm[j], ok)             
            if ok == 0:
                break
        else:
            continue

u2 = op.nodeDisp(2, 1)
print("u2 = ", u2)

op.wipe()