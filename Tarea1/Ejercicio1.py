def conversionGrados(gradosC):
    return (gradosC * 9/5) + 32 

gradosC = float(input("Por favor introduzca los grados Celsius para cambiarlos a Fahrenheit: "))

print("La temperatura en grados Fahrenheit es: ", conversionGrados(gradosC))