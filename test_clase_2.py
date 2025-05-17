import unittest
from g6_part2 import *
   
class test_es_multiplo_de(unittest.TestCase):
    def test_es_multiplo_cero_y_uno(self):
        self.assertTrue(esMultiploDe(0, 5))
        self.assertFalse(esMultiploDe(1, 5))
        self.assertTrue(esMultiploDe(15,1))
        
    def test_es_multiplo_valores_iguales(self):
        self.assertEqual(esMultiploDe(8,8), True)
        
class test_fahrenheit_a_celsius(unittest.TestCase):
    def test_F_convertir_C(self):
        self.assertEqual(fahrenheit_a_celsius(140), 60)
    
if __name__ =='__main__':
    unittest.main(verbosity=2)
    
    
