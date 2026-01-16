basedatos = ["Compu", "Laptop", "CPU", "Teclado"]

print(basedatos)

basedatos.append("Mouse")

print(basedatos)

for item in basedatos:
    if "mose".lower() == item.lower():
        print("El mouse es un dispositivo...")
   