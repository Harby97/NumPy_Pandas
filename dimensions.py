import numpy as np

scalar = np.array(42)
print(scalar)
print(scalar.ndim) #numero de dimensiones


vector = np.array([1,2,3])
print(vector)
print(vector.ndim) #numero de dimensiones

matrix = np.array([[1,2,3],[1,2,3]])
print(matrix)
print(matrix.ndim) #numero de dimensiones

tensor3d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(tensor3d)
print(tensor3d.ndim) #numero de dimensiones


print('agregar o eliminar dimensiones')
vector2 = np.array([1,2,3],ndmin=10)
print(vector2)
print(vector2.ndim) #numero de dimensiones

#para expandir un dimension en sus ejes
expand = np.expand_dims(np.array([1,2,3]),axis=0) #axis 0 es filas y 1 es columnas
print(expand)
print(expand.ndim)

#para eliminar las dimensiones que no estoy usando
expand_2 = np.squeeze(vector2)
print(expand_2, expand_2.ndim)
print(expand.shape)