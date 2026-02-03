numero = float(input("Por favor ingrese un número entero positivo: "))

if numero > 0:
    contador = 1
    while contador <= numero:
        print(contador)
        contador += 1
else:
    print("El número debe ser positivo")
