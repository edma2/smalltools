# regression.py - calculates linear regression of graphs
# author: Eugene Ma (edma2)
import sys
import pylab
import numpy as np

# fetch input 
raw = sys.stdin.readline()
raw = raw.strip()

# parse into coordinate pairs
pairs = raw.split(" ")

# count the number of points
n = len(pairs)

# make list of x's and y's
x = np.array([float(pair.split(",")[0]) for pair in pairs])
y = np.array([float(pair.split(",")[1]) for pair in pairs])
xx = np.array([z*z for z in x])
xy = np.array([[z for z in x],[z for z in y]])
xy = np.prod(xy, axis = 0)

# find sums
xsum = x.sum()
ysum = y.sum()
xxsum = xx.sum()
xysum = xy.sum()

# calculate line 
slope = (n*xysum - xsum*ysum)/(n*xxsum - xsum*xsum)
intercept = (ysum - slope*xsum)/n

# output
print "y = %fx + %f" % (slope, intercept)
t = np.arange(50)
line = slope * t + intercept
pylab.plot(line)
pylab.plot(x, y, 's')
pylab.show()
