import pandas as pd

#Creacion de un objeto tipo Series
psg_players = pd.Series(['Navas','Mbappe','Neymar','Messi'],
                         index=[1,7,10,30])
print (psg_players,'\n')

#Sin index se inicializa automaticamente desde cero haste el ultimo
psg_players_2 = pd.Series(['Navas','Mbappe','Neymar','Messi'])
print (psg_players_2,'\n')

#Creando un diccionario y luego convirtiendolo a Series
Dictionary = {1:"Navas", 7:"Mbappe", 10:"Neymar", 30:"Messi"}
psg_players_3 = pd.Series(Dictionary)
print (psg_players_3,'\n')

#accediendo desde las llaves del diccionario
print(psg_players_3[1],'\n')

#Slicing 
psg_players_4 = psg_players[0:2]
print (psg_players_4,'\n')

psg = {'Jugador': ['Navas','Mbappe','Neymar','Messi'],
        'Altura': [182.0, 170.2, 189.2, 189.2],
        'Goles': [2,200,21,344] }

#inicializacion del datafrema, se puede acceder por la llave o por el indice
psg_dataframe = pd.DataFrame(psg,index=[1,7,10,30])
print (psg_dataframe, '\n')
#mostrar indices y columnas
print(psg_dataframe.columns)
print(psg_dataframe.index)
