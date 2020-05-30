import openseespy.opensees as ops
from math import asin
# Bathe & Wilson eigenvalue problem
#   Results presented by Bathe & wilson in 1972
#   and again by Peterson in 1981

#REFERENCES: 
# 1) Bathe, K.J and Wilson, E.L.Large Eigenvalue Problems in Synamic Analysis, ASCE,
# Journal of Eng. Mech.. Division, 98(6), 1471-1485, 
# 2) Peterson, F.E. EASE2, Elastic Analysis for Structural Engineering, Example Problem Manual, 
# Engineering Analysis Corporation, Berkeley, CA 1981.

# used in verification by SAP2000:
# SAP2000 Integrated Finite Element Analysis and Design of Structures, Verification Manual, 
# Computers and Structures, 1997. Example 2.
# and seismo-struct (Example 10)
# SeismoStruct, Verification Report For Version 6, 2012. Example 10.

print("=====================================================================")
print("EigenFrame.py: Verification 2d Bathe & Wilson original Elastic Frame")
print("  - eigenvalue ")
def test_EigenFrame():
    ops.wipe()

    ops.model( 'Basic', '-ndm', 2)

    #    units kip, ft                                                                                                                              

    # properties  
    bayWidth = 20.0
    storyHeight = 10.0

    numBay = 10
    numFloor = 9
    A = 3.0         #area = 3ft^2    
    E = 432000.0   #youngs mod = 432000 k/ft^2  
    I = 1.0         #second moment of area I=1ft^4       
    M = 3.0      #mas/length = 4 kip sec^2/ft^2       
    coordTransf = "Linear"  # Linear, PDelta, Corotational
    massType = "-lMass"  # -lMass, -cMass


    # add the nodes         
    #  - floor at a time    
    nodeTag = 1
    yLoc = 0.
    for j in range(0,numFloor+1):
        xLoc = 0.
        for i in range(0,numBay+1):
            ops.node( nodeTag, xLoc, yLoc)
            xLoc += bayWidth
            nodeTag += 1

        yLoc += storyHeight


    # fix base nodes
    for i in range(1,numBay+2):
        ops.fix( i, 1, 1, 1)


    # add column element    
    ops.geomTransf(coordTransf, 1)
    eleTag = 1
    for i in range(0,numBay+1):
        end1 = i+1
        end2 = end1 + numBay + 1
        for j in range(0,numFloor):
            ops.element( 'elasticBeamColumn', eleTag, end1, end2, A, E, I, 1, '-mass', M, massType)
            end1 = end2
            end2 = end1 + numBay +1
            eleTag += 1
        


    # add beam elements
    for j in range(1,numFloor+1):
        end1 = (numBay+1)*j+1
        end2 = end1 + 1
        for i in range(0,numBay):
            ops.element( 'elasticBeamColumn', eleTag, end1, end2, A, E, I, 1, '-mass', M, massType)
            end1 = end2
            end2 = end1 + 1
            eleTag += 1
        


    # calculate eigenvalues
    numEigen = 3
    eigenValues = ops.eigen( numEigen)
    PI = 2*asin(1.0)

    #recorder('PVD','EigenFrame','eigen',numEigen)
    #record()

    # determine PASS/FAILURE of test
    testOK = 0

    # print table of camparsion
    #                         Bathe & Wilson               Peterson                    SAP2000                  SeismoStruct
    comparisonResults = [[0.589541,5.52695,16.5878],[0.589541,5.52696,16.5879],[0.589541,5.52696,16.5879],[0.58955,5.527,16.588]]
    print("\n\nEigenvalue Comparisons:")
    tolerances = [9.99e-6, 9.99e-6, 9.99e-5] # tolerances prescribed by documented precision
    formatString = '{:>15}{:>15}{:>15}{:>15}{:>15}'
    print(formatString.format('OpenSees', 'Bathe&Wilson', 'Peterson', 'SAP2000', 'SeismoStruct'))
    formatString =  '{:>15.5f}{:>15.4f}{:>15.4f}{:>15.4f}{:>15.3f}'
    for i in range(0,numEigen):
        lamb = eigenValues[i]
        print(formatString.format(lamb, comparisonResults[0][i], comparisonResults[1][i], comparisonResults[2][i], comparisonResults[3][i]))
        resultOther = comparisonResults[2][i]
        tol = tolerances[i]
        if abs(lamb-resultOther) > tol:
            testOK = -1
            print("failed->", abs(lamb-resultOther), tol)
        

    assert testOK == 0

