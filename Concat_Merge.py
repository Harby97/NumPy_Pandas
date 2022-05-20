import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
 'B':['B0','B1','B2','B3'],
 'C':['C0','C1','C2','C3'],
 'D':['D0','D1','D2','D3'],})

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
 'B':['B4','B5','B6','B7'],
 'C':['C4','C5','C6','C7'],
 'D':['D4','D5','D6','D7'],})

#-----CONCAT-----#
#Concatenado por el eje cero por defecto]
print ('Concatenado por el eje cero','\n')
print (pd.concat([df1,df2],ignore_index=True))

#Concatenado por el eje 1, columnas
print ('Concatenado por el eje uno','\n')
print (pd.concat([df1,df2],axis=1))

#------MERGE------#
izq = pd.DataFrame({'key':['k0','k1','k2','k3'],
 'A':['A0','A1','A2','A3'],
 'B':['B0','B1','B2','B3']})

der = pd.DataFrame({'key':['k0','k1','k2','k3'],
 'C':['C0','C1','C2','C3'],
 'D':['D0','D1','D2','D3']})

print ('merge de izquierda a derecha con key','\n')
print (izq.merge(der, on='key'))



izq = pd.DataFrame({'key':['k0','k1','k2','k3'],
 'A':['A0','A1','A2','A3'],
 'B':['B0','B1','B2','B3']})

der = pd.DataFrame({'key_2':['k0','k1','k2','k3'],
 'C':['C0','C1','C2','C3'],
 'D':['D0','D1','D2','D3']})

print ('merge de izquierda a derecha con key y key_2','\n')
print (izq.merge(der, left_on='key', right_on='key_2'))



izq = pd.DataFrame({'key':['k0','k1','k2','k3'],
 'A':['A0','A1','A2','A3'],
 'B':['B0','B1','B2','B3']})

der = pd.DataFrame({'key_2':['k0','k1','k2',np.nan],
 'C':['C0','C1','C2','C3'],
 'D':['D0','D1','D2','D3']})

print ('merge de izquierda a derecha con prioridad de right','\n')
print (izq.merge(der, left_on='key', right_on='key_2', how='right'))

#-----------JOIN----------#

izq = pd.DataFrame({'A':['A0','A1','A2'],
 'B':['B0','B1','B2']},
 index=['k0','k1','k2'])

der = pd.DataFrame({'C':['C0','C1','C2'],
 'D':['D0','D1','D2']},
 index=['k0','k2','k3'])

print (izq.join(der,how='outer'))


