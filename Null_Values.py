import pandas as pd
import numpy as np

dict_incomplete= {'Col1': [1,2,3,np.nan],
    'Col2': [4,np.nan,6,7],
    'Col3': ['a','b','c',None]}

df_incomplete = pd.DataFrame(dict_incomplete)

print (df_incomplete)

print (df_incomplete.isnull()*1,'\n') #Is null para saber que esta vacio

print (df_incomplete.fillna('Missing'),'\n') #Remplaza los valores por una palabra

print (df_incomplete.fillna(df_incomplete.mean()),'\n') #Remplaza los valores por la media

print (df_incomplete.fillna(df_incomplete.mean()),'\n') #Remplaza los valores por la media

print (df_incomplete.interpolate(),'\n') #Remplaza los valores con interpolacion viendo maximos y minimos

print (df_incomplete.dropna(),'\n') #Borrar las filas que tenga algun faltante

