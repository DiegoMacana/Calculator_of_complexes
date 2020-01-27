import unittest
import math
from Calculadora_de_Complejos import *
class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        a=(4,5)
        b=(4,6)
        self.assertEqual(suma(a,b),(8,11))
    def test_resta(self):
        a=(3,2)
        b=(5,-6)
        self.assertEqual(resta(a,b),(-2,8))
    def test_mult(self):
        a=(2,3)
        b=(4,5)
        self.assertEqual(multiplicar(a,b),(-7,22))
    def test_dividir(self):
        a=(3,2)
        b=(0,5)
        self.assertEqual(dividir(a,b),(0.4,-0.6))
    def test_modulo(self):
        a=(3,3)
        self.assertEqual(modulo(a),(math.sqrt(18)))
    def test_conjugado(self):
        a=(10,8)
        self.assertEqual(conjugado(a),(10,-8))
    def test_carteciana(self):
        a=(8,3)
        self.assertEqual(carteciana(a),(8,3))  


if __name__ == '__main__':
    unittest.main()
