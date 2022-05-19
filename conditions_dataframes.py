import pandas as pd
import numpy as np

df_books = pd.read_csv("./Resources/bestsellers-with-categories.csv", sep=',', header=0)
print (df_books.head(3))

higher_2018 = df_books['Year'] > 2018
print (df_books[higher_2018])

Just_Genre = df_books['Genre'] == 'Fiction'
print (df_books[Just_Genre])

print (df_books[Just_Genre & ~higher_2018])

print (df_books[df_books['Author'].str.contains('Palacio')])
