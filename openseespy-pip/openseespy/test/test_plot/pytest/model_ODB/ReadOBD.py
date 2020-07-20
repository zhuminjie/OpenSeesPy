import numpy as np
import os
import openseespy.postprocessing.Get_Rendering as opp


def GenerateTests():
    
    # Used to make the test files.
    
    # These are hard coded in right now - there is nothing stoping the values
    # From changing
    ModelName = 'TestModel'
    LoadCaseName = 'TestLoadCase'
    
    baseDir = os.getcwd()
    
    ODBdir = ModelName+"_ODB"		# ODB Dir name
    LoadCaseDir = os.path.join(ODBdir,LoadCaseName)

    if not os.path.exists(LoadCaseDir):
        os.makedirs(LoadCaseDir)    
    
    os.chdir(ODBdir)
    
    OutputNames = [ 'Nodes','Elements_2Node', 'Elements_3Node', 'Elements_4Node', 
                   'Elements_8Node']     
    
    OuputputFiles  = [Name + '.out' for Name in OutputNames]
    
    for ii, File in enumerate(OuputputFiles):
        tempArray = np.ones([10,3])*ii
        
        np.savetxt(File,tempArray)    
        
    os.chdir(LoadCaseDir)

    OutputNames = [ "NodeDisp_All", "EleForce_All", 
                   'Reaction_All', 'EleStress_All','EleStrain_All', 
                   'EleBasicDef_All', 'ElePlasticDef_All' , 'EleIntPoints_All']
    
    OuputputFiles  = [Name + '.out' for Name in OutputNames]
    
    
    for ii, File in enumerate(OuputputFiles):
        tempArray = np.ones([10,3])*(ii + 5)
        
        np.savetxt(File,tempArray)

    os.chdir(baseDir)
# # GenerateTests()
# [nodes, elements, NodeDisp, Reaction, EleForce] = opp.readODB('TestModel', 'TestLoadCase')
# # [nodes, elements, NodeDisp] = opp.readODB('TestModel', 'TestLoadCase')
    
# # We don't check everything, we just do a few manual tests.
# check1 = np.all(nodes == np.ones([10,3])*0)
# check2 = np.all(elements[4] == np.array([1., 1., 1.]))
# check3 = np.all(EleForce == np.ones([10,3])*6)
# # check4 = len(EleStress[:,0]) == 10

# check = np.all([check1,check2,check3])
# # check = np.all([check1,check2])

# assert check == True


def test_readODB():
    
    
    
    [nodes, elements, NodeDisp, Reaction, EleForce] = opp.readODB('TestModel', 'TestLoadCase')
    # [nodes, elements, NodeDisp] = opp.readODB('TestModel', 'TestLoadCase')
        
    # We don't check everything, we just do a few manual tests.
    check1 = np.all(nodes == np.ones([10,3])*0)
    check2 = np.all(elements[4] == np.array([1., 1., 1.]))
    check3 = np.all(EleForce == np.ones([10,3])*6)
    # check4 = len(EleStress[:,0]) == 10
    
    check = np.all([check1,check2,check3])
    # check = np.all([check1,check2])
    
    assert check == True
    # return check
# test_readODB()