nombres = []

for contador in range(5):
    nombre = input("Por favor ingrese un nombre: ")
    nombres.append(nombre)

print("Lista completa de nombres:", nombres)
print("Primer nombre de la lista:", nombres[0])
print("Último nombre de la lista:", nombres[4])
print("Cantidad total de nombres en la lista:", len(nombres))
