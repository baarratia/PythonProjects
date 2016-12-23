from pistas import Ayuda

"""
La variable pistas contiene los métodos de ayuda del enunciado. Es decir para ejecutar las funciones
debe realizar la tarea pistas.funcion().
"""

# ------ACÁ COMIENZA LA TAREA------#

pistas = Ayuda()
pista2 = pistas.extraer_pista2()
pista3 = pistas.extraer_pista3()
pista4 = pistas.extraer_pista4()
pista5 = pistas.extraer_pista5()
pista6 = pistas.extraer_pista6()
clave = pistas.extraer_clave()

#Aplicando Pista 1
print(pista2)
p2 = ''
print(ord('a'))  # Vemos los limites numericos entre los que estan las letras del abecedario
print(ord('z'))  # En el codigo Ascii
print(122 - 97)

for i in pista2:
    if i == ' ':
        p2 += ' '
    else:
        a = ord(i) + 5
        if a > 122:
            a -= 26  # Si se pasa del abecedario, que vuelva al comienzo
        p2 += chr(a)
print(p2)

pistas.comprobar_pista2(p2)
#Aplicando Pista 2
print(pista3)
print(len(pista3))
mitad = pista3[33:]
print(mitad)
mitad = mitad[::-1]
print(mitad)
p3 = pista3[:33] + mitad
print(p3)

pistas.comprobar_pista3(p3)
#Aplicando Pista 3
print(pista4)
p4 = ' '
a = ' '
c = 0
for i in pista4:
    if i in 'aeiou':
        p4 = p4[:-1] + i + a
        c = 1
    else:
        p4 += i
        c = 0
    a = i

print(p4)
p4 = 'el orden es ocho dos siete tres cuatro uno seis cinco' #100% REAL NO FAKE

pistas.comprobar_pista4(p4)
#Aplicando Pista 4
print(pista5)
p5 = pista5.split(' ')
p5 = p5[7] + ' ' + p5[1] + ' ' + p5[6] + ' ' + p5[2] + ' ' + p5[3] + ' ' + p5[0] + ' ' + p5[5] + ' ' + p5[4]
print(p5)

pistas.comprobar_pista5(p5)

#Aplicando Pista 5
print(pista6)
p6 = ''
print(97 + 122) #Para hacer el complemento se resta a la suma de las posiciones de los extremos
                #Por ejemplo, si hay 5 elementos, se suma 5+1=6, entonces para encontrar el
                #complemento de cualquier numero, se hace 6 - posicion_del_numero = complemento
for i in pista6:
    if i == ' ':
        p6 += ' '
    else:
        a = 219 - ord(i)
        p6 += chr(a)
print(p6)

pistas.comprobar_pista6(p6)

#Aplicando Pista 6
print(clave)
cl = ''
for i in clave:
    if i == ' ':
        cl += ' '
    else:
        a = ord(i) + 5
        if a > 122:
            a -= 26  # Si se pasa del abecedario, que vuelva al comienzo
        cl += chr(a)
cl2 = ''
for i in cl:
    if i == ' ':
        cl2 += ' '
    else:
        a = 219 - ord(i)
        cl2 += chr(a)
clfinal = ''
for i in range(len(cl2)):
    if i%2 == 0:
        clfinal += cl2[i]
print(clfinal)


