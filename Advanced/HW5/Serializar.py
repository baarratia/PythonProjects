__author__ = 'Benja'
import pickle
import os

def SaveData(Usuario, Tiempo, Puntos):
    datos = (Usuario, Tiempo, Puntos)
    if len(os.listdir("Data")) > 0:
        for file_ in os.listdir("Data"):
            if file_.endswith(".pocmon"):
                with open("Data/Dat.pocmon", 'rb') as file:
                    lista = pickle.load(file)
                lista.append(datos)
                with open("Data/Dat.pocmon", 'wb') as file:
                    pickle.dump(lista, file)
                    return lista
    else:
        with open("Data/Dat.pocmon", 'wb') as file:
            pickle.dump([datos], file)
            return [datos]

def EncontrarRecord():
    for file_ in os.listdir("Data"):
        if file_.endswith(".pocmon"):
            with open("Data/Dat.pocmon", 'rb') as file:
                lista = pickle.load(file)
                lista = sorted(lista, key=lambda x: x[1])
                return lista[0][1]
        else:
            return 0
