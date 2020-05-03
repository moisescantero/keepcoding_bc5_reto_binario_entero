"""programa para convertir número binario a su entero correspondiente con test de pruebas main.py ó programa principal"""
from bin_int_module import convert_bit_int #importar funcionalidad

#guardo en variable return lo que me devuelva el módulo de funcionalidad bin_int_module.py que se encarga de convertir la cadena introducida 
# a entero o devuelve error
result = convert_bit_int(input("Ingrese un número binario (compuesto por 0 y 1): "))

print(result)#imprimo el resultado de la variable
