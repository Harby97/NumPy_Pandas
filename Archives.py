import pandas as pd

#Guardo el data frame, con separador de ',' y que los headers estan en la fila 0
df_books = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0)
print (df_books)


#Guardo el data frame, con separador de ',' y que los headers estan en la fila 0
df_books_2 = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0,
names=['Nombre', 'Autor', 'Critica', 'Reviews', 'Price', 'Year', 'Genre'])
print (df_books_2)