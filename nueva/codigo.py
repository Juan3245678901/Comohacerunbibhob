def obtener_numeros():
    numeros = []
    
    print("Ingresa los números (ingresa 'si' para detener):")
    while True:
        num = input("Número: ")
        
        if num.lower() == 'si':
            break
        
        try:
            num = int(num)
            if num in numeros:
                print("Ese número ya ha sido ingresado. Inténtalo de nuevo.")
            else:
                numeros.append(num)
        except ValueError:
            print("Solo se aceptan números. Inténtalo de nuevo.")
    
    return numeros

def obtener_numeros_no_repetidos(arr1, arr2):
    numeros_no_repetidos = [num for num in arr1 if num not in arr2] + [num for num in arr2 if num not in arr1]
    return numeros_no_repetidos

print("Llenado del primer arreglo:")
arreglo1 = obtener_numeros()

print("\nLlenado del segundo arreglo:")
arreglo2 = obtener_numeros()

numeros_no_repetidos = obtener_numeros_no_repetidos(arreglo1, arreglo2)

print("\nNúmeros que no se repiten en ambos arreglos:")
print(numeros_no_repetidos)
