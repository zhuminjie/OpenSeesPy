# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:00:41 2022

@author: Zhongze Xu, The University of Texas at Austin

Openseespy code to run plane-strain stress-controlled undrained cyclic simple shear element
to calibrate pm4sand model
Basic Units are m, kN and s unless otherwise specified	

original opensees code is from:

2D Undrained Cyclic Direct Simple Shear Test Using One Element        
University of Washington, Department of Civil and Environmental Eng   
Geotechnical Eng Group, L. Chen, P. Arduino - Feb 2018                
Basic Units are m, kN and s unless otherwise specified				

"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

from datetime import datetime
import openseespy.opensees as op
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

#==============================================================================
#Input Variables
'''
nDMaterial('PM4Sand', matTag, Dr, G0, hpo, rho, P_atm, h0, e_max, e_min, 
           nb, nd, Ado, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf, 
           Q, R, m_par, F_sed, p_sed)
'''
atm = -101.325
sig_v0 = 2.0* atm #initial vertical stress
CSR = 0.2 #cyclic stress ratio
Cycle_max = 5 #maximxum number of cycles
strain_in = 5.0e-6 #strain increment
K0 = 0.5
nu = K0/(1+K0) #poisson's ratio
devDisp = 0.03 #cutoff shear strain
perm = 1e-9 #permeability
#==============================================================================

#primary parameters
Dr = 0.6
G0 = 476.0
hpo = 0.53 #Contraction rate parameter
rho = 1.42 #mass density, KN/m3

#secondary parameters
P_atm = 101.325
# all initial stress dependant parameters have negative default values 
# and will be calculated during initialization
h0 = -1.0  #Variable that adjusts the ratio of plastic modulus to elastic modulus
e_max = 0.8
e_min = 0.5
e_ini = e_max - (e_max - e_min)*Dr #initial void ratio
nb = 0.5 #Bounding surface parameter, nb>=0
nd = 0.1 #Dilatancy surface parameter, nd>=0
Ado = -1.0
#Dilatancy parameter, will be computed at the time of initialization if input value is negative
z_max = -1.0 #Fabric-dilatancy tensor parameter
c_z = 250.0 #Fabric-dilatancy tensor parameter
c_e = -1.0 #Fabric-dilatancy tensor parameter
phi_cv = 26.0 #Critical state effective friction angle
g_degr = 2.0 #Variable that adjusts degradation of elastic modulus with accumulation of fabric
c_dr = -1.0 #Variable that controls the rotated dilatancy surface
c_kaf = -1.0 # Variable that controls the effect that sustained static shear stresses have on plastic modulus
Q = 10.0 #Critical state line parameter
R = 1.5 #Critical state line parameter
m_par = 0.01#Yield surface constant
F_sed = -1.0#Variable that controls the minimum value the reduction factor of the elastic moduli can get during reconsolidation
p_sed = -1.0#Mean effective stress up to which reconsolidation strains are enhanced

#%%
#Rayleigh Damping Parameters
'''
rayleigh(alphaM, betaK, betaKinit, betaKcomm)
'''
damp = 0.02
omega1 = 0.2
omega2 = 20.0
a1 = 2.0*damp/(omega1+omega2) #a1 is alphaM
a0 = a1*omega1*omega2 #a0 is betaK
#%%
#create model
#Remove the existing model, important!!! 
op.wipe()

# set modelbuilder
op.model('basic', '-ndm', 2, '-ndf', 3)

#model nodes
x1 = 0.0
y1 = 0.0

x2 = 1.0
y2 = 0.0

x3 = 1.0
y3 = 1.0

x4 = 0.0
y4 = 1.0

#create nodes

op.node(1, x1, y1)
op.node(2, x2, y2)
op.node(3, x3, y3)
op.node(4, x4, y4)

#boundary conditions
op.fix(1, 1, 1, 1)
op.fix(2, 1, 1, 1)
op.fix(3, 0, 0, 1)
op.fix(4, 0, 0, 1)
op.equalDOF(3,4,1,2) #make node 3 and 4 equal displacement at degrees 1 & 2

