import sys

import os

sys.stdout.reconfigure(encoding="utf-8")

import csv

BASE_DIR = os.path.dirname(__file__) #lee la base del archivo Dia 2

ARCHIVO = os.path.join(BASE_DIR, 'csv', 'personas.csv')

#'csv/personas.csv'

####???
def guardarPersona(id, nombre, edad):
    #open    (src, atributos, lectura, systemaenco)
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as file:
              writer = csv.writer(file)
              
              writer.writerow([id, nombre, edad])
              
              print("Se guardaron datos")
              
              
guardarPersona(2, "Isaac", 21)    