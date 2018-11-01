###########################################################
This python code extracts 16 digit code from the input file
example: 4444555566667777
###########################################################

import re, sys
try:
                inputfile = sys.argv[1]
except:
                print "please enter script.py <inputfile> > <outputfile>"
                sys.exit(1)
file = open(inputfile, 'r')
file = file.read()
cardnum = re.findall(r'\d{16}',file)
for i in range(len(cardnum)):
                print format(cardnum[i])
