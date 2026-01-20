from model.persona import Persona

#Abstracion...............
#Creacion o modelar los atributos del objeto
class Profesor(Persona):

    # contadorIdProfesor = 1
#nuevodato ( nombre, edad, correo, especialidad)
    def __init__(self, nombre, edad, correo, especialidad):
        super().__init__( nombre, edad, correo)
        # self.nombre = nombre
        # self.edad = edad
        # self.correo = correo
        self.especialidad = especialidad
        # self.id = Profesor.contadorIdProfesor
        # Profesor.contadorIdProfesor += 1


    # def __init__(self, nombre, edad, correo, especialidad):
    #     self.nombre = nombre
    #     self.edad = edad
    #     self.correo = correo
    #     self.especialidad = especialidad
    #     # self.id = Profesor.contadorIdProfesor
    #     # Profesor.contadorIdProfesor += 1


#Encapsulamiento protege el ingreso directo a los atributos.
#get
    # def getNombre(self):
    #     return self.nombre
    
    # def getEdad(self):
    #     return self.edad

    # def getCorreo(self):
    #     return self.correo      

    def getespecialidad(self): 
        return self.especialidad

#ayuda a solo acceder al atributo que se quiere modificar         
#set

    # def setNombre(self, nombre):
    #     return self.nombre
    
    # def setEdad(self, edad):
    #     return self.edad

    # def setCorreo(self, correo):
    #     return self.correo        

    def setespecialidad(self): 
        return self.especialidad
    

#Metodo poliformismo
#   
    def mostraDatos(self):
        return f" {super().mostraDatos()} especialidad: { self.especialidad }"        