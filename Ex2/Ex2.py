import numpy as np

alturas = np.loadtxt("altura.txt")
anos = np.loadtxt("anos.txt")

avg = np.average(alturas[np.where((anos >= 1998) & (anos <= 2005))])

print(avg)
