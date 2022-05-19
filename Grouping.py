import pandas as pd
import numpy as np

df_books = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0)
print (df_books.head(3),'\n')


print ('count \n', df_books.groupby('Author').count(),'\n')

print ('mean \n',df_books.groupby('Author').mean(),'\n')

print ('min \n',df_books.groupby('Author').min(),'\n')

print ('max \n',df_books.groupby('Author').max(),'\n')

print ('sum \n',df_books.groupby('Author').sum(),'\n')


#Funciones de agregacion

print ('max y min \n', df_books.groupby('Author').agg(['max','min']).reset_index(),'\n')

print ('max y min \n', df_books.groupby('Author').agg({'Reviews': ['min','max'],'User Rating': 'sum'}),'\n')

print ('count \n', df_books.groupby(['Author','Year']).count(),'\n')

print (df_books.groupby('Author').agg({'Year':lambda x: [i-2000 for i in x], 'Reviews':lambda x: sum([i**2 for i in x])}))