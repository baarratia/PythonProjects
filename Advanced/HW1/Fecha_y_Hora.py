from email._header_value_parser import Value

__author__ = 'Benja'


def fecha_hora(
        vehiculo_flota):  # Dado un vehiculo perteneciente a la flota,
    # retorna una lista de todas las horas en
    # la que se encuentra "ocupado" en movimiento

    velocidad = float(vehiculo_flota.type.speed)
    horario_distancias = []  # lista de tuplas fecha inicio,  minutos que toma en recorrerla
    for i in vehiculo_flota.viajes:
        horario_distancias.append((
            i, vehiculo_flota.viajes[i].origin, vehiculo_flota.viajes[i].destination,
            int(60 * float(vehiculo_flota.viajes[i].route.length) / velocidad), vehiculo_flota.viajes[i].route))
    horario_distancias.sort()
    for i in horario_distancias:
        f, p, d, t, r = i
        vehiculo_flota.itinerario[f] = p
        ti = t
        fp = f.split(' - ')
        fecha = fp[0].split('/')
        dia = int(fecha[0])
        mes = int(fecha[1])
        ano = int(fecha[2])
        hora = (fp[1].split(':'))
        hr = int(hora[0])
        min = int(hora[1])
        while t != 0:
            min += 1
            t -= 1
            if min >= 60:
                min -= 60
                hr += 1
                if hr >= 24:
                    hr -= 24
                    dia += 1
            f_actual = str(dia).zfill(2) + '/' + str(mes).zfill(2) + '/' + str(ano).zfill(2) + ' - ' + str(hr).zfill(
                2) + ':' + str(min).zfill(2)
            vehiculo_flota.itinerario[f_actual] = r
        vehiculo_flota.horas_llegada.append((f_actual, d))


def ingresar_fecha():
    print('\nIngrese fecha de la forma dd/mm/aa\n ')
    c = 1
    while c == 1:
        try:
            mes = input('Mes:   ').strip()
            if len(mes) > 2:
                raise ValueError
            if int(mes) > 12 or int(mes) < 1:
                raise ValueError
            else:
                if len(mes) == 1:
                    mes = mes.zfill(2)
                    c = 0
                else:
                    c = 0
        except:
            print('\nMes invalido, intente nuevamente\n ')
    c = 1
    while c == 1:
        try:
            dia = input('Día:   ').strip()
            if ((int(mes) == (1 or 3 or 5 or 7 or 8 or 10 or 12)) and (int(dia) > 31)) or (
                        (int(mes) == (4 or 6 or 9 or 11)) and (int(dia) > 30)) or ((int(mes) == 2) and (int(dia) > 29)):
                raise ValueError
            else:
                if int(dia) < 1:
                    raise ValueError
                else:
                    if len(dia) == 1:
                        dia = dia.zfill(2)
                        c = 0
                    else:
                        c = 0
        except:
            print('\nDía invalido, intente nuevamente\n ')
    print(dia + '/' + mes + '/2015')
    print('\nIngrese Hora\n ')
    c = 1
    while c == 1:
        try:
            hr = input('Hora:   ').strip()
            if len(hr) > 2:
                raise ValueError
            if int(hr) > 23 or int(hr) < 0:
                raise ValueError
            else:
                if len(hr) == 1:
                    hr = hr.zfill(2)
                    c = 0
                else:
                    c = 0
        except:
            print('\nHora invalida, intente nuevamente\n ')
    c = 1
    while c == 1:
        try:
            min = input('Minuto:   ').strip()
            if len(min) > 2:
                raise ValueError
            if int(min) > 59 or int(hr) < 0:
                raise ValueError
            else:
                if len(min) == 1:
                    min = min.zfill(2)
                    c = 0
                else:
                    c = 0
        except:
            print('\nMinuto invalido, intente nuevamente\n ')
    return (dia + '/' + mes + '/2015' + ' - ' + hr + ':' + min)

