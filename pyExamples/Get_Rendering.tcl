##############################################################################################
## This script records the Nodes, Elements and the mode shape data in order to plot			##
##  the model, mode shapes,the displaced structure using OpenSeesPy Get_Rendering library.	##
##  The capability to visualize and animate element force, stress, strain is not available	##
##  to OpenSees Tcl users yet. It will be added soon.										##
##																							##
## Created By - Anurag Upadhyay, University of Utah, 06-28-2020.							##
##																							##
## Submit bugs on the development GitHub page: https://github.com/u-anurag/OpenSeesPy		##
##############################################################################################

## How to use this file: Source this script into the main OpenSees file and then use the 
#  functions as described below in the examples. The function "createODB" takes three
#  inputs and all of them are needed.

#  modelName     - Name of the opensees output folder will be named as "modelName_ODB".
#  loadCaseName  - "none" or "loadCaseName". Name of the sub-folder to store load case specific output.
#  numModes      - 0 or numModes (integer). Number of modeshapes to be recorded. Use 0 when recording output from a loadcase.

## Example 1 - To record 3 mode shapes        : createODB "TwoSpan_Bridge"  "none"   3
## Example 2 - To record output from Pushover : createODB "TwoSpan_Bridge"  "Pushover"   0

proc createODB {modelName loadCaseName numModes} {
	#########################################################
	### DO NOT CHANGE anything beyond this line				#
	#########################################################

	set odb "_ODB"
	set ODB_Dir $modelName$odb
	set LoadCaseDir $ODB_Dir/$loadCaseName

	file mkdir $ODB_Dir

	set NodeFile "$ODB_Dir/Nodes.out"
	set fieldNodes [open $NodeFile w+]

	set ele2nodeFile "$ODB_Dir/Elements_2Node.out"
	set ele3nodeFile "$ODB_Dir/Elements_3Node.out"
	set ele4nodeFile "$ODB_Dir/Elements_4Node.out"
	set ele8nodeFile "$ODB_Dir/Elements_8Node.out"

	set field_ele2node [open $ele2nodeFile w+]
	set field_ele3node [open $ele3nodeFile w+]
	set field_ele4node [open $ele4nodeFile w+]
	set field_ele8node [open $ele8nodeFile w+]

	set listNodes		[getNodeTags] ; # Get all the node tags in the current domain
	set listElements	[getEleTags]  ; # get all the element tags in the current domain

	foreach nodeTag $listNodes {
		set tempNode [nodeCoord $nodeTag]
		puts $fieldNodes	"$nodeTag $tempNode"
		unset tempNode
		}
		
	foreach eleTag $listElements {
		set tempEle [eleNodes $eleTag]
		if {[llength $tempEle] == 2} {
			puts $field_ele2node "$eleTag $tempEle"
			}
		if {[llength $tempEle] == 3} {
			puts $field_ele3node "$eleTag $tempEle"
			}
		if {[llength $tempEle] == 4} {
			puts $field_ele4node "$eleTag $tempEle"
			}
		if {[llength $tempEle] == 8} {
			puts $field_ele8node "$eleTag $tempEle"
			}
			
		unset tempEle
		}
		
	close $fieldNodes
	close $field_ele2node  
	close $field_ele3node  
	close $field_ele4node  
	close $field_ele8node

	#####################################
	## Record load case specific data  ##
	#####################################

	if {$loadCaseName == "none"} {
		puts "No load case folder name provided."
	} else {

		file mkdir $LoadCaseDir

		set N [llength $listNodes]
		set Nele [llength $listElements]
		set NodeOne [nodeCoord [lindex $listNodes 0]]
		if {[llength $NodeOne] == 2} {
			puts "Recording output for 2D Model"
			recorder Node -file $LoadCaseDir/NodeDisp_All.out  -time -nodeRange [lindex $listNodes 0] [lindex $listNodes [expr $N-1]] -dof 1 2 disp;  #  
			recorder Node -file $LoadCaseDir/Reaction_All.out  -time -nodeRange [lindex $listNodes 0] [lindex $listNodes [expr $N-1]] -dof 1 2 reaction;  #  
			# recorder Element -file $LoadCaseDir/EleForce_All.out  -time -eleRange [lindex $listElements 0] [lindex $listElements [expr $Nele-1]] -dof 1 2 localForce;  #  
			# recorder Element -file $LoadCaseDir/EleStress_All.out  -time -eleRange [lindex $listElements 0] [lindex $listElements [expr $Nele-1]] -dof 1 2 stresses;  #  
			# recorder Element -file $LoadCaseDir/EleStrain_All.out  -time -eleRange [lindex $listElements 0] [lindex $listElements [expr $Nele-1]] -dof 1 2 strains;  #  
		} else {
			puts "Recording output for 3D model"
			recorder Node -file $LoadCaseDir/NodeDisp_All.out  -time -nodeRange [lindex $listNodes 0] [lindex $listNodes [expr $N-1]] -dof 1 2 3 disp;  #  
			recorder Node -file $LoadCaseDir/Reaction_All.out  -time -nodeRange [lindex $listNodes 0] [lindex $listNodes [expr $N-1]] -dof 1 2 3 reaction;  #  
			# recorder Element -file $LoadCaseDir/EleForce_All.out  -time -eleRange [lindex $listElements 0] [lindex $listElements [expr $Nele-1]] -dof 1 2 3 localForce;  #  
			# recorder Element -file $LoadCaseDir/EleStress_All.out  -time -eleRange [lindex $listElements 0] [lindex $listElements [expr $Nele-1]] -dof 1 2 3 stresses;  #  
			# recorder Element -file $LoadCaseDir/EleStrain_All.out  -time -eleRange [lindex $listElements 0] [lindex $listElements [expr $Nele-1]] -dof 1 2 3 strains;  #  
			}
		#
	}

	if {$numModes > 0} {

		set DirName "ModeShapes"
		set modeShapeDir $ODB_Dir/$DirName
		file mkdir $modeShapeDir
		set periodFile "$modeShapeDir/ModalPeriods.out"
		set fieldperiodFile [open $periodFile w+]
			
		set wa	[eigen -genBandArpack  $numModes];
		
		for {set mode 1} {$mode <=$numModes} {incr mode} { 
			set wwa  [lindex $wa [expr $mode-1]]
			set Ta  [expr 2*3.1415926535/sqrt($wwa)];
			puts $fieldperiodFile "$Ta" 
		}
		close $fieldperiodFile
		
		proc getModeShapeData {modeNumber modeShapeDir} {
			
			set nodeList		[getNodeTags] 
			set nodeOne			[lindex $nodeList 0]
			set ndm  [llength [nodeCoord $nodeOne]]
			
			set prefix "ModeShape"
			set ModeShapeFile "$modeShapeDir/$prefix$modeNumber.out"
			set fieldModeShape [open $ModeShapeFile w+]
			
			foreach nodeTag $nodeList {
				set tempNodeData [nodeEigenvector $nodeTag $modeNumber]
				puts $fieldModeShape "$nodeTag [lrange $tempNodeData 0 [expr $ndm-1]]"
			}
			
			close $fieldModeShape
			}

		for {set i 1} {$i <= $numModes} {incr i} {

			getModeShapeData $i $modeShapeDir
		}
	#
	}

}

