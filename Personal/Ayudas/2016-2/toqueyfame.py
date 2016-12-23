import random
n = int(input('Largo de los numeros: '))
c = ""
while len(c) < n:
    a = str(random.randint(1,9))
    if a not in c:
        c += a
print(c)
e = 0
while e == 0:
    b = input('Ingrese su numero: ')
    if len(b) == n:
        e = 1
    else:
        print('Largo incorrecto!')
print(b)
cnt = 0
for i in b:
    if i in c:
        cnt += 1
print(cnt)
cnt2 = 0
for i in range(n):
    if c[i] == b[i]:
        cnt2 += 1
print(cnt2)



