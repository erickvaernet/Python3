class Animal:

    def __init__(self, especie=None, nombre="NN"):
        self.especie = especie
        self.nombre = nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_nombre(self):
        return self.nombre

    def __del__(self):
        print("Se elimino", self.nombre, " de especie", self.especie)

    def __str__(self):
        return f"Especie: {self.especie}, Nombre: {self.nombre}"


animalin_1 = Animal("Camponotus Barbaricus", "hormiga_1")

print(animalin_1.get_nombre())
animalin_1.set_nombre("Hormiga")
print(animalin_1)
