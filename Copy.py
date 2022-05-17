import numpy as np

Arr = np.arange(0,11)
print (Arr)

slice_Arr = Arr[0:6]
print (slice_Arr)
"""
#Aqui solo queria cambiar el slice_arr pero como esta referenciado de un objeto padre 
#lo va a modificar y cambiar Arr, por eso se necesita copy
slice_Arr[:] = 0
print (slice_Arr)
print (Arr)
"""
Arr_copy = Arr.copy()
Arr_copy[:] = 100
print (Arr_copy)
print (Arr)
