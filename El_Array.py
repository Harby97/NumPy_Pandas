import numpy as np

list = [1,2,3,4,5,6,7,8,9]
print (list)

#lista ya te tipo array
arr = np.array(list)
print (arr)
print(type(arr))

#lista ya te tipo array de dos dimensiones una matriz
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = np.array(matrix)
print (matrix)
print(type(matrix))

#manipulacion de array y matrix por medio de sus indices
print('manipulacion de array y matrix por medio de sus indices')
print(arr[0] + arr[5])
print(matrix[0,0] + matrix[2,2])

#slicing para tomar valores de unas posiciones especifias de mi array
print('slicing array')
print('De 0 a 4 ' + str(arr[0:4]))
print('De 0 a 4 ' + str(arr[:4]))
print('De 2 a 4 ' + str(arr[2:4]))
print('De 2 a fin ' + str(arr[2:]))
print('De 0 a fin de 3 en 3 ' + str(arr[::3]))
print('De fin-3  a fin' + str(arr[-3:]))
print('De fin a fin-3 ' + str(arr[::-3]))

print('')
print('slicing matrix')
print('fila de la 1 al fin y columna de la 0 a a la 2')
print(matrix[1:,0:2])