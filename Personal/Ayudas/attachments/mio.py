a = True
lista = []
listac = []
while a == True:
    entrada = input().split(" ")
    if entrada == ["end"]:
        break
    else:
        nombre = entrada[0]
        numero = int(entrada[1])
        listac.append([numero, nombre])
listac.sort()
for i in listac:
    nombre = i[1]
    numero = i[0]
    print(nombre + ' ' + str(numero) )