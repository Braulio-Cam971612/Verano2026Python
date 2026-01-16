# El modelo
from model.carroModel import Carro
# la vista
import view.carroView as vistaCarro

class carroController:

    def __init__(self):
        #donde guardamos
        self.carroArreglo = []#guaramos la info temporal

    def mostrandoDatos(self):
        print(self.carroArreglo)

    #creamos una variable y luego llamar al controller, 
    def insertarDatos(self, placa, marca, modelo, color): 
            #y llamar a la funcion de insertar 
        nuevoDato =  Carro (placa, marca, modelo, color)
        self.carroArreglo.append(nuevoDato)
        vistaCarro.mostrandoMensaje(f"El nuevo carro ha sido incluido, Id {nuevoDato.id}")


    def mostrarLista(self):
        vistaCarro.mostrarLista(self.carroArreglo)