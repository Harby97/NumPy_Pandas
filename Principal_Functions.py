import numpy as np

#Funciones matematicas https://numpy.org/doc/stable/reference/routines.math.html
#Funciones estadisticas https://numpy.org/doc/stable/reference/routines.statistics.html


Arr = np.random.randint(1,20,10)
print (Arr, '\n')

Matrix = Arr.reshape(2,5)
print (Matrix, '\n')

#Funcion MAX
print('maximo', Matrix.max())
print('maximo columnas', Matrix.max(0))
print('maximo filas', Matrix.max(1),'\n')

#Para encontrar el indice
print('indice del maximo', Matrix.argmax())
print('indice del maximo columnas',Matrix.argmax(0))
print('indice del maximo filas',Matrix.argmax(1), '\n')

#Funcion MIN
print('minimo', Matrix.min())
print('minimo columnas', Matrix.min(0))
print('minimo filas', Matrix.min(1),'\n')

#Para encontrar el indice
print('indice del minimo', Matrix.argmin())
print('indice del minimo columnas',Matrix.argmin(0))
print('indice del minimo filas',Matrix.argmin(1), '\n')

#Funcion peak to peak ptp
print('el valor entre picos es', Matrix.ptp())
print('el valor entre picos de las columnas es', Matrix.ptp(0))
print('el valor entre picos de las filas  es', Matrix.ptp(1), '\n')

#Funcion percentile 
Arr = np.sort(Arr)
print(Arr)
print('el valor percentile es', np.percentile(Matrix,50))
print('el valor percentile de las columnas es', np.percentile(Matrix,50,0))
print('el valor percentile de las filas  es', np.percentile(Matrix,50,1),'\n')

#Funcion mediana
print('la mediana es', np.median(Matrix))
print('la mediana de las columnas es', np.median(Matrix,0))
print('la mediana de las filas  es', np.median(Matrix,1),'\n')

#Desviacion estandar
print('la Desviacion estandar es', np.std(Matrix))
print('la Desviacion estandar de las columnas es', np.std(Matrix,0))
print('la Desviacion estandar de las filas  es', np.std(Matrix,1),'\n')

#Varianza
print('la Varianza es', np.var(Matrix))
print('la Varianza de las columnas es', np.var(Matrix,0))
print('la Varianza de las filas  es', np.var(Matrix,1),'\n')

#Media (promedio, la mitad del arreglo)
print('la Media es', np.mean(Matrix))
print('la Media de las columnas es', np.mean(Matrix,0))
print('la Media de las filas  es', np.mean(Matrix,1),'\n')


#FUNCION CONCATENATE
a = np.array([[1,2],[3,4]])
b = np.array([5,6])
print('la dimension de a es ', a.ndim)
print('la dimension de b es ', b.ndim) #como es diferente no se puede concatenar

#se redimensiona el array
b = np.expand_dims(b,axis=0)
print('la nueva dimension de b es ', b.ndim,'\n')
print(b,'\n')

#se concatena
c = np.concatenate((a,b),0)
print (c)

#Para hacerla en el otro eje se debe tener la transpuesta de b
d = np.concatenate((a,b.T),1)
print (d)