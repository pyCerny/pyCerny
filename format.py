#!/usr/bin/python

import sys, getopt


inputfile = ''
outputfile = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
    print 'test.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
for opt, arg in opts:
    print opt, arg
print 'arg'
for arga in args:
	print arga

    #if opt == '-h':
    #    print 'test.py -i <inputfile> -o <outputfile>'
    #    sys.exit()
    #elif opt in ("-i", "--ifile"):
    #    inputfile = arg
    #elif opt in ("-o", "--ofile"):
    #    outputfile = arg

print 'Input file is "', inputfile
print 'Output file is "', outputfile


data = open("test.txt").readlines()
for x in range(0, len(data)-1):
	data.insert(1+2*x,'\n---\n\n')
#print ''.join(data)
