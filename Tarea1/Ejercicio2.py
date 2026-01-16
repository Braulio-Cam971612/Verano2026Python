def es_par(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

numero = float(input("Por favor ingrese un número: "))

print(es_par(numero))
76