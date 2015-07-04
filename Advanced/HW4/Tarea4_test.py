__author__ = 'Benja'

from clases_botones import *
import random
import unittest


class TestEval((unittest.TestCase)):
    def setUp(self):
        self.N1 = str(random.randrange(-10, 10) + random.random())
        self.N2 = str(random.randrange(-10, 10) + random.random())
        self.Operacion_Simple = random.choice(['+', '-', '*', '**', '/'])
        self.Operacion_Compleja = random.choice(['abs', 'log'])
        self.Trigonometrica = random.choice(['sin', 'cos', 'tan'])
        self.Operacion_MM = random.choice(('max', 'min'))
        self.Op_1 = ('{0}{1}{2}'.format(self.N1, self.Operacion_Simple, self.N2))
        self.Op_2 = ('{0}({1})'.format(self.Operacion_Compleja, self.N1))
        self.Op_3 = ('{0}({1})'.format(self.Trigonometrica, str(radians(float(self.N1)))))
        self.Op_4 = ('{0}({1})'.format(self.Operacion_MM, self.N1 + ',' + self.N2))
        self.Op_Mala1 = ('{0}{1}{2}'.format(self.N1, '/', '0'))
        self.Op_Mala2 = ('{0}({1})'.format('log', '0'))

    def test_operaciones(self):
        if float(self.N2) == 0.0 and Operacion_Simple == '/':
            bool, mensaje = evaluar(self.Op_1)
            assert bool is False
        else:
            bool, mensaje = evaluar(self.Op_1)
            assert bool is True
        if float(self.N1) <= 0 and self.Operacion_Compleja == 'log':
            bool, mensaje = evaluar(self.Op_2)
            assert bool is False
        else:
            bool, mensaje = evaluar(self.Op_2)
            assert bool is True
        bool, mensaje = evaluar(self.Op_3)
        assert bool is True
        bool, mensaje = evaluar(self.Op_4)
        assert bool is True
        bool, mensaje = evaluar(self.Op_Mala1)
        assert bool is False
        bool, mensaje = evaluar(self.Op_Mala2)
        assert bool is False






