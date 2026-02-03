# try:
#     #todo el codigo ejecutandose
# except:
#     #Mostrara el codigo de error
#     
#

# 
# try:
#     numero = int(input("Ingrese un numero:"))
# 
#     print ("Su numero:",numero)
#     
# except :
#     print("Usted debe ingresar un valor numerico")


# 
# 
# try:
#     numero = int(input("Ingrese un numero:"))
# 
#     print ("Su numero:",numero)
#     
#     resultado = numero / 0
#     
# except ValueError:
#     print("Usted debe ingresar un valor numerico")
# 
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# 


try:
    print("Abriendo documento")
    
    f = open("test.csv")

except FileNotFoundError:
    print("Abriendo documento, no se logro porque no esta el archivo")
    
else:
    print("documento Abierto")
    
finally:
    print("Fin del proceso documento Abierto")