import numpy as np

#Creando una lista por medio de range
list1 = list(range(0,10))
print (list1,'\n')

#Creando arrays con arange
Arr1 = np.arange(0,10)
Arr2 = np.arange(0,10,2)
print (Arr1)
print (Arr2,'\n')

#Creacion de arrays de ceros
Arr3 = np.zeros(3)
Arr4 = np.zeros((3,3))
print (Arr3)
print (Arr4,'\n')

#Creacion de arrays de unos
Arr5 = np.ones(3)
Arr6 = np.ones((3,3))
print (Arr5)
print (Arr6,'\n')

#Creacion de arrays de matriz identidad
Arr7 = np.eye(7)
print (Arr7,'\n')

#Generacion de una distribucion normalizada (inicio,final,# datos)
Arr8 = np.linspace(0,10,10 )
print (Arr8,'\n')


#Generacion de numeros aleatorios
Arr9 = np.random.rand(5)
Arr10 = np.random.rand(5,5)
print (Arr9)
print (Arr10,'\n')


#Generacion de numeros aleatorios enteros (rango inicial,rango final,(# filas, #colum))
Arr11 = np.random.randint(1,100)
Arr12 = np.random.randint(1,100,(4))
Arr13 = np.random.randint(1,100,(5,6))
print (Arr11)
print (Arr12)
print (Arr13,'\n')

