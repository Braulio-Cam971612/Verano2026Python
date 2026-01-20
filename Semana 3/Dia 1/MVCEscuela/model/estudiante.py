from model.persona import Persona

#Abstracion...............
#Creacion o modelar los atributos del objeto
class Estudiante(Persona):

    # contadorIdEstudiante = 1
#nuevodato ( nombre, edad, correo, fechaingreso, grado)
    def __init__(self, nombre, edad, correo, fechaingreso, grado):
        super().__init__(nombre, edad, correo)

        self.fechaingreso = fechaingreso
        self.grado = grado    
        # self.id = Estudiante.contadorIdEstudiante
        # Estudiante.contadorIdEstudiante += 1        
    # def __init__(self, nombre, edad, correo, fechaingreso, grado):
    #     self.nombre = nombre
    #     self.edad = edad
    #     self.correo = correo
    #     self.fechaingreso = fechaingreso
    #     self.grado = grado


#Encapsulamiento protege el ingreso directo a los atributos.
#get
    # def getNombre(self):
    #     return self.nombre
    
    # def getEdad(self):
    #     return self.edad

    # def getCorreo(self):
    #     return self.correo        
    
    def getgrado(self): 
        return self.grado


#ayuda a solo acceder al atributo que se quiere modificar         
#set

    # def setNombre(self, nombre):
    #     return self.nombre
    
    # def setEdad(self, edad):
    #     return self.edad

    # def setCorreo(self, correo):
    #     return self.correo        

    
    def setgrado(self, grado): 
        self.grado = grado

#Metodo poliformismo
#   
    def mostraDatos(self):
        return f" {super().mostraDatos()} grado: { self.grado }"        