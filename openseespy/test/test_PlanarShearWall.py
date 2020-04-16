import openseespy.opensees as ops
# Linear Elastic Planar Shear Walls

#REFERENCES: 
# 1) ETABS Software Verification Examples, Computers and Structures, Inc, 2003 (Example 15A)
print("=====================================================================")
print("PlanarShearWall.py: Verification of Linear Elastic Planar Shear Wall")
print("   NOTE: using SAP2000 results for verification")

# Multiple Shear Wall building models with lengths of 120",240" and 360" lengths. Buildings of 1 story, 3 Story and 
# 6 story are modelled. Each buildings story height is 120" All walls 12". All materials elastic with modulus of elasticity 
# of 3000 ksi and poisson's ration of 0.2. At each floor in the buildings al nodes at the floor level are constrained to
# move horizontally together.
#
# Loading: For each building a 100k load is applied at top left node.
# Results: compare nodal displacement at node were load is applied to Etabs and SAP, results verified using SAP.

# NOTE: The discretization of the SAP and ETABS models are not known at this time

def test_PlanarShearWall():

    testOK = 0
    tol = 5.0e-2

    resultsSAP = [2.4287,0.1031,0.0186,0.3205,0.0187,0.0052,0.0185,0.0029,0.0013]
    resultsETABS = [2.3926,0.0985,0.0172,0.3068,0.0169,0.0046,0.0144,0.0024,0.0011]


    # wall properties
    E = 3000.
    v = 0.2
    t = 12.0

    floorHeight = 120.
    bayWidth = 120.

    # modeling parameters # of elements in floorHeight * bayWidth block

    #nxBay   16
    #nyFloor 16
    nxBay = 16
    nyFloor = 16

    # ----------------------------
    # Start of model generation
    # ----------------------------

    # QUAD

    #foreach numFloor {6 3 1} {

    for eleType in ['quad', 'SSPquad']:

        counter = 0
        print('\n - using',eleType, 'elements')

        formatString = '{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}'
        print(formatString.format('# Stories','Wall Height','Wall Length','ETABS', 'SAP2000','OpenSees', 'Difference'))
        formatString = '{:>12.0f}{:>12.0f}{:>12.0f}{:>12.4f}{:>12.4f}{:>12.4f}{:>12.4f}'

        for numFloor in [6,3,1]:
            for numBay in [1,3,6]:
                ops.wipe()
                
                ops.model( 'basic', '-ndm', 2, '-ndf', 2)
                
                ops.nDMaterial( 'ElasticIsotropic', 1,  E, v)
                
                # some parameters for node and element generation
                
                nx = numBay * nxBay     # number of elements along building length
                ny = numFloor * nyFloor # number of elements along building height
                
                nodeTop = (nx+1)*ny + 1
                
                # generate the nodes and elements
                if eleType == 'quad':
                    ops.block2D( nx, ny, 1, 1, eleType,
                            t, 'PlaneStress', 1,
                            1, 0., 0. ,
                            2, bayWidth * numBay, 0. ,
                            3, bayWidth * numBay, floorHeight * numFloor,
                            4, 0., floorHeight*numFloor)
                elif eleType == 'SSPquad':
                    ops.block2D( nx, ny, 1, 1, eleType,
                            1, 'PlaneStress', t,
                            1, 0., 0. ,
                            2, bayWidth * numBay, 0. ,
                            3, bayWidth * numBay, floorHeight * numFloor,
                            4, 0., floorHeight*numFloor)
                    
                # add some loads
                ops.timeSeries('Linear', 1)
                ops.pattern('Plain', 1, 1)
                ops.load(nodeTop,  100.0,  0.0)  
                
                ops.fixY( 0.0,   1, 1) 
                
                #floor constraints
                for i in range(1,numFloor+1):
                    mNode = (nx+1)*nyFloor*i + 1

                    for j in range(1,nx+1):
                        ops.equalDOF( mNode, mNode+j, 1)

                
                ops.integrator('LoadControl',  1.0  )
                ops.algorithm('Linear')
                ops.numberer('RCM')
                ops.constraints('Plain') 
                ops.system("UmfPack")
                ops.analysis('Static') 
                
                ops.analyze(1)
                
                disp = ops.nodeDisp(nodeTop, 1)
                dispETABS = resultsETABS[counter]
                dispSAP = resultsSAP[counter]
                diffR = abs(dispSAP-disp)
                print(formatString.format(numFloor, floorHeight*numFloor, bayWidth*numBay, dispETABS, dispSAP, disp, diffR))
                
                
                # verify result
                if abs(disp-dispSAP) > tol:
                    testOK = -1
                    print('failed  ',eleType,': disp - dispSAP', abs(disp-dispSAP), '>', tol)
                
                counter += 1


    # Shell
    print('\n - using Shell elements')

    formatString = '{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}'
    print(formatString.format('# Stories','Wall Height','Wall Length','ETABS', 'SAP2000','OpenSees', 'Difference'))
    formatString = '{:>12.0f}{:>12.0f}{:>12.0f}{:>12.4f}{:>12.4f}{:>12.4f}{:>12.4f}'

    counter = 0
    for numFloor in [6,3,1]:
        for numBay in [1,3,6]:
            ops.wipe()

            ops.model( 'basic', '-ndm', 3, '-ndf', 6)

            # create the material
    #       t 12.0
    #       nDMaterial ElasticIsotropic 1 E v
    #       nDMaterial PlateFiber 4 1
    #       section PlateFiber 1 4 t

            ops.section('ElasticMembranePlateSection',  1, E, v, t, 0.0)
            
            # some parameters for node and element generation
            Plate = 'shell'
            
            eleArgs = 1

            nx = numBay * nxBay     # number of elements along building length
            ny = numFloor * nyFloor # number of elements along building height      

            nodeTop = (nx+1)*ny + 1
            
            # generate the nodes and elements
            ops.block2D( nx, ny, 1, 1, Plate,
                    1,
                    1, 0., 0. , 0.,
                    2, bayWidth * numBay, 0. , 0., 
                    3, bayWidth * numBay, floorHeight * numFloor, 0.,
                    4, 0., floorHeight*numFloor, 0.)

            # add some loads
            ops.timeSeries('Linear', 1)
            ops.pattern('Plain', 1, 1)
            ops.load(nodeTop,  100.0,  0.0, 0.0, 0.0, 0.0, 0.0)  
        
            ops.fixY( 0.0,   1, 1, 1, 0, 0, 0)

            #floor constraints
            for i in range(1,numFloor+1):
                mNode = (nx+1)*nyFloor*i + 1

                for j in range(1,nx+1):
                    ops.equalDOF( mNode, mNode+j, 1)


            ops.integrator('LoadControl',  1.0  )
            ops.algorithm('Linear')
            ops.numberer('RCM')
            ops.constraints('Plain') 
            ops.system('UmfPack')
            ops.analysis('Static') 
            ops.analyze(1)

            disp = ops.nodeDisp(nodeTop, 1)
            dispETABS = resultsETABS[counter]
            dispSAP = resultsSAP[counter]
            diffR = abs(dispSAP-disp)
            print(formatString.format(numFloor, floorHeight*numFloor, bayWidth*numBay, dispETABS, dispSAP, disp, diffR))

            # verify result
            if abs(disp-dispSAP) > tol:
                testOK = -1
                print('failed  ',eleType,': disp - dispSAP', abs(disp-dispSAP), '>', tol)
                
            counter += 1


    # Brick

    for eleType in ['stdBrick', 'SSPbrick']:

        counter = 0
        print('\n - using',eleType, 'elements')

        formatString = '{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}'
        print(formatString.format('# Stories','Wall Height','Wall Length','ETABS', 'SAP2000','OpenSees', 'Difference'))
        formatString = '{:>12.0f}{:>12.0f}{:>12.0f}{:>12.4f}{:>12.4f}{:>12.4f}{:>12.4f}'

        for numFloor in [6,3,1]:
            for numBay in [1,3,6]:
                ops.wipe()
                
                ops.model( 'basic', '-ndm', 3, '-ndf', 3)
                
                ops.nDMaterial( 'ElasticIsotropic', 1,  E, v)
                
                # some parameters for node and element generation
                
                nx = numBay * nxBay     # number of elements along building length
                ny = numFloor * nyFloor # number of elements along building height
                nz = 1
                
                nodeTop = (nx+1)*ny + 1
                
                # generate the nodes and elements
                ops.block3D( nx, ny, nz, 1, 1, eleType,
                        1,
                        1, 0., 0. ,0.,
                        2, bayWidth * numBay, 0. ,0.,
                        3, bayWidth * numBay, floorHeight * numFloor, 0.,
                        4, 0., floorHeight*numFloor, 0.,
                        5, 0., 0., t,
                        6, bayWidth*numBay, 0., t,
                        7, bayWidth*numBay, floorHeight * numFloor, t,
                        8, 0., floorHeight * numFloor, t)
                    
                # add some loads
                ops.timeSeries('Linear', 1)
                ops.pattern('Plain', 1, 1)
                ops.load(nodeTop,  50.0,  0.0, 0.0)
                ops.load(nodeTop+(nx+1)*(ny+1), 50.0, 0.0, 0.0)
                
                ops.fixY( 0.0,   1, 1, 1) 
                
                #floor constraints
                for i in range(1,numFloor+1):
                    mNode1 = (nx+1)*nyFloor*i + 1
                    mNode2 = mNode1 + (nx+1)*(ny+1)

                    for j in range(1,nx+1):
                        ops.equalDOF(mNode1, mNode1+j, 1)
                        ops.equalDOF(mNode2, mNode2+j, 1)

                
                ops.integrator('LoadControl',  1.0  )
                ops.algorithm('Linear')
                ops.numberer('RCM')
                ops.constraints('Plain') 
                ops.system('UmfPack')
                ops.analysis('Static') 
                
                ops.analyze(1)
                
                disp = ops.nodeDisp(nodeTop, 1)
                dispETABS = resultsETABS[counter]
                dispSAP = resultsSAP[counter]
                diffR = abs(dispSAP-disp)
                print(formatString.format(numFloor, floorHeight*numFloor, bayWidth*numBay, dispETABS, dispSAP, disp, diffR))
                
                
                # verify result
                if abs(disp-dispSAP) > tol:
                    testOK = -1
                    print('failed  ',eleType,': disp - dispSAP', abs(disp-dispSAP), '>', tol)
                
                counter += 1

    assert testOK == 0
