__author__ = 'Benja'


class Mapa:
    def __init__(self, ubicaciones):
        self.ubicaciones = ubicaciones
        self.nivel_zoom = 0
        self.mapa = []
        self.actualizar_mapa()

    def actualizar_mapa(self):
        self.mapa = []

        for i in self.ubicaciones:
            lis = []
            for j in i:
                if self.nivel_zoom == 0 or self.nivel_zoom == 1:
                    lis.append(j.continente)
                if self.nivel_zoom == 2:
                    lis.append(j.pais)
                if self.nivel_zoom == 3:
                    lis.append(j.ciudad)
                if self.nivel_zoom == 4:
                    lis.append(j.comuna)
                if self.nivel_zoom == 5:
                    lis.append(j.calle)
                if self.nivel_zoom == 6:
                    lis.append(j.tipo)
            self.mapa.append(lis)

    def cambiar_zoom(self, num):
        if num <= 6 and num >= 0:
            self.nivel_zoom = num
        self.actualizar_mapa()


class ubicacion:  # forma transversal cubica
    def __init__(self, x, y, continente, pais, ciudad, comuna, calle, tipo):
        self.continente = continente[x][y][1:-1]  # 1
        self.pais = pais[x][y][1:-1]  # 2
        self.ciudad = ciudad[x][y][1:-1]  # 3
        self.comuna = comuna[x][y][1:-1]  # 4
        self.calle = calle[x][y][1:-1]  # 5
        self.tipo = tipo[x][y][1:-1]  # 6
        tipo[x][y] = self
