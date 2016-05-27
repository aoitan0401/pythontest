#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
list=[]
f = open('test.txt')
line = f.readline()
while line:
	print line
	list.append([line])
	line = f.readline()
print list
plt.plot(list)
plt.show()
f.close()
