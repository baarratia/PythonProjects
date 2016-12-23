a = True
lista = []
listac = []
while a == True:
    entrada = input().split(" ")
    if entrada == ["end"]:
        break
    elif len(entrada) == 2:
        int(entrada[1])
        lista.append(entrada[1])
        listac.append(entrada)
print(lista)
num = len(lista)
lista.sort()
for g in range(num):
    asd = lista[g]
    for n in listac:
        if n[1] == asd:
            print(n[0], asd)
            break