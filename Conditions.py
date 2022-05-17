import numpy as np

#Creacion de array con una distribucion normalizada
Arr = np.linspace(1,10,10,dtype='int8')
print (Arr)

Condition_indexes = (Arr > 5) & (Arr < 9)
print (Condition_indexes)

#filtrado de solo los que cumplen la condicion
Arr[(Condition_indexes)]=99
print (Arr)

