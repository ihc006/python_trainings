#106 isimsiz fonsiyonlar

def old_sum(a,b):
    return a+b

old_sum(4,5)

new_sum = lambda a,b: a+b

new_sum(4,5)

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]

sirasiz_liste

sorted(sirasiz_liste,key=lambda  x: x[1])


# 107 Vektorel OPs

a=[1,2,3,4,5]
b=[2,3,4,5,6]

ab= []

for i in range(0, len(a)):
    print(i)


for i in range(0, len(a)):
    ab.append(a[i]*b[i])


ab

# fp olarak yapma // kutuphaneleri kullanma   vektorel bir oprasyon
#--------
import  numpy as np

a1=np.array([1,2,3,4,5])
b1=np.array([2,3,4,5,6])

a1*b1
#--------

#108 map & filter & reduce

liste= [1,2,3,4,5,6]

for i in liste:
    print(i+10)

# farkli bir yolla // eklemeyi liste icinde yapmak

list(map(lambda x: x+10,liste))

list(map(lambda x: x*10,liste))
liste

# filter

liste2= [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x%2 ==0 , liste2))

# reduce  =  indirgeme

from functools import reduce

liste3=[1,2,3,4,5]

reduce(lambda a,b: a+b,liste3)
