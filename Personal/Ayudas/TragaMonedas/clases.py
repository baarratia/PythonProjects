__author__ = 'Benja'

class Perro:
    def __init__(self, color, nombre, patas):
        self.color = color
        self.nombre = nombre
        self.patas = patas
        self.hp = 20

    def correr(self, x):
        print('{0} corre {1} minutos'.format(self.nombre, x))
        self.hp -= x*3
        if self.hp <= 0:
            print('{} esta muy cansado'.format(self.nombre))


fido = Perro('negro', 'fido', 4)
fido.correr(5)
fido.correr(3)