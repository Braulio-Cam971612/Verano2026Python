#aquien llamo???????
from controller.carroController import carroController

def main():
    _carroController = carroController()
    # aca creamos un menu, interfaz

    print("Inicio de sistema")
    
    #creamos una variable y luego llamar al controller, 
    #y llamar a la funcion de insertar
    # placa, marca, modelo, color
    _carroController.insertarDatos("123","Nissan", "TXT", "Blanco")
    _carroController.insertarDatos("1234","Nissan", "2TXT", "Blanco")
    _carroController.insertarDatos("1235","Nissan", "T3XT", "Blanco")
    _carroController.insertarDatos("1236","Nissan", "4XT", "Azul")
    _carroController.insertarDatos("1236","Nissan", "T5XT", "Negro")

    _carroController.mostrarLista()


if __name__ == "__main__":
    main()    