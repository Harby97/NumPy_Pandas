import pandas as pd
import numpy as np

df_books = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0)
print (df_books.head(3))

#--------Drop para eliminar datos------------#
print(df_books.drop('Genre',axis=1)) #Con drop en esta sintaxis solo borra de esta salida y no de la fuente
print (df_books) #Se evidencia que no se borra de la fuente

#Drop para borrar de la fuente
df_books.drop('Genre',axis=1,inplace=True)
print (df_books) #Se evidencia que se borro de la fuente

#otra opcion
df_books = df_books.drop('Year',axis=1)
print (df_books) #Se evidencia que se borro de la fuente

#otra opcion
del df_books['Reviews']
print (df_books.head(3),'\n') #Se evidencia que se borro de la fuente

#Borrar filas
print(df_books.drop(0,axis=0).head(3))
print(df_books.drop([0,1,2,3],axis=0).head(3))
print(df_books.drop(range(0,12),axis=0).head(3))

#--------Agregar datos------------#
df_books['nueva columna'] = np.nan #Se agrega una nueva columna llena de datos no numericos
print (df_books.head(3),'\n') 

data = np.arange(0,df_books.shape[0])
print(data)

df_books['Rango'] = data
print (df_books,'\n')

#Agregar filas
print(df_books.append(df_books))
