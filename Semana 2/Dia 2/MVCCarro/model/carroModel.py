
# Crear una clase Carro con los atributos:

# id (autoincremental y único),
# placa,
# marca,
# modelo,
# color.
class Carro:
    contadorId = 1

    def __init__(self, placa, marca, modelo, color):
        self.id = Carro.contadorId
        Carro.contadorId += 1
        
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrandoDatos(self):
        return f"ID : {self.id}, {self.placa}, {self.marca}, {self.modelo}, {self.color} "