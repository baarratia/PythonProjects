# -*- coding: utf-8 -*-
import hashlib
import pickle
import os
import re

def getDigest(password, salt=None):
    if not salt:
        salt = os.urandom(32)
    digest = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    return salt, digest


def isPassword(password, salt, digest):
    return getDigest(password, salt)[1] == digest


def Comprobar_User(email):
    if (
    re.search(r'[\w.-]+(@uc.cl)|(@puc.cl)', email)):  # Comprueba que el mail ingresado posea una linea de caracteres
        return True  # de cualquier tipo, seguido de @uc.cl o @puc.cl
    else:
        return False


def Comprobar_Contraseña(Password):
    if (re.match(r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?=.*[A-Z])(?=.*[a-z]).*$', Password)):  # Comprueba que tenga minimo
        return True  # 8 caracteres, alguna Mayuscula
    else:  # Numeros y letras minusculas
        return False


def Nuevo_Usuario(Nombre, Password):
    if Comprobar_User(Nombre):
        salt, digest = getDigest(Password)
        if len(os.listdir("Data")) > 0:
            for file_ in os.listdir("Data"):
                if file_.endswith(".Ichat"):
                    with open("Data/Dat.Ichat", 'rb') as file:
                        dic = pickle.load(file)
                    if Nombre in dic:
                        return False, 'Este nombre de usuario ya existe!'
                    else:
                        dic[Nombre] = (salt, digest)
                        with open("Data/Dat.Ichat", 'wb') as file:
                            pickle.dump(dic, file)
                            return True, 'Usuario Creado correctamente'
        else:
            with open("Data/Dat.Ichat", 'wb') as file:
                dic = {Nombre: (salt, digest)}
                pickle.dump(dic, file)
                return True, 'Usuario Creado correctamente'
    else:
        return False, 'Nombre de usuario no válido'


def Validar_Datos(Nombre, Password):
    if Comprobar_User(Nombre):
        if len(os.listdir("Data")) > 0:
            for file_ in os.listdir("Data"):
                if file_.endswith(".Ichat"):
                    with open("Data/Dat.Ichat", 'rb') as file:
                        dic = pickle.load(file)
                    if Nombre in dic:
                        salt = dic[Nombre][0]
                        digest = dic[Nombre][1]
                        if isPassword(Password, salt, digest) is True:
                            return True, 'Usuario y contraseña validos!!!'
                        else:
                            return False, 'Contraseña incorrecta, intente nuevamente'
                    else:
                        return False, 'Nombre de usuario no valido, intente nuevamente'
    else:
        return False, 'Nombre de usuario no válido'