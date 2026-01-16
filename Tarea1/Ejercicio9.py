def saludar():
    print("Hola, bienvenido al programa sumador de Braulio ;)")

def sumar():
    a = int(input("Por favor ingrese el primer número: "))
    b = int(input("Por favor ingrese el segundo número: "))
    print("La suma es:", a + b)

opcion = 0

while opcion != 3:
    print("\nMENÚ")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Salir")

    opcion = int(input("Elija una opción: "))

    match opcion:
        case 1:
            saludar()
        case 2:
            sumar()
        case 3:
            print("Saliendo del programa, que tengas un buen dia")
        case _:
            print("Opción no válida, ingresa un valor correcto")
