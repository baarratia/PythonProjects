class Pokemon:
    def __init__(self, nombre, tipo, hp, at, df, vel):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.at = at
        self.df = df
        self.vel = vel

    def calcular_danio(self, otropokemon):  # Calcula el danio que debe realizar
        if self.tipo is 'Planta':
            if otropokemon.tipo is 'Agua':
                self.danio = 2 * self.at
            elif otropokemon.tipo is 'Fuego':
                self.danio = 0.5 * self.at
        if self.tipo is 'Fuego':
            if otropokemon.tipo is 'Planta':
                self.danio = 2 * self.at
            elif otropokemon.tipo is 'Agua':
                self.danio = 0.5 * self.at
        if self.tipo is 'Agua':
            if otropokemon.tipo is 'Fuego':
                self.danio = 2 * self.at
            elif otropokemon.tipo is 'Planta':
                self.danio = 0.5 * self.at

    def atacar(self, otropokemon):  # le quita vida al otro pokemon
        x = max(self.danio//2, self.danio - otropokemon.df)
        otropokemon.hp -= x

    def vivo(self):  # Editar, si vida > 0, return True, else return False
        if self.hp > 0:
            return True
        else:
            return False


p1 = input().split(' ')
p2 = input().split(' ')
nombre1 = p1[0]
tipo1 = p1[1]
hp1 = int(p1[2])
at1 = int(p1[3])
df1 = int(p1[4])
vel1 = int(p1[5])
nombre2 = p2[0]
tipo2 = p2[1]
hp2 = int(p2[2])
at2 = int(p2[3])
df2 = int(p2[4])
vel2 = int(p2[5])
pok1 = Pokemon(nombre1, tipo1, hp1, at1, df1, vel1)  # Pasarle paramentros p1
pok2 = Pokemon(nombre2, tipo2, hp2, at2, df2, vel2) # Pasarle parametros p2
while pok1.vivo() and pok2.vivo():
    if pok1.vel > pok2.vel:
        pok1.calcular_danio(pok2)
        pok1.atacar(pok2)
        pok2.vivo()
        pok2.calcular_danio(pok1)
        pok2.atacar(pok1)
        pok1.vivo()
    else:
        pok2.calcular_danio(pok1)
        pok2.atacar(pok1)
        pok1.vivo()
        pok1.calcular_danio(pok2)
        pok1.atacar(pok2)
        pok2.vivo()
if pok1.vivo():
    print("Gana "+pok1.nombre)
else:
    print("Gana "+pok2.nombre)

