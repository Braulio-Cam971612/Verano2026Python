frase = input("Por favor ingrese una frase cualquiera: ")

palabras = frase.split()

palabra_larga = palabras[0]

for palabra in palabras:
    if len(palabra) > len(palabra_larga):
        palabra_larga = palabra

print("La palabra más larga es:", palabra_larga)
print("Su longitud es:", len(palabra_larga))
