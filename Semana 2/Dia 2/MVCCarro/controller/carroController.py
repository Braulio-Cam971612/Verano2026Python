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


    def modificarDatos(self, id, placa, marca, modelo, color): 
        #print(id)
            #y llamar a la funcion de insertar 
        objetoEncontrado = self.buscarId(id)
        
        if objetoEncontrado:
            objetoEncontrado.placa = placa
            objetoEncontrado.marca = marca
            objetoEncontrado.modelo = modelo
            objetoEncontrado.color = color

            vistaCarro.mostrandoMensaje(f"Datos actualizados en {id}")
        else:
            vistaCarro.mostrandoMensaje(f"Datos no actualizados en {id}")
       

    def buscarId(self, id):   
        #print("Linea 40", id)     
        for items in self.carroArreglo: 
            #print("Linea 42", items.id, id)           
            if items.id == id:
                #print("Linea 43", id)     
                return items
        return None


    def mostrarLista(self):
        vistaCarro.mostrarLista(self.carroArreglo)