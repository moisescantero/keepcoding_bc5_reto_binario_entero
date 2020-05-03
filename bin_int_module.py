"""módulo para funcionalidad del programa conversor de binario a entero con test de preubas
001 = 0 * 2**2 + 0 * 2**1 + 1 * 2**0 = 0 + 0 + 1 = 1
110 = 1 * 2**2 + 1 * 2**1 + 0 * 2**0 = 4 + 2 + 0 = 6 """

def convert_bit_int(string):
    index = 0#índice para usar elevando al cuadrado
    tot_result = 0#variable para acumular el resultado total del número entero
    bit_list = []#lista vacía para almacenar cada caracter de la cadena introducida en main.py
    for carac in reversed(string):#bucle que recorre al revés la cadena introducida en main.py
        if carac == "0" or carac == "1":#compruebo que cada carácter sea 0 o 1
            bit_list.append(carac)#guardo en lista el carácter correspondiente en ese momento del bucle
            if carac == "1":#si el carácter en ese momento es 1
                tot_result += 2 **index#el resultado total es la suma de él mismo más elevar 2 a lo que valga el índice(2**0,2**1,etc)
                index += 1#incremento el índice 
            elif carac == "0":#y si el caracter en ese momento es 0
                index += 1#simplemente incremento el índice ya que multiplicar algo por 0 es 0
            else:#si el carácter no es ni 1 ni 0 entonces
                return "Error de formato"#retorna error de formato
            
        
        else:#si no es 0 o 1
            return "Error de formato"#devuelve error de formato
            
            

    return tot_result#retorna resultado del acumulado del número entero