#material
#==================================================================
#nDMaterial('PM4Sand', matTag, D_r, G_o, h_po, Den, P_atm, h_o, e_max, 
#e_min, n_b, n_d, A_do, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf, 
#Q_bolt, R_bolt, m_par, F_sed, p_sed)
#==================================================================
op.nDMaterial('PM4Sand', 1, Dr, G0, hpo, rho, P_atm, h0, e_max, e_min, 
           nb, nd, Ado, z_max, c_z, c_e, phi_cv, nu, g_degr, c_dr, c_kaf, 
           Q, R, m_par, F_sed, p_sed)

#element
op.element('SSPquadUP',1, 1,2,3,4, 1, 1.0, 2.2e6, 1.0, perm, perm, e_ini, 1.0e-5)

#create recorders
op.recorder('Node','-file', 'Cycdisp.txt','-time', '-node',1,2,3,4,'-dof', 1, 2, 'disp')
op.recorder('Node','-file', 'CycPP.txt','-time', '-node',1,2,3,4,'-dof', 3, 'vel')
op.recorder('Element','-file', 'Cycstress.txt','-time','-ele', 1, 'stress')
op.recorder('Element','-file', 'Cycstrain.txt','-time','-ele', 1, 'strain')
#%%
#Analysis officially starts here
op.constraints('Transformation')
op.test('NormDispIncr', 1.0e-5, 35, 1)
op.algorithm('Newton')
op.numberer('RCM')
op.system('FullGeneral')
op.integrator('Newmark', 5.0/6.0, 4.0/9.0)
op.rayleigh(a1, a0, 0.0, 0.0) #modification
op.analysis('Transient')

#%%apply consolidation pressure
pNode = sig_v0/2.0 #put confining pressure evenly on two nodes

# create a plain load pattern with time series 1
op.timeSeries('Path', 1, '-values', 0, 1, 1, '-time', 0.0, 100.0, 1.0e10)
op.pattern("Plain", 1, 1, '-factor',1.0)
op.load(3, 0.0, pNode, 0.0) #apply vertical pressure at y direction
op.load(4, 0.0, pNode, 0.0)
op.updateMaterialStage('-material', 1, '-stage', 0)
op.analyze(100,1.0)
vDisp = op.nodeDisp(3,2)
b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
print('shear stress is',b[2])
op.timeSeries('Path', 2, '-values', 1.0, 1.0, 1.0, '-time', 100.0, 80000.0, 1.0e10, '-factor', 1.0)
op.pattern('Plain', 2, 2,'-factor',1.0)
op.sp(3, 2, vDisp)
op.sp(4, 2, vDisp)

#Close Drainage
for i in range(4):
    op.remove('sp', i+1, 3)
    print('Node ID', i+1)


op.analyze(25,1.0)
b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
print('shear stress is',b[2])
print('Drainage is closed')

op.updateMaterialStage('-material', 1, '-stage', 1)
'''
Note:
The program will use the default value of a secondary parameter if 
a negative input is assigned to that parameter, e.g. Ado = -1. 
However, FirstCall is mandatory when switching from elastic to elastoplastic 
if negative inputs are assigned to stress-dependent secondary parameters, 
e.g. Ado and zmax. 
'''

#setParameter('-value', 0, '-ele', elementTag, 'FirstCall', matTag)
op.setParameter('-val', 0, '-ele', 1, 'FirstCall', '1')

op.analyze(25,1.0)
b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
print('shear stress is',b[2])
print('finished update fixties')
# update Poisson's ratio for analysis
#setParameter -value 0.3 -ele 1 poissonRatio 1
op.setParameter('-val', 0.3, '-ele', 1, 'poissonRatio', 1)


controlDisp = 1.1 * devDisp
numCycle = 0.25
print('Current Number of Cycle:', numCycle)

