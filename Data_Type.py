import numpy as np

#TIPOS DE DATOS https://numpy.org/doc/stable/user/basics.types.html


list = [0,1,2,3,4,5,6,7,8,9]
print (list)

#lista ya te tipo array
arr = np.array(list)
print (arr)
print(arr.dtype) #int32

#creacion de array tipo float64
arr2 = np.array(list, dtype='float64')
print (arr2)
print(arr2.dtype) #float64

#Cambiar un array de tipo sin tener que crearlo
arr = arr.astype(np.string_)
print(arr)
print(arr.dtype)
