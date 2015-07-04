__author__ = 'Benja'


def crear_vehiculo(archivo, avion, barco, crucero, bus, camion):
    arch = open(archivo, 'r')
    linea_base = ''
    for i in arch:
        linea = i.split('\t')
        if len(linea) == 1:
            linea_base = linea
            atributos = arch.readline()
        while linea_base[0] == 'Airplane\n':
            linea = arch.readline().split('\t')
            if len(linea) == 1:
                linea_base = linea
                continue
            model = linea[0]
            size = linea[1]
            speed = linea[2]
            range = linea[3]
            seats = linea[4]
            volume = linea[5]
            weight = linea[6]
            cargo = linea[7].split(',')
            cost = linea[8]
            avion(model, size, speed, cost, range, seats, volume, weight, cargo)
            continue
        while linea_base[0] == 'CargoShip\n' or linea_base[0] == 'Truck\n':
            linea = arch.readline().split('\t')
            if len(linea) == 1:
                linea_base = linea
                continue
            model = linea[0]
            size = linea[1]
            speed = linea[2]
            volume = linea[3]
            weight = linea[4]
            cargo = linea[5].split(', ')
            cost = linea[6]
            if linea_base[0] == 'CargoShip\n':
                barco(model, size, speed, cost, volume, weight, cargo)
                continue
            elif linea_base[0] == 'Truck\n':
                camion(model, size, speed, cost, volume, weight, cargo)
                continue
        while linea_base[0] == 'CruiseShip\n' or linea_base[0] == 'Bus\n':
            linea = arch.readline().split('\t')
            if len(linea) == 1:
                linea_base = linea
                continue
            model = linea[0]
            size = linea[1]
            speed = linea[2]
            seats = linea[3]
            cost = linea[4]
            if linea_base[0] == 'CruiseShip\n':
                crucero(model, size, speed, cost, seats)
                continue
            elif linea_base[0] == 'Bus\n':
                bus(model, size, speed, cost, seats)
                continue
    arch.close()