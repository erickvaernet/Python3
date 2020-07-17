
import pickle
"""
lista_a_guardar = ["primero", 1, 2, 3, False, True, "lista Fin"]
archivo_b = open("listag", "wb")  # wb para escribir en binario

pickle.dump(lista_a_guardar, archivo_b)
archivo_b.close()
"""
"""

archivo_b = open("listag", "rb")  # Read binary

lista_importada = pickle.load(archivo_b)

print(lista_importada)

archivo_b.close()
del (archivo_b)
"""
"""
# para objetos/IMPORTANTE hay que tener la clase declarada en el archivo del que se abre

class auto():

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def estado(self):
        print("Color:", self.color)
        print("Marca:", self.marca)


auto_1 = auto("Toyota", "Negro")
auto_2 = auto("Sandero", "Azul")
auto_3 = auto("Gol", "Rojo")

autos = [auto_1, auto_2, auto_3]

autines_a = open("coleccion_autos", "wb")

pickle.dump(autos, autines_a)

autines_a.close()
del (autines_a)

coleccion_leer = open("coleccion_autos", "rb")

coleccion = pickle.load(coleccion_leer)

coleccion_leer.close()

for a in coleccion:
    print(a)

for a in coleccion:
    print("\n")
    a.estado()
"""
