class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("Hola me llamo", self.nombre, "y tengo", self.edad, "años")

persona1 = Persona("Braulio", 20)
persona2 = Persona("Carlos", 25)

persona1.presentarse()
persona2.presentarse()
