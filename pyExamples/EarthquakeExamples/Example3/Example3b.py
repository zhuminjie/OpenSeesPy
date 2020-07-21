# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:12:06 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
# Example 3. 2D Cantilever -- Static Pushover
#To run Uniaxial Inelastic Material, Fiber Section, Nonlinear Mode, Static Pushover Analysis: First import the InelasticFiberSection.py(upto gravity loading is already in this script)
#and run the current script
#the detailed problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual  (example: 3)
# --------------------------------------------------------------------------------------------------
#	OpenSees (Tcl) code by:	Silvia Mazzoni & Frank McKenna, 2006
# characteristics of pushover analysis
##########################################################################################################################################################################
import openseespy.opensees as op
#import the os module
#import os
import math
op.wipe()

from InelasticFiberSection import *
Dmax = 0.05*LCol
Dincr = 0.001*LCol
Hload = Weight
maxNumIter = 6
tol = 1e-8

op.timeSeries('Linear', 2)
op.pattern('Plain', 200, 2)
op.load(2, Hload, 0.0,0.0)

op.wipeAnalysis()
op.constraints('Plain')
op.numberer('Plain')
op.system('BandGeneral')
op.test('EnergyIncr', Tol, maxNumIter)
op.algorithm('Newton')

op.integrator('DisplacementControl', IDctrlNode, IDctrlDOF, Dincr)
op.analysis('Static')


Nsteps =  int(Dmax/ Dincr)

ok = op.analyze(Nsteps)
print(ok)

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
            ok = op.analyze(Nsteps)                            
            print(test[i], algorithm[j], ok)             
            if ok == 0:
                break
        else:
            continue

u2 = op.nodeDisp(2, 1)
print("u2 = ", u2)

op.wipe()