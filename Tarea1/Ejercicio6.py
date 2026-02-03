def tabla(n):
    for contador in range(1, 11):
        print(n, "x", contador, "=", n * contador)

numero = int(input("Por favor ingrese un número para mostrar su tabla de multiplicación del 1 al 10: "))

tabla(numero)
