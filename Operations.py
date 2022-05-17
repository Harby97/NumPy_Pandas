import numpy as np 

user_list = [1,2]

print(user_list * 2) #concatena la lista

user_array = np.arange(0,10)
print (user_array)

user_array_copy = user_array.copy()

print (user_array_copy *4)
print (user_array_copy + user_array_copy)

matriz = user_array_copy.reshape(2,5)
matriz2 = matriz.copy()
print(matriz,'\n')
print (matriz + matriz2)

#Se puede hacer el producto punto entre matrices
print(np.matmul(matriz,matriz2.T))
print(matriz @ matriz2.T)