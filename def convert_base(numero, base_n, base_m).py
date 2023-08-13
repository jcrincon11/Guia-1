def convert_base(numero, base_n, base_m):
    if base_n == 10:
        num_base = int(numero)
    else:
        num_base = int(numero, base_n)
    
    if base_m == 10:
        convertir_numero = str(num_base)
    else:
        convertir_numero = format(num_base, 'X') if base_m == 16 else format(num_base, '0' + str(base_m) + 'b')
    
    return convertir_numero

def main():
    try:
        num = input("Ingresa un número: ")
        base_n = int(input("Ingresa la base del número de entrada (2-16): "))
        base_m = int(input("Ingresa la base a la que deseas convertir (2-16): "))
        
        if base_n < 2 or base_n > 16 or base_m < 2 or base_m > 16:
            print("Las bases deben estar entre 2 y 16.")
            return
        
        convertir_numero = convert_base(num, base_n, base_m)
        mensaje_ascii = chr(int(convertir_numero, base_m))
        
        print(f"El número convertido es: {convertir_numero}")
        print(f"Representación ASCII: {mensaje_ascii}")
        
        nu = int(input("Ingresa un número para obtener su representación ASCII: "))
        print(chr(nu))
        
    except ValueError:
        print("Ingresa un número válido y asegúrate de usar las bases correctas.")

if __name__ == "__main__":
    main()
