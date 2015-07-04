__author__ = 'Benja'


class Tarea:
    def __init__(self, Map):
        self.Mapa = Map
        self.x1 = 84
        self.y1 = 84
        self.x2 = 122  # tamano inicial= 38 x 38,al centro de todo, nivel de zoom = 0
        self.y2 = 122
        self.lista = self.Mapa.mapa[self.y1:self.y2]
        for i in range(len(self.lista)):
            self.lista[i] = self.lista[i][self.x1:self.x2]

    def actualizar(self):
        tam_grilla = self.x2 - self.x1
        if self.y1 < 0:
            y = -self.y1
            self.y1 = 0
            self.lista = []
            for i in range(y):
                l = []
                for j in range(tam_grilla):
                    l.append('vacio')
                self.lista.append(l)
            self.lista.extend(self.Mapa.mapa[self.y1:self.y2])

        elif self.y2 > len(self.Mapa.mapa):
            y = self.y2 - len(self.Mapa.mapa) - 1
            self.y2 = len(self.Mapa.mapa) - 1
            self.lista = self.Mapa.mapa[self.y1:self.y2]
            for i in range(y):
                l = []
                for j in range(tam_grilla):
                    l.append('vacio')
                self.lista.append(l)

        else:
            self.lista = self.Mapa.mapa[self.y1:self.y2]

        if self.x1 < 0:
            x = -self.x1
            self.x1 = 0
            lis = []
            for i in range(x):
                lis.append('vacio')
            for i in range(len(self.lista)):
                self.lista[i] = (self.lista[i][self.x1:self.x2]).insert(0, lis)

        elif self.x2 > len(self.Mapa.mapa[0]):
            x = self.x2 - len(self.Mapa.mapa[0]) - 1
            self.x2 = len(self.Mapa.mapa[0]) - 1
            lis = []
            for i in range(x):
                lis.append('vacio')
            for i in range(len(self.lista)):
                self.lista[i] = self.lista[i][self.x1:self.x2].extend(lis)

        else:
            for i in range(len(self.lista)):
                self.lista[i] = self.lista[i][self.x1:self.x2]


    def func_zoom(self, num):
        zoom_inicial = self.Mapa.nivel_zoom
        x = (num // 16) + 1
        if x > 6:
            x = 6
        if num == 0:
            x = 0
        self.Mapa.cambiar_zoom(x)
        dif = x - zoom_inicial
        self.x1 += 3 * dif  # cumple con las restricciones de tamaño 38 - 6 * (x) y lo centra
        self.y1 += 3 * dif
        self.x2 -= 3 * dif
        self.y2 -= 3 * dif
        self.actualizar()
        return self.lista


    def func_move(self, tupla):
        if tupla[0] == 0:
            self.x1 -= tupla[0]
            self.x2 -= tupla[0]
            self.y1 -= tupla[1]
            self.y2 -= tupla[1]
        else:
            self.x1 += tupla[0]
            self.x2 += tupla[0]
            self.y1 += tupla[1]
            self.y2 += tupla[1]

        self.actualizar()
        return self.lista

    # Consultas globales
    def consulta1(self, tupla):
        ubi = ((tupla[0][0]).strip()).title()
        region = ((tupla[1][0]).strip()).lower()
        dic = {}
        for i in self.Mapa.ubicaciones:
            for j in i:
                if region == 'continente':
                    x = j.continente
                if region == 'pais':
                    x = j.pais
                if region == 'ciudad':
                    x = j.ciudad
                if region == 'comuna':
                    x = j.comuna
                if region == 'calle':
                    x = j.calle
                if len(dic) != 0:
                    if dic.get(x, 'no') == 'no':
                        if j.tipo == ubi:
                            dic[x] = 1
                    else:
                        if j.tipo == ubi:
                            dic[x] += 1
                else:
                    if j.tipo == ubi:
                        dic[x] = 1

        return [(k, v) for k, v in dic.items()]

    def consulta2(self, tupla):
        lista = tupla[0]
        region = ((tupla[1][0]).strip()).lower()
        dic = {}
        for i in self.Mapa.ubicaciones:
            for j in i:
                if region == 'continente':
                    x = j.continente
                if region == 'pais':
                    x = j.pais
                if region == 'ciudad':
                    x = j.ciudad
                if region == 'comuna':
                    x = j.comuna
                if region == 'calle':
                    x = j.calle

                if len(dic) != 0:
                    if dic.get(x, 'no') == 'no':
                        c = 0
                        for k in lista:
                            if j.tipo == (k.strip()).title():
                                c += 1
                        if c == 0:
                            dic[x] = ''

                    else:
                        c = 0
                        for k in lista:
                            if j.tipo == (k.strip()).title():
                                c += 1
                        if c > 0:
                            if dic[x] == 'borrar':
                                pass
                            else:
                                dic[x] = 'borrar'
                else:
                    c = 0
                    for k in lista:
                        if j.tipo == (k.strip()).title():
                            c += 1
                        if c == 0:
                            dic[x] = ''
        w = []
        for i in dic:
            if dic[i] == 'borrar':
                w.append(i)

        for i in w:
            del (dic[i])
        if len(dic) == 0:
            return '----'
        else:
            return list(dic)

    def consulta3(self, tupla, evitar=None):
        x1 = int(tupla[0][0])
        x2 = int(tupla[0][1])
        y1 = int(tupla[1][0])
        y2 = int(tupla[1][1])
        o1 = self.Mapa.mapa[x1][y1]
        o2 = self.Mapa.mapa[x2][y2]
        r = []
        if x2 > x1:
            while x2 > x1:
                x1 += 1
                u = self.Mapa.mapa[x1][y1]
                r.append(u.tipo)
        else:
            while x2 > x1:
                x1 -= 1
                u = self.Mapa.mapa[x1][y1]
                r.append(u.tipo)
        if y2 > y1:
            while y2 > y1:
                y1 += 1
                u = self.Mapa.mapa[x1][y1]
                r.append(u.tipo)
        else:
            while y2 > y1:
                y1 -= 1
                u = self.Mapa.mapa[x1][y1]
                r.append(u.tipo)
        return 'Coming soon...'

    # Consultas sub-grilla actual

    def contador(bloque, ubicacion):
        c = 0
        for i in bloque:
            for j in i:
                if j == ubicacion:
                    c += 1
        return c

    def consulta4(self, tupla):
        if self.Mapa.nivel_zoom == 6:
            ubi = ((tupla[0][0]).strip()).title()
            num = int(tupla[1][0]) * 2
            blo_sup = self.Mapa.mapa[self.y1 - num:self.y2 - 2]
            for i in range(len(blo_sup)):
                blo_sup[i] = blo_sup[i][self.x1:self.x2]
            blo_inf = self.Mapa.mapa[self.y1 + 2:self.y2 + num]
            for i in range(len(blo_inf)):
                blo_inf[i] = blo_inf[i][self.x1:self.x2]
            blo_der = self.Mapa.mapa[self.y1:self.y2]
            for i in range(len(blo_der)):
                blo_der[i] = blo_der[i][self.x1 + 2:self.x2 + num]
            blo_izq = self.Mapa.mapa[self.y1:self.y2]
            for i in range(len(blo_izq)):
                blo_izq[i] = blo_izq[i][self.x1 - num:self.x2 - 2]
            return Tarea.contador(blo_sup, ubi) + Tarea.contador(blo_inf, ubi) + Tarea.contador(blo_der,
                                                                                                ubi) + Tarea.contador(
                blo_izq, ubi)
        else:
            return 'Acceso Prohibido'

    def consulta5(self, tupla):
        if self.Mapa.nivel_zoom == 6:
            ubi = ((tupla[0][0]).strip()).title()
            try:
                cantidad = int(tupla[1][0])
            except:
                return 'Error: Dato ingresado incorrecto'
            d = 1
            c = 0
            while c < cantidad:
                blo_sup = self.Mapa.mapa[self.y1 - 2 * d:self.y2 - 2 * d]
                for i in range(len(blo_sup)):
                    blo_sup[i] = blo_sup[i][self.x1:self.x2]

                blo_inf = self.Mapa.mapa[self.y1 + 2 * d:self.y2 + 2 * d]
                for i in range(len(blo_inf)):
                    blo_inf[i] = blo_inf[i][self.x1:self.x2]

                blo_der = self.Mapa.mapa[self.y1:self.y2]
                for i in range(len(blo_der)):
                    blo_der[i] = blo_der[i][self.x1 + 2 * d:self.x2 + 2 * d]
                blo_izq = self.Mapa.mapa[self.y1:self.y2]

                for i in range(len(blo_izq)):
                    blo_izq[i] = blo_izq[i][self.x1 - 2 * d:self.x2 - 2 * d]

                c += Tarea.contador(blo_sup, ubi) + Tarea.contador(blo_inf, ubi) + Tarea.contador(blo_der,
                                                                                                  ubi) + Tarea.contador(
                    blo_izq, ubi)
                d += 1
            return d - 1
        else:
            return 'Acceso Prohibido'
