def mostrar_suma(lista):
    suma = 0
    for numero in lista:
        suma += numero
    print("La suma total es: ", suma)

numeros = [12, 42, 73, 24, 55]

mostrar_suma(numeros)
