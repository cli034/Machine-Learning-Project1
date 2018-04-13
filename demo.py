import numpy as np
import matplotlib.pyplot as plt

# load data set
a = np.loadtxt('iris.data.txt', delimiter=',', usecols=(0, 1, 2, 3))
# first 50 items in the first column
b = a[0:50, 0]
print b
print b.size
min_b = min(b)
max_b = max(b)
bins = 5 
binRange = float((max_b - min_b) / bins) #this should be the interval, the width of the thing
Y = np.zeros(bins) #{0,0,0,0,0}

r1 = min_b
r2 = min_b + binRange
X = []
for i in range(bins):
    c = b[b > r1] # an array that stores anything greater than min in b
    c = c[c <= r2] # an array that stores anything less than or equal to max in c
    Y[i] = c.size
    string = str(r1) + "-" + str(r2)
    X.append(string)
    r1 = r2
    r2 = r2 + binRange

# {0,1,2,3,4}
inds = np.arange(bins)
width = 0.35
p1 = plt.bar(inds, Y, width)
print X
plt.xticks(inds, X)
plt.show()


