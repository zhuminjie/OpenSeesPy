import openseespy.opensees as ops

from math import asin, sqrt
# Two dimenional Frame: Eigenvalue & Static Loads


# REFERENCES:
# used in verification by SAP2000:
# SAP2000 Integrated Finite Element Analysis and Design of Structures, Verification Manual, 
# Computers and Structures, 1997. Example 1.
# and seismo-struct (Example 10)
# SeismoStruct, Verification Report For Version 6, 2012. Example 11.

def test_PortalFrame2d():

    # set some properties
    print("================================================")
    print("PortalFrame2d.py: Verification 2d Elastic Frame")
    print("  - eigenvalue and static pushover analysis")

    ops.wipe()

    ops.model( 'Basic', '-ndm', 2)

    # properties  

    #    units kip, ft

    numBay = 2
    numFloor = 7

    bayWidth = 360.0
    storyHeights = [162.0, 162.0, 156.0, 156.0, 156.0, 156.0, 156.0]

    E = 29500.0
    massX = 0.49
    M = 0.
    coordTransf = "Linear"  # Linear, PDelta, Corotational
    massType = "-lMass"  # -lMass, -cMass


    beams =  ['W24X160', 'W24X160', 'W24X130', 'W24X130', 'W24X110', 'W24X110', 'W24X110']
    eColumn = ['W14X246', 'W14X246', 'W14X246', 'W14X211', 'W14X211', 'W14X176', 'W14X176']
    iColumn = ['W14X287', 'W14X287', 'W14X287', 'W14X246', 'W14X246', 'W14X211', 'W14X211']
    columns = [eColumn,iColumn,eColumn]


    WSection = {
        'W14X176': [51.7, 2150.],
        'W14X211': [62.1, 2670.],
        'W14X246': [72.3, 3230.],
        'W14X287': [84.4, 3910.],
        'W24X110': [32.5, 3330.],
        'W24X130': [38.3, 4020.],
        'W24X160': [47.1, 5120.]
    }

    nodeTag = 1


    # procedure to read 
    def ElasticBeamColumn(eleTag, iNode, jNode, sectType, E, transfTag, M, massType):

        found = 0

        prop = WSection[sectType]

        A = prop[0]
        I = prop[1]
        ops.element('elasticBeamColumn', eleTag, iNode, jNode, A, E, I, transfTag, '-mass', M, massType)


    # add the nodes         
    #  - floor at a time    
    yLoc = 0.
    for j in range(0,numFloor+1):

        xLoc = 0.
        for i in range(0,numBay+1):
            ops.node(nodeTag, xLoc, yLoc)
            xLoc += bayWidth
            nodeTag += 1

        if j < numFloor:
            storyHeight = storyHeights[j]

        yLoc += storyHeight


    # fix first floor
    ops.fix( 1, 1, 1, 1)
    ops.fix( 2, 1, 1, 1)
    ops.fix( 3, 1, 1, 1)

    #rigid floor constraint & masses
    nodeTagR  = 5
    nodeTag = 4
    for j in range(1,numFloor+1):
        for i in range(0,numBay+1):

            if nodeTag != nodeTagR:
                ops.equalDOF(nodeTagR, nodeTag, 1)
            else:
                ops.mass( nodeTagR, massX, 1.0e-10, 1.0e-10)

            nodeTag += 1

        nodeTagR += numBay+1


    # add the columns
    # add column element    
    ops.geomTransf(coordTransf, 1)
    eleTag = 1
    for j in range(0,numBay+1):

        end1 = j+1
        end2 = end1 + numBay +1
        thisColumn = columns[j]

        for i in range(0,numFloor):
            secType = thisColumn[i]
            ElasticBeamColumn(eleTag, end1, end2, secType, E, 1, M, massType)
            end1 = end2
            end2 += numBay +1
            eleTag += 1
        


    # add beam elements
    for j in range(1,numFloor+1):
        end1 = (numBay+1)*j+1
        end2 = end1 + 1
        secType = beams[j-1]
        for i in range(0,numBay):
            ElasticBeamColumn(eleTag, end1, end2, secType, E, 1, M, massType)
            end1 = end2
            end2 = end1 + 1
            eleTag += 1
        


    # calculate eigenvalues & print results     
    numEigen = 7
    eigenValues = ops.eigen(numEigen)
    PI = 2*asin(1.0)

    #
    # apply loads for static analysis & perform analysis
    #

    ops.timeSeries('Linear', 1)
    ops.pattern('Plain', 1, 1) 
    ops.load(  22, 20.0, 0., 0.)
    ops.load( 19, 15.0, 0., 0.)
    ops.load( 16, 12.5, 0., 0.)
    ops.load( 13, 10.0, 0., 0.)
    ops.load( 10,  7.5, 0., 0.)
    ops.load(  7,  5.0, 0., 0.)
    ops.load(  4,  2.5, 0., 0.) 

    ops.integrator('LoadControl', 1.0)
    ops.algorithm('Linear')
    ops.analysis('Static')
    ops.analyze(1)

    # determine PASS/FAILURE of test
    ok = 0

    #
    # print pretty output of comparsions
    #

    #               SAP2000   SeismoStruct
    comparisonResults = [[1.2732, 0.4313, 0.2420, 0.1602, 0.1190, 0.0951, 0.0795], [1.2732, 0.4313, 0.2420, 0.1602, 0.1190, 0.0951, 0.0795]]
    print("\n\nPeriod Comparisons:")
    print('{:>10}{:>15}{:>15}{:>15}'.format('Period','OpenSees','SAP2000','SeismoStruct'))

    #formatString {%10s%15.5f%15.4f%15.4f}
    for i in range(0,numEigen):
        lamb = eigenValues[i]
        period = 2*PI/sqrt(lamb)
        print('{:>10}{:>15.5f}{:>15.4f}{:>15.4f}'.format(i+1,period,comparisonResults[0][i],comparisonResults[1][i]))
        resultOther = comparisonResults[0][i]
        if abs(period-resultOther) > 9.99e-5:
            ok = -1



    # print table of camparsion
    #       Parameter          SAP2000   SeismoStruct
    comparisonResults = [["Disp Top", "Axial Force Bottom Left", "Moment Bottom Left"], [1.45076, 69.99, 2324.68], [1.451, 70.01, 2324.71]]
    tolerances = [9.99e-6, 9.99e-3, 9.99e-3]

    print("\n\nSatic Analysis Result Comparisons:")
    print('{:>30}{:>15}{:>15}{:>15}'.format('Parameter', 'OpenSees', 'SAP2000', 'SeismoStruct'))
    for i in range(3):
        response = ops.eleResponse(1,'forces')
        if i==0:
            result = ops.nodeDisp( 22, 1)
        elif i==1:
            result = abs(response[1])
        else:
            result = response[2]

        print('{:>30}{:>15.3f}{:>15.2f}{:>15.2f}'.format(comparisonResults[0][i],result,comparisonResults[1][i],comparisonResults[2][i]))
        resultOther = comparisonResults[1][i]
        tol = tolerances[i]
        if abs(result-resultOther) > tol:
            ok = -1
            print("failed-> ", i, abs(result-resultOther), tol)
        


    assert ok==0


