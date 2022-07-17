# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:39:41 2021

@author: harsh
"""
import numpy as np
import math as mm
import opensees as op
import time as tt
##################################################################
#                                                                #
# Effective stress site response analysis for a layered          #
# soil profile located on a 2% slope and underlain by an         #
# elastic half-space.  9-node quadUP elements are used.          #
# The finite rigidity of the elastic half space is               #
# considered through the use of a viscous damper at the          #
# base.                                                          #
#                                                                #
#    Converted to openseespy by: Harsh Mistry                    #
#                                The University of Manchester    #
#                                                                #
#   Created by:  Chris McGann                                    #
#                HyungSuk Shin                                   #
#                Pedro Arduino                                   #
#                Peter Mackenzie-Helnwein                        #
#              --University of Washington--                      #
#                                                                #
# ---> Basic units are kN and m   (unless specified)             #
#                                                                #
##################################################################
#-----------------------------------------------------------------------------------------
#  1. DEFINE SOIL AND MESH GEOMETRY
#-----------------------------------------------------------------------------------------

op.wipe()
nodes_dict = dict()

#---SOIL GEOMETRY
# thicknesses of soil profile (m)
soilThick = 30.0
# number of soil layers
numLayers = 3
# layer thicknesses
layerThick=[20.0,8.0,2.0]

# depth of water table
waterTable = 2.0

# define layer boundaries
layerBound=np.zeros((numLayers,1))
layerBound[0]=layerThick[0];
for i in range(1,numLayers):
    layerBound[i]=layerBound[i-1]+layerThick[i]
    
#---MESH GEOMETRY
# number of elements in horizontal direction
nElemX = 1
# number of nodes in horizontal direction
nNodeX =2 * nElemX+1
# horizontal element size (m)
sElemX = 2.0

# number of elements in vertical direction for each layer
nElemY = [40,16,4]

# total number of elements in vertical direction
nElemT = 60

sElemY = np.zeros((numLayers,1))
# vertical element size in each layer
for i in range(numLayers):
    sElemY[i] = [layerThick[i-1]/nElemY[i-1]]
    print('size:',sElemY[i])
    
# number of nodes in vertical direction
nNodeY = 2 * nElemT+1

# total number of nodes
nNodeT = nNodeX * nNodeY

#-----------------------------------------------------------------------------------------
#  2. CREATE PORE PRESSURE NODES AND FIXITIES
#-----------------------------------------------------------------------------------------
op.model('basic', '-ndm', 2, '-ndf', 3) 

count = 1
layerNodeCount = 0
dry_Node=np.zeros((500,1))
node_save=np.zeros((500,1))
# loop over soil layers
for k in range(1,numLayers+1):
    # loop in horizontal direction
    for i in range(1,nNodeX+1,2):
       if k==1:
           bump = 1
       else:
           bump = 0
       j_end=2 * nElemY[k-1] + bump    
       for j in range(1,j_end+1,2):
            xCoord  = (i-1) * (sElemX/2)
            yctr    = j + layerNodeCount
            yCoord  = (yctr-1) * (np.float(sElemY[k-1]))/2
            nodeNum = i + ((yctr-1) * nNodeX)
            op.node(nodeNum, xCoord, yCoord)

          # output nodal information to data file
            nodes_dict[nodeNum] = (nodeNum, xCoord, yCoord)
            node_save[nodeNum] = np.int(nodeNum)
          # designate nodes above water table
            waterHeight = soilThick - waterTable
            if yCoord >= waterHeight:
                dry_Node[count] = nodeNum
                count = count+1
    layerNodeCount = yctr + 1

dryNode=np.trim_zeros(dry_Node)
Node_d=np.unique(node_save)        
Node_d=np.trim_zeros(Node_d)
np.savetxt('Node_record.txt',Node_d)    
print('Finished creating all -ndf 3 nodes')
print('Number of Dry Nodes:',len(dryNode))    

# define fixities for pore pressure nodes above water table
for i in range(count-1):
    n_dryNode=np.int(dryNode[i])
    op.fix(n_dryNode, 0, 0, 1)
    
op.fix(1, 0, 1, 0)
op.fix(3, 0, 1, 0)    
print('Finished creating all -ndf 3 boundary conditions...')

# define equal degrees of freedom for pore pressure nodes
for i in range(1,((3*nNodeY)-2),6):
    op.equalDOF(i, i+2, 1, 2)
    
print("Finished creating equalDOF for pore pressure nodes...")

#-----------------------------------------------------------------------------------------
#  3. CREATE INTERIOR NODES AND FIXITIES
#-----------------------------------------------------------------------------------------
op.model('basic', '-ndm', 2, '-ndf', 2) 

xCoord = np.float(sElemX/2)

# loop over soil layers
layerNodeCount = 0

for k in range(1,numLayers+1):
    if k==1:
        bump = 1
    else:
        bump = 0
    j_end=2 * nElemY[k-1] + bump    
    for j in range(1,j_end+1,1):
        yctr = j + layerNodeCount
        yCoord  = (yctr-1) * (np.float(sElemY[k-1]))/2
        nodeNum = (3*yctr) - 1 
        op.node(nodeNum, xCoord, yCoord)
        # output nodal information to data file
        nodes_dict[nodeNum] = (nodeNum, xCoord, yCoord)
    
    layerNodeCount = yctr   

# interior nodes on the element edges
# loop over layers
layerNodeCount = 0

for k in range(1,numLayers+1):
    # loop in vertical direction
    for j in range(1,((nElemY[k-1])+1)):
        yctr     = j + layerNodeCount;
        yCoord   = np.float(sElemY[k-1])*(yctr-0.5)
        nodeNumL = (6*yctr) - 2
        nodeNumR = nodeNumL + 2
        
        op.node(nodeNumL ,0.0, yCoord)
        op.node(nodeNumR , sElemX, yCoord)
        
        # output nodal information to data file
        nodes_dict[nodeNumL] = (nodeNumL ,0.0, yCoord)
        nodes_dict[nodeNumR] = (nodeNumR , sElemX, yCoord)
    layerNodeCount = yctr

print("Finished creating all -ndf 2 nodes...")        

# define fixities for interior nodes at base of soil column
op.fix(2, 0, 1)
print('Finished creating all -ndf 2 boundary conditions...')

# define equal degrees of freedom which have not yet been defined
for i in range(1,((3*nNodeY)-6),6):
    op.equalDOF(i  , i+1, 1, 2)
    op.equalDOF(i+3, i+4, 1, 2)
    op.equalDOF(i+3, i+5, 1, 2)

op.equalDOF(nNodeT-2, nNodeT-1, 1, 2)
print('Finished creating equalDOF constraints...')

#-----------------------------------------------------------------------------------------
#  4. CREATE SOIL MATERIALS
#-----------------------------------------------------------------------------------------

# define grade of slope (%)
grade = 2.0
slope = mm.atan(grade/100.0)
g     = -9.81

xwgt_var = g * (mm.sin(slope))
ywgt_var = g * (mm.cos(slope))
thick = [1.0,1.0,1.0]
xWgt  = [xwgt_var, xwgt_var, xwgt_var] 
yWgt  = [ywgt_var, ywgt_var, ywgt_var] 
uBulk = [6.88E6,  5.06E6, 5.0E-6]
hPerm = [1.0E-4, 1.0E-4, 1.0E-4]
vPerm = [1.0E-4, 1.0E-4, 1.0E-4]


# nDMaterial PressureDependMultiYield02
# nDMaterial('PressureDependMultiYield02', matTag, nd, rho, refShearModul, refBulkModul,\
#    frictionAng, peakShearStra, refPress, pressDependCoe, PTAng,\
#        contrac[0], contrac[2], dilat[0], dilat[2], noYieldSurf=20.0,\
#            *yieldSurf=[], contrac[1]=5.0, dilat[1]=3.0, *liquefac=[1.0,0.0],e=0.6, \
#                *params=[0.9, 0.02, 0.7, 101.0], c=0.1)

op.nDMaterial('PressureDependMultiYield02',3, 2, 1.8, 9.0e4, 2.2e5, 32, 0.1, \
                                      101.0, 0.5, 26, 0.067, 0.23, 0.06, \
                                      0.27, 20, 5.0, 3.0, 1.0, \
                                      0.0, 0.77, 0.9, 0.02, 0.7, 101.0)

op.nDMaterial('PressureDependMultiYield02', 2, 2, 2.24, 9.0e4, 2.2e5, 32, 0.1, \
                                      101.0, 0.5, 26, 0.067, 0.23, 0.06, \
                                      0.27, 20, 5.0, 3.0, 1.0, \
                                      0.0, 0.77, 0.9, 0.02, 0.7, 101.0)
    
op.nDMaterial('PressureDependMultiYield02',1, 2, 2.45, 1.3e5, 2.6e5, 39, 0.1, \
                                      101.0, 0.5, 26, 0.010, 0.0, 0.35, \
                                      0.0, 20, 5.0, 3.0, 1.0, \
                                      0.0, 0.47, 0.9, 0.02, 0.7, 101.0)    

print("Finished creating all soil materials...")

#-----------------------------------------------------------------------------------------
#  5. CREATE SOIL ELEMENTS
#-----------------------------------------------------------------------------------------

for j in range(1,nElemT+1):
    nI = ( 6*j) - 5
    nJ = nI + 2
    nK = nI + 8
    nL = nI + 6
    nM = nI + 1
    nN = nI + 5
    nP = nI + 7
    nQ = nI + 3
    nR = nI + 4
    
    lowerBound = 0.0
    for i in range(1,numLayers+1):
        if j * sElemY[i-1] <= layerBound[i-1] and j * sElemY[i-1] > lowerBound:
            # permeabilities are initially set at 1.0 m/s for gravity analysis,
            op.element('9_4_QuadUP', j, nI, nJ, nK, nL, nM, nN, nP, nQ, nR, \
                           thick[i-1], i, uBulk[i-1], 1.0, 1.0, 1.0, xWgt[i-1], yWgt[i-1])
                
        lowerBound = layerBound[i-1]
            
print("Finished creating all soil elements...")
#-----------------------------------------------------------------------------------------
#  6. LYSMER DASHPOT
#-----------------------------------------------------------------------------------------

# define dashpot nodes
dashF =  nNodeT+1
dashS =  nNodeT+2

op.node(dashF,  0.0, 0.0)
op.node(dashS,  0.0, 0.0)

# define fixities for dashpot nodes
op.fix(dashF, 1, 1)
op.fix(dashS, 0, 1)

# define equal DOF for dashpot and base soil node
op.equalDOF(1, dashS,  1)
print('Finished creating dashpot nodes and boundary conditions...')

# define dashpot material
colArea      = sElemX * thick[0]
rockVS       = 700.0
rockDen      = 2.5
dashpotCoeff = rockVS * rockDen

#uniaxialMaterial('Viscous', matTag, C, alpha)
op.uniaxialMaterial('Viscous', numLayers+1, dashpotCoeff * colArea, 1)

# define dashpot element
op.element('zeroLength', nElemT+1, dashF, dashS, '-mat', numLayers+1, '-dir', 1)

print("Finished creating dashpot material and element...")

#-----------------------------------------------------------------------------------------
#  7. CREATE GRAVITY RECORDERS
#-----------------------------------------------------------------------------------------

# create list for pore pressure nodes
load_nodeList3=np.loadtxt('Node_record.txt')
nodeList3=[]

for i in range(len(load_nodeList3)):
    nodeList3.append(np.int(load_nodeList3[i]))
# record nodal displacment, acceleration, and porepressure
op.recorder('Node','-file','Gdisplacement.txt','-time','-node',*nodeList3,'-dof', 1, 2, 'disp')
op.recorder('Node','-file','Gacceleration.txt','-time','-node',*nodeList3,'-dof', 1, 2, 'accel')
op.recorder('Node','-file','GporePressure.txt','-time','-node',*nodeList3,'-dof', 3, 'vel')

# record elemental stress and strain (files are names to reflect GiD gp numbering)
op.recorder('Element','-file','Gstress1.txt','-time','-eleRange', 1,nElemT,'material','1','stress')
op.recorder('Element','-file','Gstress2.txt','-time','-eleRange', 1,nElemT,'material','2','stress')
op.recorder('Element','-file','Gstress3.txt','-time','-eleRange', 1,nElemT,'material','3','stress')
op.recorder('Element','-file','Gstress4.txt','-time','-eleRange', 1,nElemT,'material','4','stress')
op.recorder('Element','-file','Gstress9.txt','-time','-eleRange', 1,nElemT,'material','9','stress')
op.recorder('Element','-file','Gstrain1.txt','-time','-eleRange', 1,nElemT,'material','1','strain')
op.recorder('Element','-file','Gstrain2.txt','-time','-eleRange', 1,nElemT,'material','2','strain')
op.recorder('Element','-file','Gstrain3.txt','-time','-eleRange', 1,nElemT,'material','3','strain')
op.recorder('Element','-file','Gstrain4.txt','-time','-eleRange', 1,nElemT,'material','4','strain')
op.recorder('Element','-file','Gstrain9.txt','-time','-eleRange', 1,nElemT,'material','9','strain')

print("Finished creating gravity recorders...")

#-----------------------------------------------------------------------------------------
#  8. DEFINE ANALYSIS PARAMETERS
#-----------------------------------------------------------------------------------------

#---GROUND MOTION PARAMETERS
# time step in ground motion record
motionDT = 0.005
# number of steps in ground motion record
motionSteps = 7990

#---RAYLEIGH DAMPING PARAMETERS
# damping ratio
damp = 0.02
# lower frequency
omega1 = 2 * np.pi * 0.2
# upper frequency
omega2 = 2 * np.pi * 20
# damping coefficients
a0 = 2*damp*omega1*omega2/(omega1 + omega2)
a1 = 2*damp/(omega1 + omega2)
print("Damping Coefficients: a_0 = $a0;  a_1 = $a1")

#---DETERMINE STABLE ANALYSIS TIME STEP USING CFL CONDITION
# maximum shear wave velocity (m/s)
vsMax = 250.0
# duration of ground motion (s)
duration = motionDT*motionSteps
# minimum element size
minSize = sElemY[0]

for i in range(2,numLayers+1):
    if sElemY[i-1] <= minSize:
        minSize = sElemY[i-1]

# trial analysis time step
kTrial = minSize/(vsMax**0.5)
# define time step and number of steps for analysis
if motionDT <= kTrial:
    nSteps = motionSteps
    dT     = motionDT
else:
    nSteps = np.int(mm.floor(duration/kTrial)+1)
    dT     = duration/nSteps
    

print("Number of steps in analysis: $nSteps")
print("Analysis time step: $dT")

#---ANALYSIS PARAMETERS
# Newmark parameters
gamma = 0.5
beta  = 0.25

#-----------------------------------------------------------------------------------------
#  9. GRAVITY ANALYSIS
#-----------------------------------------------------------------------------------------
# update materials to ensure elastic behavior
op.updateMaterialStage('-material', 1, '-stage', 0)
op.updateMaterialStage('-material', 2, '-stage', 0)
op.updateMaterialStage('-material', 3, '-stage', 0)

op.constraints('Penalty', 1.0E14, 1.0E14)
op.test('NormDispIncr', 1e-4, 35, 1)
op.algorithm('KrylovNewton')
op.numberer('RCM')
op.system('ProfileSPD')
op.integrator('Newmark', gamma, beta)
op.analysis('Transient')

startT = tt.time()
op.analyze(10, 5.0E2)
print('Finished with elastic gravity analysis...')

# update material to consider elastoplastic behavior
op.updateMaterialStage('-material', 1, '-stage', 1)
op.updateMaterialStage('-material', 2, '-stage', 1)
op.updateMaterialStage('-material', 3, '-stage', 1)

# plastic gravity loading
op.analyze(40, 5.0e2)

print('Finished with plastic gravity analysis...')

#-----------------------------------------------------------------------------------------
#  10. UPDATE ELEMENT PERMEABILITY VALUES FOR POST-GRAVITY ANALYSIS
#-----------------------------------------------------------------------------------------

# choose base number for parameter IDs which is higer than other tags used in analysis
ctr = 10000.0
# loop over elements to define parameter IDs 
for i in range(1,nElemT+1):
    op.parameter(np.int(ctr+1.0), 'element', i, 'vPerm')
    op.parameter(np.int(ctr+2.0), 'element', i, 'hPerm')
    ctr   = ctr+2.0

# update permeability parameters for each element using parameter IDs
ctr = 10000.0
for j in range(1,nElemT+1):
    lowerBound = 0.0
    for i in range(1,numLayers+1):
        if j * sElemY[i-1] <= layerBound[i-1] and j*sElemY[i-1] > lowerBound:
            op.updateParameter(np.int(ctr+1.0), vPerm[i-1])
            op.updateParameter(np.int(ctr+2.0), hPerm[i-1])
        lowerBound = layerBound[i-1]
    ctr = ctr+2.0

print("Finished updating permeabilities for dynamic analysis...")

#-----------------------------------------------------------------------------------------
#  11. CREATE POST-GRAVITY RECORDERS
#-----------------------------------------------------------------------------------------

# reset time and analysis
op.setTime(0.0)
op.wipeAnalysis()
op.remove('recorders')

# recorder time step
recDT = 10*motionDT

# record nodal displacment, acceleration, and porepressure
op.recorder('Node','-file','displacement.txt','-time', '-dT',recDT,'-node',*nodeList3,'-dof', 1, 2, 'disp')
op.recorder('Node','-file','acceleration.txt','-time', '-dT',recDT,'-node',*nodeList3,'-dof', 1, 2, 'accel')
op.recorder('Node','-file','porePressure.txt','-time', '-dT',recDT,'-node',*nodeList3,'-dof', 3, 'vel')

# record elemental stress and strain (files are names to reflect GiD gp numbering)
op.recorder('Element','-file','stress1.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','1','stress')
op.recorder('Element','-file','stress2.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','2','stress')
op.recorder('Element','-file','stress3.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','3','stress')
op.recorder('Element','-file','stress4.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','4','stress')
op.recorder('Element','-file','stress9.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','9','stress')
op.recorder('Element','-file','strain1.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','1','strain')
op.recorder('Element','-file','strain2.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','2','strain')
op.recorder('Element','-file','strain3.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','3','strain')
op.recorder('Element','-file','strain4.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','4','strain')
op.recorder('Element','-file','strain9.txt','-time', '-dT',recDT,'-eleRange', 1,nElemT,'material','9','strain')

print("Finished creating all recorders...")

#-----------------------------------------------------------------------------------------
#  12. DYNAMIC ANALYSIS
#-----------------------------------------------------------------------------------------
op.model('basic', '-ndm', 2, '-ndf', 3)

# define constant scaling factor for applied velocity
cFactor = colArea * dashpotCoeff

# define velocity time history file
velocityFile='velocityHistory';
data_gm=np.loadtxt('velocityHistory.txt')
#motionSteps=len(data_gm)
#print('Number of point for GM:',motionSteps)

# timeseries object for force history
op.timeSeries('Path', 2, '-dt', motionDT, '-filePath', velocityFile+'.txt', '-factor', cFactor)
op.pattern('Plain', 10, 2)
op.load(1, 1.0, 0.0, 0.0)

print( "Dynamic loading created...")

op.constraints('Penalty', 1.0E16, 1.0E16)
op.test('NormDispIncr', 1e-3, 35, 1)
op.algorithm('KrylovNewton')
op.numberer('RCM')
op.system('ProfileSPD')
op.integrator('Newmark', gamma, beta)
op.rayleigh(a0, a1, 0.0, 0.0)
op.analysis('Transient')

# perform analysis with timestep reduction loop
ok = op.analyze(nSteps,dT)

# if analysis fails, reduce timestep and continue with analysis
if ok !=0:
    print("did not converge, reducing time step")
    curTime = op.getTime()
    mTime = curTime
    print("curTime: ", curTime)
    curStep = curTime/dT
    print("curStep: ", curStep)
    rStep   = (nSteps-curStep)*2.0
    remStep = np.int((nSteps-curStep)*2.0)
    print("remStep: ", remStep)
    dT = dT/2.0
    print("dT: ", dT)

    ok = op.analyze(remStep, dT)
    # if analysis fails again, reduce timestep and continue with analysis    
    if ok !=0:
        print("did not converge, reducing time step")
        curTime = op.getTime()
        print("curTime: ", curTime)
        curStep = (curTime-mTime)/dT
        print("curStep: ", curStep)
        remStep = np.int((rStep-curStep)*2.0)
        print("remStep: ", remStep)
        dT = dT/2.0
        print("dT: ", dT)
    
        ok = op.analyze(remStep, dT)    

endT = tt.time()
print("Finished with dynamic analysis...")
print("Analysis execution time: ",(endT-startT))
op.wipe()
