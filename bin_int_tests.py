"""módulo para hacer tests a módulo bin_int_module.py"""

import unittest#importar para test de pruebas
import bin_int_module#para comprobar funcionalidad

class bin_int_test(unittest.TestCase):

    def test_bin_int(self):
        self.assertEqual(bin_int_module.convert_bit_int("001"), 1)
        self.assertEqual(bin_int_module.convert_bit_int("110"), 6)
        self.assertEqual(bin_int_module.convert_bit_int("211"), "Error de formato")
        self.assertEqual(bin_int_module.convert_bit_int("kkk"), "Error de formato")
        self.assertEqual(bin_int_module.convert_bit_int("011001110"), 206)
        self.assertEqual(bin_int_module.convert_bit_int("101110"), 46)
        self.assertEqual(bin_int_module.convert_bit_int("11111110000011010001100111111000111"), 34098171847)

        







if __name__ == "__main__":#esto se pone para que al llamar en la consola python bin_int_tests.py ejecute y compruebe los errores de arriba
    unittest.main()