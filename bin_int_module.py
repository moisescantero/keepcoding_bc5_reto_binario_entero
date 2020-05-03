"""módulo para funcionalidad del programa conversor de binario a entero con test de preubas"""

def convert_bit_int(string):
    index = 0
    int_result = 0
    tot_result = 0
    bit_list = []
    for carac in reversed(string):
        if carac == "0" or carac == "1":
            bit_list.append(int(carac))
            if carac == "1":
                int_result = 2 **index
                tot_result += int_result
                index += 1
            elif carac == "0":
                index += 1
            else:
                return "Error de formato"
            
        
        else:
            return "Error de formato"
            
            

    return tot_result