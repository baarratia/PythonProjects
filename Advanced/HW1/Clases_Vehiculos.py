__author__ = 'Benja'


class vehiculo:
    vehiculos = {}

    def __init__(self, model, size, speed, cost):
        self.model = model
        self.size = size
        self.speed = speed
        self.cost = cost
        if self.size == 'Big': # num_size facilitará las cosas al momento de ver donde pueden entrar
            self.num_size = 3
        if self.size == 'Medium':
            self.num_size = 2
        if self.size == 'Small':
            self.num_size = 1
        vehiculo.vehiculos[self.model] = self


class avion(vehiculo):
    aviones = {}

    def __init__(self, model, size, speed, cost, range, seats, volume, weight, cargo):
        super(avion, self).__init__(model, size, speed, cost)
        self.range = range
        self.seats = seats
        self.volume = volume
        self.weight = weight
        self.cargo_types = cargo
        self.mensaje = 'avion'
        avion.aviones[self.model] = self


    def __str__(self):
        return 'modelo:{0}, porte:{1}, velocidad:{2}, rango:{3},\n asientos:{4}, volumen:{5},\n peso:{6}, tipo de cargo:{7}, costo:{8}\n'.format(
            self.model, self.size, self.speed, self.range, self.seats, self.volume, self.weight, self.cargo_types,
            self.cost)


class barco(vehiculo):
    barcos = {}

    def __init__(self, model, size, speed, cost, volume, weight, cargo):
        super(barco, self).__init__(model, size, speed, cost)
        self.volume = volume
        self.weight = weight
        self.cargo_types = cargo
        self.mensaje = 'barco'
        barco.barcos[self.model] = self


    def __str__(self):
        return 'modelo:{0}, porte:{1}, velocidad:{2},\nvolumen:{3},\n peso:{4}, tipo de cargo:{5}, costo:{6}\n'.format(
            self.model, self.size, self.speed, self.volume, self.weight, self.cargo_types,
            self.cost)


class crucero(vehiculo):
    cruceros = {}

    def __init__(self, model, size, speed, cost, seats):
        super(crucero, self).__init__(model, size, speed, cost)
        self.seats = seats
        self.mensaje = 'crucero'
        crucero.cruceros[self.model] = self

    def __str__(self):
        return 'modelo:{0}, porte:{1}, velocidad:{2},\n asientos:{3}, costo:{4}\n'.format(
            self.model, self.size, self.speed, self.seats,
            self.cost)


class bus(vehiculo):
    bus = {}

    def __init__(self, model, size, speed, cost, seats):
        super(bus, self).__init__(model, size, speed, cost)
        self.seats = seats
        self.mensaje = 'bus'
        crucero.cruceros[self.model] = self

    def __str__(self):
        return 'modelo:{0}, porte:{1}, velocidad:{2},\n asientos:{3}, costo:{4}\n'.format(
            self.model, self.size, self.speed, self.seats,
            self.cost)


class camion(vehiculo):
    camiones = {}

    def __init__(self, model, size, speed, cost, volume, weight, cargo):
        super(camion, self).__init__(model, size, speed, cost)
        self.volume = volume
        self.weight = weight
        self.cargo_types = cargo
        self.mensaje = 'camion'
        camion.camiones[self.model] = self


    def __str__(self):
        return 'modelo:{0}, porte:{1}, velocidad:{2},\nvolumen:{3},\n peso:{4}, tipo de cargo:{5}, costo:{6}\n'.format(
            self.model, self.size, self.speed, self.volume, self.weight, self.cargo_types,
            self.cost)


