# ReadRecord.py
# ------------------------------------------------------------------------------------------------------------
#
# Written: minjie
# Date: May 2016

# A procedure which parses a ground motion record from the PEER
# strong motion database by finding dt in the record header, then
# echoing data values to the output file.
#
# Formal arguments
#	inFilename -- file which contains PEER strong motion record
#	outFilename -- file to be written in format G3 can read
# Return values
#	dt -- time step determined from file header
#	nPts -- number of data points from file header
#
# Assumptions
#	The header in the PEER record is, e.g., formatted as 1 of following:
#  1) new PGA database
#	 PACIFIC ENGINEERING AND ANALYSIS STRONG-MOTION DATA
#	  IMPERIAL VALLEY 10/15/79 2319, EL CENTRO ARRAY 6, 230                           
#	  ACCELERATION TIME HISTORY IN UNITS OF G                                         
#	  3930 0.00500 NPTS, DT

#   2) old SMD database
#	 PACIFIC ENGINEERING AND ANALYSIS STRONG-MOTION DATA
#	  IMPERIAL VALLEY 10/15/79 2319, EL CENTRO ARRAY 6, 230                           
#	  ACCELERATION TIME HISTORY IN UNITS OF G                                         
#	  NPTS=  3930, DT= .00500 SEC


def ReadRecord (inFilename, outFilename):

    dt = 0.0
    npts = 0
    
    # Open the input file and catch the error if it can't be read
    inFileID = open(inFilename, 'r')
    
    # Open output file for writing
    outFileID = open(outFilename, 'w')
	
    # Flag indicating dt is found and that ground motion
    # values should be read -- ASSUMES dt is on last line
    # of header!!!
    flag = 0
	
    # Look at each line in the file
    for line in inFileID:
        if line == '\n':
            # Blank line --> do nothing
            continue
        elif flag == 1:
            # Echo ground motion values to output file
            outFileID.write(line)
        else:
            # Search header lines for dt
            words = line.split()
            lengthLine = len(words)

            if lengthLine >= 4:

                if words[0] == 'NPTS=':
                    # old SMD format
                    for word in words:
                        if word != '':
                            # Read in the time step
                            if flag == 1:
                                dt = float(word)
                                break

                            if flag == 2:
                                npts = int(word.strip(','))
                                flag = 0

                            # Find the desired token and set the flag
                            if word == 'DT=' or word == 'dt':
                                flag = 1

                            if word == 'NPTS=':
                                flag = 2
                        
                    
                elif words[-1] == 'DT':
                    # new NGA format
                    count = 0
                    for word in words:
                        if word != '':
                            if count == 0:
                                npts = int(word)
                            elif count == 1:
                                dt = float(word)
                            elif word == 'DT':
                                flag = 1
                                break

                            count += 1

                        

    inFileID.close()
    outFileID.close()

    return dt, npts
