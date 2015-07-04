__author__ = 'Benja'

def Armar_reloj(tiempo, x=False):
    if x is not True:
        hora = str(int(9 + tiempo // 3600))
    else: hora = str(int(tiempo // 3600))
    if int(hora) > 23:
        hora = str(int(tiempo// 3600)-12)
    min = str(int((tiempo % 3600) // 60))
    sec = str(int((tiempo % 3600) % 60))
    return '{0}:{1}:{2}'.format(hora.zfill(2), min.zfill(2), sec.zfill(2))