start = datetime.now()
while (numCycle <= Cycle_max):
    #impose 1/4 cycle: zero stress to positve max stress  
    hDisp = op.nodeDisp(3,1)
    cur_time = op.getTime()
    steps = controlDisp/strain_in
    time_change = cur_time + steps
    op.timeSeries('Path', 3,'-values', hDisp, controlDisp, controlDisp, '-time', cur_time, time_change, 1.0e10, '-factor', 1.0)
    op.pattern('Plain', 3, 3, '-fact', 1.0)
    op.sp(3, 1, 1.0)
    b = op.eleResponse(1, 'stress') #b = [sigmaxx, sigmayy, sigmaxy]
    print('shear stress is',b[2])
    while b[2] <= CSR*sig_v0*(-1.0): #b[2] is the shear stress, sigmaxy
        op.analyze(1, 1.0)
        b = op.eleResponse(1, 'stress')
        hDisp = op.nodeDisp(3,1)
        if hDisp >= devDisp:
            print('loading break')
            break
    numCycle = numCycle + 0.25
    hDisp = op.nodeDisp(3,1)
    cur_time = op.getTime()
    op.remove('loadPattern', 3)
    op.remove('timeSeries', 3)
    op.remove('sp', 3, 1)
    #impose 1/2 cycle: Postive max stress to negative max stress
    steps = (controlDisp+hDisp)/strain_in
    time_change = cur_time + steps
    op.timeSeries('Path', 3,'-values', hDisp, -1.0*controlDisp, -1.0*controlDisp, '-time', cur_time, time_change, 1.0e10, '-factor', 1.0)
    op.pattern('Plain', 3, 3)
    op.sp(3, 1, 1.0)
    while b[2] > CSR*sig_v0:
        op.analyze(1, 1.0)
        b = op.eleResponse(1, 'stress')
        print('shear stress is',b[2])
        hDisp = op.nodeDisp(3,1)
        if hDisp <= -1.0*devDisp:
            print('unloading break')
            break
    numCycle = numCycle + 0.5
    hDisp = op.nodeDisp(3,1)
    cur_time = op.getTime()
    op.remove('loadPattern', 3)
    op.remove('timeSeries', 3)
    op.remove('sp', 3, 1)
    #impose 1/4 cycle
    steps = (controlDisp+hDisp)/strain_in
    op.timeSeries('Path', 3,'-values', hDisp, controlDisp, controlDisp, '-time', cur_time, time_change, 1.0e10, '-factor', 1.0)
    op.pattern('Plain', 3, 3, '-fact', 1.0)
    op.sp(3, 1, 1.0)
    while b[2] <= 0.0: #b[2] is the shear stress, sigmaxy
        op.analyze(1, 1.0)
        b = op.eleResponse(1, 'stress')
        print('shear stress is',b[2])
        hDisp = op.nodeDisp(3,1)
        if hDisp >= devDisp:
            print('reloading break')
            break
    numCycle = numCycle + 0.25
    print('Current Number of Cycle:', numCycle)
    op.remove('loadPattern', 3)
    op.remove('timeSeries', 3)
    #op.remove('sp', 3, 1)

op.wipe()
print('Analysis is done!')
end = datetime.now()
run_time = end-start
print('Computation time is' , run_time)
#%%PostProcessing
import pandas as pd
df_stress = pd.read_csv('Cycstress.txt', sep=" ", header=None)
df_strain = pd.read_csv('Cycstrain.txt', sep=" ", header=None)
#df_PP = pd.read_csv('CycPP.txt', sep=" ", header=None)

Stress_V = df_stress.iloc[:, 1].to_numpy()*(-1.0) #compression is positive 
Shear_Stress = df_stress.iloc[:, 3].to_numpy()
Shear_Strain = df_strain.iloc[:, 3].to_numpy()*100.0

fig = plt.figure(figsize=(10,18))
ax0 = fig.add_subplot(211)
ax0.plot(Shear_Strain, Shear_Stress, label='stress-strain', linewidth=0.8)
ax0.set_xlabel("Shear Strain,%", fontsize=16)
ax0.set_ylabel("Shear Stress, kPa", fontsize=16)
ax0.legend(fontsize=16)

ax1 = fig.add_subplot(212)
ax1.plot(Stress_V, Shear_Stress, label='Stress Path', linewidth=0.8)
ax1.set_xlabel("Vertical Stress, kPa", fontsize=16)
ax1.set_ylabel("Shear Stress, kPa", fontsize=16)
ax1.legend(fontsize=16)
plt.show()
plt.close()
