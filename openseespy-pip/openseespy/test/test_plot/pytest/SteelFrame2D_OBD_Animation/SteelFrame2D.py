
##################################################################
## 2D steel frame example.
## 3 story steel building with rigid beam-column connections.  
## This script uses W-section command inOpensees to create steel.. 
## .. beam-column fiber sections. 
##
## By - Anurag Upadhyay, PhD Student, University of Utah.
## Date - 08/06/2018
##################################################################


import openseespy.opensees as ops
import openseespy.postprocessing.Get_Rendering as opp

import numpy as np
import matplotlib.pyplot as plt
import os
from math import asin, sqrt


def RunAnalysis():
    AnalysisType='Pushover'	;		#  Pushover  Gravity
    
    ## ------------------------------
    ## Start of model generation
    ## -----------------------------
    # remove existing model
    ops.wipe()
    
    # set modelbuilder
    ops.model('basic', '-ndm', 2, '-ndf', 3)
    
    import math
    
    ############################################
    ### Units and Constants  ###################
    ############################################
    
    inch = 1;
    kip = 1;
    sec = 1;
    
    # Dependent units
    sq_in = inch*inch;
    ksi = kip/sq_in;
    ft = 12*inch;
    
    # Constants
    g = 386.2*inch/(sec*sec);
    pi = math.acos(-1);
    
    #######################################
    ##### Dimensions 
    #######################################
    
    # Dimensions Input
    H_story=10.0*ft;
    W_bayX=16.0*ft;
    W_bayY_ab=5.0*ft+10.0*inch;
    W_bayY_bc=8.0*ft+4.0*inch;
    W_bayY_cd=5.0*ft+10.0*inch;
    
    # Calculated dimensions
    W_structure=W_bayY_ab+W_bayY_bc+W_bayY_cd;
    
    ################
    ### Material
    ################
    
    # Steel02 Material 
    
    matTag=1;
    matConnAx=2;
    matConnRot=3;
    
    Fy=60.0*ksi;		# Yield stress 
    Es=29000.0*ksi;		# Modulus of Elasticity of Steel 
    v=0.2;				# Poisson's ratio
    Gs=Es/(1+v);		# Shear modulus
    b=0.10;				# Strain hardening ratio
    params=[18.0,0.925,0.15]		# R0,cR1,cR2
    R0=18.0
    cR1=0.925
    cR2=0.15
    a1=0.05
    a2=1.00
    a3=0.05
    a4=1.0
    sigInit=0.0
    alpha=0.05
    
    ops.uniaxialMaterial('Steel02', matTag, Fy, Es, b, R0, cR1, cR2, a1, a2, a3, a4, sigInit)
    
    # ##################
    # ## Sections
    # ##################
    
    colSecTag1=1;
    colSecTag2=2;
    beamSecTag1=3;
    beamSecTag2=4;
    beamSecTag3=5;
    
    # COMMAND: section('WFSection2d', secTag, matTag, d, tw, bf, tf, Nfw, Nff)
    
    ops.section('WFSection2d', colSecTag1, matTag, 10.5*inch, 0.26*inch, 5.77*inch, 0.44*inch, 15, 16)		# outer Column
    ops.section('WFSection2d', colSecTag2, matTag, 10.5*inch, 0.26*inch, 5.77*inch, 0.44*inch, 15, 16)		# Inner Column
    
    ops.section('WFSection2d', beamSecTag1, matTag, 8.3*inch, 0.44*inch, 8.11*inch, 0.685*inch, 15, 15)		# outer Beam
    ops.section('WFSection2d', beamSecTag2, matTag, 8.2*inch, 0.40*inch, 8.01*inch, 0.650*inch, 15, 15)		# Inner Beam
    ops.section('WFSection2d', beamSecTag3, matTag, 8.0*inch, 0.40*inch, 7.89*inch, 0.600*inch, 15, 15)		# Inner Beam
    
    # Beam size - W10x26
    Abeam=7.61*inch*inch;
    IbeamY=144.*(inch**4);			# Inertia along horizontal axis
    IbeamZ=14.1*(inch**4);			# inertia along vertical axis
    
    # BRB input data
    Acore=2.25*inch;
    Aend=10.0*inch;
    LR_BRB=0.55;
    
    # ###########################
    # ##### Nodes
    # ###########################
    
    # Create All main nodes
    ops.node(1, 0.0, 0.0)
    ops.node(2, W_bayX, 0.0)
    ops.node(3, 2*W_bayX, 0.0)
    
    ops.node(11, 0.0, H_story)
    ops.node(12, W_bayX, H_story)
    ops.node(13, 2*W_bayX, H_story)
    
    ops.node(21, 0.0, 2*H_story)
    ops.node(22, W_bayX, 2*H_story)
    ops.node(23, 2*W_bayX, 2*H_story)
    
    ops.node(31, 0.0, 3*H_story)
    ops.node(32, W_bayX, 3*H_story)
    ops.node(33, 2*W_bayX, 3*H_story)
    
    # Beam Connection nodes
    
    ops.node(1101, 0.0, H_story)
    ops.node(1201, W_bayX, H_story)
    ops.node(1202, W_bayX, H_story)
    ops.node(1301, 2*W_bayX, H_story)
    
    ops.node(2101, 0.0, 2*H_story)
    ops.node(2201, W_bayX, 2*H_story)
    ops.node(2202, W_bayX, 2*H_story)
    ops.node(2301, 2*W_bayX, 2*H_story)
    
    ops.node(3101, 0.0, 3*H_story)
    ops.node(3201, W_bayX, 3*H_story)
    ops.node(3202, W_bayX, 3*H_story)
    ops.node(3301, 2*W_bayX, 3*H_story)
    
    # ###############
    #  Constraints
    # ###############
    
    ops.fix(1, 1, 1, 1)
    ops.fix(2, 1, 1, 1)
    ops.fix(3, 1, 1, 1)
    
    # #######################
    # ### Elements 
    # #######################
    
    # ### Assign beam-integration tags
    
    ColIntTag1=1;
    ColIntTag2=2;
    BeamIntTag1=3;
    BeamIntTag2=4;
    BeamIntTag3=5;
    
    ops.beamIntegration('Lobatto', ColIntTag1, colSecTag1, 4)
    ops.beamIntegration('Lobatto', ColIntTag2, colSecTag2, 4)
    ops.beamIntegration('Lobatto', BeamIntTag1, beamSecTag1, 4)
    ops.beamIntegration('Lobatto', BeamIntTag2, beamSecTag2, 4)
    ops.beamIntegration('Lobatto', BeamIntTag3, beamSecTag3, 4)
    
    # Assign geometric transformation
    
    ColTransfTag=1
    BeamTranfTag=2
    
    ops.geomTransf('PDelta', ColTransfTag)
    ops.geomTransf('Linear', BeamTranfTag)
    
    
    # Assign Elements  ##############
    
    # ## Add non-linear column elements
    ops.element('forceBeamColumn', 1, 1, 11, ColTransfTag, ColIntTag1, '-mass', 0.0)
    ops.element('forceBeamColumn', 2, 2, 12, ColTransfTag, ColIntTag2, '-mass', 0.0)
    ops.element('forceBeamColumn', 3, 3, 13, ColTransfTag, ColIntTag1, '-mass', 0.0)
    
    ops.element('forceBeamColumn', 11, 11, 21, ColTransfTag, ColIntTag1, '-mass', 0.0)
    ops.element('forceBeamColumn', 12, 12, 22, ColTransfTag, ColIntTag2, '-mass', 0.0)
    ops.element('forceBeamColumn', 13, 13, 23, ColTransfTag, ColIntTag1, '-mass', 0.0)
    
    ops.element('forceBeamColumn', 21, 21, 31, ColTransfTag, ColIntTag1, '-mass', 0.0)
    ops.element('forceBeamColumn', 22, 22, 32, ColTransfTag, ColIntTag2, '-mass', 0.0)
    ops.element('forceBeamColumn', 23, 23, 33, ColTransfTag, ColIntTag1, '-mass', 0.0)
    
    #  ### Add linear main beam elements, along x-axis
    #element('elasticBeamColumn', 101, 1101, 1201, Abeam, Es, Gs, Jbeam, IbeamY, IbeamZ, beamTransfTag, '-mass', 0.0)
    
    ops.element('forceBeamColumn', 101, 1101, 1201, BeamTranfTag, BeamIntTag1, '-mass', 0.0)
    ops.element('forceBeamColumn', 102, 1202, 1301, BeamTranfTag, BeamIntTag1, '-mass', 0.0)
    
    ops.element('forceBeamColumn', 201, 2101, 2201, BeamTranfTag, BeamIntTag2, '-mass', 0.0)
    ops.element('forceBeamColumn', 202, 2202, 2301, BeamTranfTag, BeamIntTag2, '-mass', 0.0)
    
    ops.element('forceBeamColumn', 301, 3101, 3201, BeamTranfTag, BeamIntTag3, '-mass', 0.0)
    ops.element('forceBeamColumn', 302, 3202, 3301, BeamTranfTag, BeamIntTag3, '-mass', 0.0)
    
    # Assign constraints between beam end nodes and column nodes (RIgid beam column connections)
    ops.equalDOF(11, 1101, 1,2,3)
    ops.equalDOF(12, 1201, 1,2,3)
    ops.equalDOF(12, 1202, 1,2,3)
    ops.equalDOF(13, 1301, 1,2,3)
    
    ops.equalDOF(21, 2101, 1,2,3)
    ops.equalDOF(22, 2201, 1,2,3)
    ops.equalDOF(22, 2202, 1,2,3)
    ops.equalDOF(23, 2301, 1,2,3)
    
    ops.equalDOF(31, 3101, 1,2,3)
    ops.equalDOF(32, 3201, 1,2,3)
    ops.equalDOF(32, 3202, 1,2,3)
    ops.equalDOF(33, 3301, 1,2,3)
    
    AllNodes = ops.getNodeTags()
    massX = 0.49
    
    for nodes in AllNodes:
    	ops.mass(nodes, massX, massX, 0.00001)
    
    
    ################
    ## Gravity Load 
    ################
    # create TimeSeries
    ops.timeSeries("Linear", 1)
    
    # create a plain load pattern
    ops.pattern("Plain", 1, 1)
    
    # Create the nodal load
    ops.load(11, 0.0, -5.0*kip, 0.0)
    ops.load(12, 0.0, -6.0*kip, 0.0)
    ops.load(13, 0.0, -5.0*kip, 0.0)
    
    ops.load(21, 0., -5.*kip, 0.0)
    ops.load(22, 0., -6.*kip,0.0)
    ops.load(23, 0., -5.*kip, 0.0)
    
    ops.load(31, 0., -5.*kip, 0.0)
    ops.load(32, 0., -6.*kip, 0.0)
    ops.load(33, 0., -5.*kip, 0.0)    
    
    ###############################
    ### PUSHOVER ANALYSIS
    ###############################
    
    if(AnalysisType=="Pushover"):
    	
    	print("<<<< Running Pushover Analysis >>>>")
    
    	# Create load pattern for pushover analysis
    	# create a plain load pattern
    	ops.pattern("Plain", 2, 1)
    
    	ops.load(11, 1.61, 0.0, 0.0)
    	ops.load(21, 3.22, 0.0, 0.0)
    	ops.load(31, 4.83, 0.0, 0.0)
    	
    	ControlNode=31
    	ControlDOF=1
    	MaxDisp=0.15*H_story
    	DispIncr=0.1
    	NstepsPush=int(MaxDisp/DispIncr)
    	
    	Model = 'test'
    	LoadCase = 'Pushover'   
    	dt=0.2       
    	opp.createODB(Model, LoadCase, Nmodes = 3)
     
    	ops.system("ProfileSPD")
    	ops.numberer("Plain")
    	ops.constraints("Plain")
    	ops.integrator("DisplacementControl", ControlNode, ControlDOF, DispIncr)
    	ops.algorithm("Newton")
    	ops.test('NormUnbalance',1e-8, 10)
    	ops.analysis("Static")
    
    	
    
    
    # 	analyze(NstepsPush)
    	ops.analyze(100)
    	
    	print("Pushover analysis complete")
