#!/usr/bin/python
import sys
import math

fin = open(sys.argv[1], "r")
fout = open(str(sys.argv[1][:-3] + ".outref"), "w")

line = fin.readline()

ls = line[:-1].split(" ")
rows = int(ls[0])
cols = int(ls[1])
L = int(ls[2])
H = int(ls[3])

matrix = [[0 for i in range(cols)] for j in range(rows)]
divPairs = []
slices = 0

def buildMatrix():
	global matrix
	for i in range(rows):
		line = fin.readline()
		for j in range(cols):
		    if line[j] == 'T':
		        matrix[i][j] = 1
		    else:
		        matrix[i][j] = 0

def satisfySlice(x1, x2, y1, y2):
    t = 0
    m = 0
    if x2 >= rows:
        return False
    if y2 >= cols:
        return False
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if matrix[i][j] is 1:
                t += 1
            if matrix[i][j] is 0:
                m += 1
            if matrix[i][j] is -1:
            	return False
    if t >= L and m >= L:
        return True
    return False

def cutSlice(x1, x2, y1, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            matrix[i][j] = -1

def computeDivs():
    for i in range(H, 2*L-1, -1):
        for j in range(1, i+1):
            if i % j == 0:
                t1 = (j, i/j)
                divPairs.append(t1)

def findBiggestSlice(icurr, jcurr):
    for tup in divPairs:
        if satisfySlice(icurr, icurr + tup[0] - 1, jcurr, jcurr + tup[1] - 1) is True:
            cutSlice(icurr, icurr + tup[0] - 1, jcurr, jcurr + tup[1] - 1)
            fout.write(str(icurr) + " " + str(jcurr) + " " + str(icurr + tup[0] - 1) + " " + str(jcurr + tup[1] - 1) + "\n")
            global slices
            slices += 1
            break

def run():
    icurr = 0
    jcurr = 0
    for icurr in range(0, rows):
        for jcurr in range(0, cols):
            if matrix[icurr][jcurr] != -1:
                findBiggestSlice(icurr, jcurr)

computeDivs()
buildMatrix()
run()
fout.write(str(slices) + "\n")
