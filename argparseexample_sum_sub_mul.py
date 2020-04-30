import argparse
import sys
import os
#Specify -h to know the input parameters
try:
    arg1 = sys.argv[1]


except IndexError:
    print "Usage: " + "python" + os.path.basename(__file__) + " -h"
    sys.exit(1)

parser = argparse.ArgumentParser()

parser.add_argument('-add',action='store_true',help="For adding two numbers")
parser.add_argument('-sub',action='store_true',help="For sub two numbers")
parser.add_argument('-mul',action='store_true',help="For mul two numbers")
args = parser.parse_args()

if args.add:
    print ("enter any two numbers to know the sum")
    a = int(input('enter the value of a: '))
    b = int(input('enter the value of b: '))
    def additon(a, b):
        additon = a + b
        print 'sum of two numbers is: ' ,str(additon)
    additon(a, b)

if args.sub:
    print ("enter any two numbers to know the sum")
    a = int(input('enter the value of a: '))
    b = int(input('enter the value of b: '))
    def subraction(a,b):
        subr = int(a - b)
        print 'sub of two num is: ', str(subr)
    subraction(a,b)

if args.mul:
    print ("enter any two numbers to know the sum")
    a = int(input('enter the value of a: '))
    b = int(input('enter the value of b: '))
    def multiplication(a,b):
        mult = int(a * b)
        print 'Mul of two numm is: ', (str(mult))
    multiplication(a,b)



