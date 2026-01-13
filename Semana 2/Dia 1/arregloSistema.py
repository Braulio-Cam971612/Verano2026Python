#Mi variables
personas = ["Mario", "Isaac", "Alberto","Sasha"]

def modificar():
    print("Modificando")

print("Los usuarios del sistema", personas)
modificar()
usuarioNuevo = input("Ingrese un nuevo usuario")
personas.append(usuarioNuevo)

print("Los usuarios del sistema", personas)

#La seccion de buscar
buscar = input("Que usuario desea buscar?")
print(personas.index(buscar))

#La seccion de modificar
editar = input("Que usuario desea modificar?")

#La seccion de borrar
