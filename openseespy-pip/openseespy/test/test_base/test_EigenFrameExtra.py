import openseespy.opensees as ops
from math import asin
# This Extends EigenFrame.py verification test to:
#   1) run different element options to test: ForceBeamColumn, DspBeamColumn, ElasticSection and FiberSection2d.
#   2) run different solver options to test:

# REFERENCES
#   as per EigenFrame.py
print("================================================================================================")
print("EigenFrame.Extra.py: Verification 2d Bathe & Wilson original Elastic Frame - with other options")
print("  - eigenvalue ")

def test_EigenFrameExtra():

    eleTypes = ['elasticBeam', 'forceBeamElasticSection', 'dispBeamElasticSection', 'forceBeamFiberSectionElasticMaterial', 'dispBeamFiberSectionElasticMaterial']

    for eleType in eleTypes:

        ops.wipe()

        ops.model('Basic', '-ndm', 2)
        
        #    units kip, ft                                                                                                                              
        
        # properties  
        bayWidth = 20.0
        storyHeight = 10.0
        
        numBay = 10
        numFloor = 9

        A = 3.0         #area = 3ft^2    
        E = 432000.0    #youngs mod = 432000 k/ft^2  
        I = 1.0         #second moment of area I=1ft^4       
        M = 3.0         #mas/length = 4 kip sec^2/ft^2           
        coordTransf = "Linear"  # Linear, PDelta, Corotational
        massType = "-lMass"  # -lMass, -cMass


        nPts = 3      # numGauss Points

        # an elastic material
        ops.uniaxialMaterial( 'Elastic', 1, E)

        # an elastic section
        ops.section( 'Elastic', 1, E, A, I)
            
        # a fiber section with A=3 and I = 1 (b=1.5, d=2) 2d bending about y-y axis
    #   b 1.5 d 2.0
        y = 2.0
        z = 1.5
        numFiberY = 2000  # note we only need so many to get the required accuracy on eigenvalue 1e-7!
        numFiberZ = 1
        ops.section( 'Fiber', 2) 
        #   patch rect 1 numFiberY numFiberZ 0.0 0.0 z y
        ops.patch( 'quad', 1,numFiberY,numFiberZ,-y/2.0,-z/2.0,y/2.0,-z/2.0,y/2.0,z/2.0,-y/2.0,z/2.0)
        
        

        # add the nodes         
        #  - floor at a time    
        nodeTag = 1
        yLoc = 0.
        for j in range(0,numFloor+1):
            xLoc = 0.
            for i in range(numBay+1):
                ops.node( nodeTag, xLoc, yLoc)
                xLoc += bayWidth
                nodeTag += 1
            
            yLoc += storyHeight

        
        # fix base nodes
        for i in range(1,numBay+2):
            ops.fix( i, 1, 1, 1)

        # add column element
        transfTag = 1
        ops.geomTransf( coordTransf, transfTag)
        integTag1 = 1
        ops.beamIntegration( 'Lobatto', integTag1, 1, nPts)
        integTag2 = 2
        ops.beamIntegration( 'Lobatto', integTag2, 2, nPts)
        eleTag = 1
        for i in range(numBay+1):
            end1 = i+1
            end2 = end1 + numBay +1
            for j in range(numFloor):

                if eleType == "elasticBeam": 
                    ops.element( 'elasticBeamColumn', eleTag, end1, end2, A, E, I, 1, '-mass', M, massType)
                elif eleType == "forceBeamElasticSection":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M)
                elif eleType == "dispBeamElasticSection": 
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M, massType)
                elif eleType == "forceBeamFiberSectionElasticMaterial":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M)
                elif eleType == "dispBeamFiberSectionElasticMaterial":
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M, massType)
                else: 
                    print("BARF")
                
                end1 = end2
                end2 = end1 + numBay +1
                eleTag += 1
            
        
        

        # add beam elements
        for j in range(1,numFloor+1):
            end1 = (numBay+1)*j+1
            end2 = end1 + 1
            for i in range(numBay):
                if eleType == "elasticBeam":
                    ops.element('elasticBeamColumn', eleTag, end1, end2, A, E, I, 1, '-mass', M, massType)
                elif eleType == "forceBeamElasticSection":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M)
                elif eleType == "dispBeamElasticSection":
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M, massType)
                elif eleType == "forceBeamFiberSectionElasticMaterial":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M)
                elif eleType == "dispBeamFiberSectionElasticMaterial":
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M, massType)
                else:
                    print("BARF")
                
    #           element(elasticBeamColumn eleTag end1 end2 A E I 1 -mass M
                end1 = end2
                end2 = end1 + 1
                eleTag += 1
            
        
        
        # calculate eigenvalues
        numEigen = 3
        eigenValues =ops.eigen( numEigen)
        PI = 2*asin(1.0)
        
        # determine PASS/FAILURE of test
        testOK = 0

        # print table of camparsion
        #                         Bathe & Wilson               Peterson                    SAP2000                  SeismoStruct

        comparisonResults = [[0.589541,5.52695,16.5878],[0.589541,5.52696,16.5879],[0.589541,5.52696,16.5879],[0.58955,5.527,16.588]]
        print("\n\nEigenvalue Comparisons for eleType:", eleType)
        tolerances = [9.99e-7, 9.99e-6, 9.99e-5]
        formatString = '{:>15}{:>15}{:>15}{:>15}{:>15}'
        print(formatString.format('OpenSees', 'Bathe&Wilson', 'Peterson', 'SAP2000', 'SeismoStruct'))
        formatString = '{:>15.5f}{:>15.4f}{:>15.4f}{:>15.4f}{:>15.3f}'
        for i in range(numEigen):
            lamb = eigenValues[i]
            print(formatString.format(lamb, comparisonResults[0][i], comparisonResults[1][i], comparisonResults[2][i], comparisonResults[3][i]))
            resultOther = comparisonResults[2][i]
            tol = tolerances[i]
            if abs(lamb-resultOther) > tol:
                testOK = -1
                print("failed->", abs(lamb-resultOther), tol)
            
        
        
        assert testOK == 0


    solverTypes = ['-genBandArpack', '-fullGenLapack', '-UmfPack', '-SuperLU', '-ProfileSPD']

    for solverType in solverTypes:

        eleType = 'elasticBeam'

        
        ops.wipe()

        ops.model('Basic', '-ndm', 2)
        
        #    units kip, ft                                                                                                                              
        
        # properties  
        bayWidth = 20.0
        storyHeight = 10.0
        
        numBay = 10
        numFloor = 9

        A = 3.0         #area = 3ft^2    
        E = 432000.0    #youngs mod = 432000 k/ft^2  
        I = 1.0         #second moment of area I=1ft^4       
        M = 3.0         #mas/length = 4 kip sec^2/ft^2           
        coordTransf = "Linear"  # Linear, PDelta, Corotational
        massType = "-lMass"  # -lMass, -cMass


        nPts = 3      # numGauss Points

        # an elastic material
        ops.uniaxialMaterial( 'Elastic', 1, E)

        # an elastic section
        ops.section( 'Elastic', 1, E, A, I)
            
        # a fiber section with A=3 and I = 1 (b=1.5, d=2) 2d bending about y-y axis
    #   b 1.5 d 2.0
        y = 2.0
        z = 1.5
        numFiberY = 2000  # note we only need so many to get the required accuracy on eigenvalue 1e-7!
        numFiberZ = 1
        ops.section( 'Fiber', 2) 
        #   patch rect 1 numFiberY numFiberZ 0.0 0.0 z y
        ops.patch( 'quad', 1,numFiberY,numFiberZ,-y/2.0,-z/2.0,y/2.0,-z/2.0,y/2.0,z/2.0,-y/2.0,z/2.0)
        
        

        # add the nodes         
        #  - floor at a time    
        nodeTag = 1
        yLoc = 0.
        for j in range(0,numFloor+1):
            xLoc = 0.
            for i in range(numBay+1):
                ops.node( nodeTag, xLoc, yLoc)
                xLoc += bayWidth
                nodeTag += 1
            
            yLoc += storyHeight

        
        # fix base nodes
        for i in range(1,numBay+2):
            ops.fix( i, 1, 1, 1)

        # add column element
        transfTag = 1
        ops.geomTransf( coordTransf, transfTag)
        integTag1 = 1
        ops.beamIntegration( 'Lobatto', integTag1, 1, nPts)
        integTag2 = 2
        ops.beamIntegration( 'Lobatto', integTag2, 2, nPts)
        eleTag = 1
        for i in range(numBay+1):
            end1 = i+1
            end2 = end1 + numBay +1
            for j in range(numFloor):

                if eleType == "elasticBeam": 
                    ops.element( 'elasticBeamColumn', eleTag, end1, end2, A, E, I, 1, '-mass', M, massType)
                    
                elif eleType == "forceBeamElasticSection":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M)
                        
                elif eleType == "dispBeamElasticSection": 
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M, massType)
                elif eleType == "forceBeamFiberSectionElasticMaterial":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M)
                    
                elif eleType == "dispBeamFiberSectionElasticMaterial":
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M, massType)
                else: 
                    print("BARF")
                
                end1 = end2
                end2 = end1 + numBay +1
                eleTag += 1
            
        
        

        # add beam elements
        for j in range(1,numFloor+1):
            end1 = (numBay+1)*j+1
            end2 = end1 + 1
            for i in range(numBay):
                if eleType == "elasticBeam":
                    ops.element('elasticBeamColumn', eleTag, end1, end2, A, E, I, 1, '-mass', M, massType)
                elif eleType == "forceBeamElasticSection":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M)
                elif eleType == "dispBeamElasticSection":
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag1, '-mass', M, massType)
                elif eleType == "forceBeamFiberSectionElasticMaterial":
                    ops.element('forceBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M)
                elif eleType == "dispBeamFiberSectionElasticMaterial":
                    ops.element('dispBeamColumn', eleTag, end1, end2, transfTag, integTag2, '-mass', M, massType)
                else:
                    print("BARF")
                
    #           element(elasticBeamColumn eleTag end1 end2 A E I 1 -mass M
                end1 = end2
                end2 = end1 + 1
                eleTag += 1
            
        
        
        # calculate eigenvalues
        numEigen = 3
        eigenValues =ops.eigen(solverType, numEigen)
        PI = 2*asin(1.0)
        
        # determine PASS/FAILURE of test
        testOK = 0

        # print table of camparsion
        #                         Bathe & Wilson               Peterson                    SAP2000                  SeismoStruct

        comparisonResults = [[0.589541,5.52695,16.5878],[0.589541,5.52696,16.5879],[0.589541,5.52696,16.5879],[0.58955,5.527,16.588]]
        print("\n\nEigenvalue Comparisons for solverType:", solverType)
        tolerances = [9.99e-7, 9.99e-6, 9.99e-5]
        formatString = '{:>15}{:>15}{:>15}{:>15}{:>15}'
        print(formatString.format('OpenSees', 'Bathe&Wilson', 'Peterson', 'SAP2000', 'SeismoStruct'))
        formatString = '{:>15.5f}{:>15.4f}{:>15.4f}{:>15.4f}{:>15.3f}'
        for i in range(numEigen):
            lamb = eigenValues[i]
            print(formatString.format(lamb, comparisonResults[0][i], comparisonResults[1][i], comparisonResults[2][i], comparisonResults[3][i]))
            resultOther = comparisonResults[2][i]
            tol = tolerances[i]
            if abs(lamb-resultOther) > tol:
                testOK = -1
                print("failed->", abs(lamb-resultOther), tol)
            
        
        assert testOK == 0

        
