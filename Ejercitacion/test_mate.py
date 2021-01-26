from mate import *
import unittest

class TestFuncionesMatematicas(unittest.TestCase):
    
    def test_sumas(self):
        self.assertEqual(sumar(5,4), 9, 'Caso base')
        self.assertEqual(sumar(0, 0), 0, 'Cero') 
        self.assertEqual(sumar(4, -4), 0, 'Positivos y negativos')
        self.assertEqual(sumar(3.5, 6.5), 10, 'Punto flotante')
        self.assertTrue(sumar(64222, 5453) == sumar(5453, 64222), 'Conmutativa')
        
    def test_multiplicaciones(self):
        self.assertEqual(multiplicar(5, 4), 20, 'Caso base')
        
    def test_divisiones(self):
        self.assertRaises(ZeroDivisionError, dividir, 20, 0)
        self.assertNotRaises(ZeroDivisionError, dividir, 20, 1)
        
    def test_combos(self):
        self.assertNotEqual(sumar(4,5), restar(4,5), 'Sumar != Restar')
        self.assertFalse(sumar(4,5) == restar(4,5), 'Sumar != Restar')

        self.assertNotIn(sumar(4,5) , [1, 2, 3, 4, 5])
        self.assertIn(sumar(4,5) , [6, 7, 8, 9, 10])

        div, mod = dividir(100, 10)
        self.assertIsNotNone(div);    
        
if __name__ == '__main__':
    unittest.main()