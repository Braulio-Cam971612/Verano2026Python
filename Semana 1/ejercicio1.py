# Ejercicio 1: Conversión de temperatura
# Cree un programa que solicite al usuario una temperatura en grados Celsius y muestre su equivalente
# en Fahrenheit usando la fórmula F = (C * 9/5) + 32.
# Rúbrica de calificación:
# • Código funcional y sin errores (4 pts)
# • Uso correcto de variables (3 pts)
# • Mensajes claros (1 pt)
# • Captura de pantalla (1 pt)
# • Reflexión (1 pt)

def ConversionTemperatura(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))

print("La temperatura es en el Celsius: ", celsius)

print ( "La temperatura en Fahrenheit", ConversionTemperatura(celsius) )