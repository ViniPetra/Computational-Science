import numpy as np

print(np.average(np.loadtxt("altura.txt")[np.where((np.loadtxt("anos.txt") >= 1998) & (np.loadtxt("anos.txt") <= 2005))]))
