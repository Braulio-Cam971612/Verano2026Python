🚗 📝 ENUNCIADO DEL EJERCICIO – Sistema de Gestión de Carros
 con Identificador Único
En este ejercicio, usted deberá implementar un 
sistema básico de gestión de carros utilizando
 Programación Orientada a Objetos (POO) en Python.

El programa permitirá registrar carros, 
asignarles un identificador único, modificarlos, 
eliminarlos y mostrarlos. Además, 
pondrá en práctica el manejo de listas que contienen objetos,
 así como las operaciones fundamentales de un sistema CRUD.

🎯 Objetivo del ejercicio
Desarrollar un programa que permita:

Crear una clase Carro con los atributos:

id (autoincremental y único),

placa,

marca,

modelo,

color.

Almacenar múltiples carros en una lista de objetos.

Implementar operaciones CRUD:

Insertar un carro nuevo,

Buscar un carro por ID,

Modificar datos de un carro existente,

Eliminar un carro por ID,

Mostrar todos los carros registrados.

Aplicar conceptos de:

Constructores,

Atributos de instancia y clase,

Métodos para mostrar información,

Funciones independientes para CRUD,

Manejo de listas de objetos,

Programación estructurada apoyada en POO.

📘 Descripción del funcionamiento esperado
✔ Clase Carro
El programa debe definir una clase llamada Carro, la cual debe:

Contener un atributo de clase que permita generar IDs autoincrementales.

Registrar la información básica del vehículo (placa, marca, modelo, color).

Contar con un método mostrar() que devuelva una representación en texto del carro, incluyendo su ID.

✔ Lista de Carros
El programa debe mantener una lista global llamada:

 
carros = [] 
En esta lista se almacenarán todas las instancias de Carro creadas.

✔ Funciones CRUD
El programa debe implementar:

insertar(placa, marca, modelo, color)
Crea un nuevo Carro, le asigna un ID único y lo agrega a la lista.

buscar_por_id(id)
Recorre la lista y retorna el carro cuyo ID coincida con el parámetro.

modificar(id, nuevaPlaca, nuevaMarca, nuevoModelo, nuevoColor)
Permite editar los datos de un carro existente.

borrar(id)
Elimina de la lista el carro cuyo ID coincida.

mostrar_todos()
Imprime la información de todos los carros registrados utilizando el método mostrar().

🧪 Programa Principal
El estudiante deberá:

Insertar al menos tres carros con datos ficticios.

Mostrar la lista completa.

Buscar un carro por su ID.

Modificar los datos de otro carro.

Eliminar un carro por su ID.

Mostrar la lista final comparativa.