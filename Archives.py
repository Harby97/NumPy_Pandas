import pandas as pd

#Guardo el data frame, con separador de ',' y que los headers estan en la fila 0
df_books = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0)
print (df_books)


#Guardo el data frame, le puedo cambiar los nombres de los encabezados
df_books_2 = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0,
names=['Nombre', 'Autor', 'Critica', 'Reviews', 'Price', 'Year', 'Genre'])
print (df_books_2)


#Manejo de archivos JSON, son datos no estructurados llave valor
#Para pasar de un archivo JSON que es no estructurado a un data frame que si es estructurado
df_HP_Characters = pd.read_json('./Resources/HPCharactersDataRaw.json')
print (df_HP_Characters)

#Para pasar de un archivo JSON a formato raw
df_HP_Characters_2 = pd.read_json('./Resources/HPCharactersDataRaw.json', typ='Series' )
print (df_HP_Characters_2.info())


#PRUEBAS DE FILTRADO CON LOC E ILOC


