import numpy as np

Arr = np.random.randint(1,50,(3,2))
#print (Arr)
#print (Arr.shape,'\n')

#Reorganizarlo de 1 fila y 6 columnas
Arr2 = Arr.reshape(1,6)
#print (Arr2,'\n')

#Reorganizarlo de 2 fila y 3 columnas
Arr3 = Arr.reshape(2,3)
#print (Arr3,'\n')

#Reorganizarlo de 1 fila y 6 columnas diferente sintaxys
Arr4 = np.reshape(Arr,(1,6))
#print (Arr4,'\n')

#Reorganizarlo como lo hace C (Organiza por filas)
Arr5 = np.reshape(Arr,(2,3),'C')
#print (Arr5,'\n')

#Reorganizarlo como lo hace Fortran (Organiza por columnas)
Arr5 = np.reshape(Arr,(2,3),'F')
#print (Arr5,'\n')

#Reorganizarlo como mejor este optimizado el sistema (para optimizar tiempo)
Arr5 = np.reshape(Arr,(2,3),'A')
#print (Arr5,'\n')

Arr6 = np.random.randint(1,10,(5,4,10,5))
Arr7 = np.reshape(Arr6,(2,10,5,10),'C')
print (Arr6,'\n')
print (Arr6.shape,'\n')
print (Arr7)
print (Arr7.shape,'\n')
