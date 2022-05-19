import pandas as pd
import numpy as np

df_books = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0)
print (df_books.head(3),'\n')

print (df_books.info(),'\n') #informacion de tipo de datos del dataframe

print (df_books.describe(),'\n') # Muestra la distribucion de los datos

print (df_books.tail(10),'\n') # Trae los n datos del final del dataframe

print (df_books.memory_usage(deep=True),'\n') #Muestra la cantidad de memoria que consumen los datos

print (df_books['Author'].value_counts(),'\n') #Muestra el conteo de veces que sale algo

# PODER VER LOS REPETIDOS
df_books = df_books.append(df_books.iloc[0]) #Agregamos un valor duplicado
print (df_books.drop_duplicates(),'\n') #Eliminar los datos que estan duplicados
print (df_books.drop_duplicates(keep='last')) #Elimina el primer o primeros duplicados

# Organizar lo valores
print (df_books.sort_values('Year'))

print (df_books.sort_values('Year',ascending=False))

print (df_books.groupby('Genre').size())

print (df_books['User Rating'].skew())
