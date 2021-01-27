#in Python 3 regular division is actually integer division unless you include the from __future__ import division thing
from __future__ import division
from numpy import *
from math import *
import Schemes.py

# Aici am scris formula aceea care trebuie aplicata recurent de jos in sus. x e spinul 'copilului' si y e spinul 'parintelui'

def coeff(x,y):
    a=abs(x)
    b=abs(abs(y)-abs(x))
    c=abs(y)
    return (c*(c+1)+a*(a+1)-b*(b+1))/(2*c*(c+1)) 

# Functie care aplica formula recursiv de jos in sus. Un coupling_scheme arata asa:  [[1], [1,2], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7]]

def calc_coeff(coupling_scheme):
    k=1
    for i in range(len(coupling_scheme)-1):
        k=k*coeff(sum(coupling_scheme[i]),sum(coupling_scheme[i+1]))
    return k

# Functie care calculeaza suma tuturor numerelor dintr-un list

def sum(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    return sum

# Functie care schimba numerele dintr-un coupling scheme in spinii corespunzatori numerelor acelora. S va fi o lista de forma [2, 2, 2, 2, -2.5, -2.5, -2.5]

def replace(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] == 1:
                list[i][j] = S[0]
            elif list[i][j] == 2:
                list[i][j] = S[1]
            elif list[i][j] == 3:
                list[i][j] = S[2]
            elif list[i][j] == 4:
                list[i][j] = S[3]
            elif list[i][j] == 5:
                list[i][j] = S[4]
            elif list[i][j] == 6:
                list[i][j] = S[5]
            elif list[i][j] == 7:
                list[i][j] = S[6]
    return list
    
# Functie care verifica daca numerele dintr-o lista sunt ordonate crescator sau nu. Stiu ca se poate face cu booleans dar nu mai stiu sintaxa asa ca whatever

def is_ordered(l):
    z=1
    for i in range(1,len(l)):
        if l[i]<=l[i-1]:
            z = 0
    return z

# Functie care transforma o lista intr-un string

def st(l):
    stri=''
    for i in range(len(l)):
        stri = stri+str(l[i])
    return stri
    
# Functie care ia un coupling scheme de genul celor care le vei genera tu :D si le prelucreaza ca sa arata asa: [[1], [1, 2], [1, 2 ,3] etc ect].  l va fi de exemplu [1] si m coupling scheme-ul.

def gen(l,m):
    scheme=[l]
    for i in range(len(m)-1,-1,-1):
        if st(l) in st(m[i][0]) or st(l) in st(m[i][1]):
            list_A= l + m[i][1]
            list_B = m[i][0] +  l
            if is_ordered(list_A) == 1:
                l = list_A
            elif is_ordered(list_B) == 1:
                l = list_B
            scheme.append(l)
    return scheme

def calc_ph(l,s,k):
    sum=0
    for i in range(len(l)):
        sum=sum+k[l[i]-1]/abs(s[l[i]-1])
    return 1/len(l)*sum*1/2



# Actual body of code

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


	








