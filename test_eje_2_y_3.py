import unittest
from clase2_ej_2_y_3 import *

class test_es_primo(unittest.TestCase):
    def test_uno_y_cero(self):
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))   
    
    def test_primo(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(17))
        
    
    
    def test_compuesto(self):
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(964))
    
    def test_negativo(self):
        self.assertTrue(es_primo(-2))
        self.assertTrue(es_primo(-17))
        self.assertFalse(es_primo(-4))
        self.assertFalse(es_primo(-964))
        
        
class test_cuantos_primos_en_rango(unittest.TestCase):
    def test_n_menor_m(self):
        self.assertEqual(cuantos_primos_en_rango(2, 7), 4)
    def test_n_igual_m(self):
        self.assertEqual(cuantos_primos_en_rango(5, 5), 1)
        self.assertEqual(cuantos_primos_en_rango(4,4), 0)
    def test_n_mayor_m(self):
        self.assertEqual(cuantos_primos_en_rango(7, 2), 4)
    def test_n_positivo_m_neg(self):
        self.assertEqual(cuantos_primos_en_rango(-3, 3), 4)
    def test_m_positivo_n_neg(self):
        self.assertEqual(cuantos_primos_en_rango(3, -3), 4)
    
    
         
        
    
if __name__ =='__main__':
   unittest.main(verbosity=2)