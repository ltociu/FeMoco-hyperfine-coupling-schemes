from __future__ import division
from numpy import *
from math import *
import Schemes.py

S=[2, 2, 2, 2, -2.5, -2.5, -2.5]

atoms=[[1], [2], [3], [4], [5], [6], [7]]

K=[]
for i in range(len(schemes)):
	k=[]
	for j in range(len(atoms)):
		k.append(calc_coeff(replace(gen(atoms[j], schemes[i]))))
	K.append(k)

for i in range(len(K)):
	l=[2, 6]
	if 15 <= calc_pH(l, S, K[i]) <= 35:
		print(calc_pH(l, S, K[i]), scheme[i])


	








