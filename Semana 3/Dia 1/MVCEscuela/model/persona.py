#Abstracion...............
#Creacion o modelar los atributos del objeto
class Persona:

    contadorId = 1

    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.id = Persona.contadorId
        Persona.contadorId += 1

        


#Encapsulamiento protege el ingreso directo a los atributos.
#get
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad

    def getCorreo(self):
        return self.correo      


#ayuda a solo acceder al atributo que se quiere modificar         
#set

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setEdad(self, edad):
        self.edad = edad

    def setCorreo(self, correo):
        self.correo = correo


#Metodo poliformismo
#   
    def mostraDatos(self):
        return f" nombre: { self.nombre } edad: { self.edad }, correo: { self.correo }  " 