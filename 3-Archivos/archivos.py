"""
# Libreia io
from io import open

# ombre del archivo y w para escribir/ r para leer
archivo = open("ArchivoDeTexto.txt", "w")

texto1 = "El primer texto es este \n asd \n asfgagga \n FIN"
archivo.write(texto1)

archivo.close()
"""
"""
# nose por que lo crean en la carpeta python
#
from io import open

archivo = open("ArchivoDeTexto.txt", "r")

texto_de_archivo = archivo.read()

print(texto_de_archivo)
"""
"""
texto_de_archivo = archivo.readlines()
print(texto_de_archivo)

texto_lineal = ""
for elemento in texto_de_archivo:
    elemento = elemento.replace("\n", "")
    texto_lineal += elemento

print(texto_lineal)

archivo.close()
"""
"""
# Para agregar texto al archivo se usa a de append

archivo = open("ArchivoDeTexto.txt", "a")

archivo.write("\nAsi agrego esta linea")
"""
