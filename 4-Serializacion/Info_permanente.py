# Encontre algo IMPORTANTE cuando usamos print en un objeto instanciado nos imprime "__main__.persona"
# Sin embargo existe el metodo __str__ que permite que alcrearlo en la clase, cuando se llame al metodo print(persona), en vez
# de que pase lo de arriba(__main__) se impriman los atributos

"""
class persona():

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Nueva persona creada:", self.nombre)


persona1 = persona("Erick", "Masculino", 25)

print(persona1)
"""
"""
# GUARDADO PERMANENTE
import pickle


class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Nueva persona creada:", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas = []

    def __init__(self):
        fichero = open("fichero_personas", "ab+")
        fichero.seek(0)
        try:
            self.personas = pickle.load(fichero)
            print("Se cargaron {} personas del fichero externo".format(
                len(self.personas)))
        except:
            print("No hay personas cargadas en el fichero externo")
        finally:
            fichero.close()
            del (fichero)

    def agregarPersonas(self, pers):
        self.personas.append(pers)
        # IMPORTANTE de esta forma cada vez que agreguemos una persona en el programa, se guarda en memoria secund
        self.guardarEnFichero()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarEnFichero(self):
        fichero = open("fichero_personas", "wb")
        pickle.dump(self.personas, fichero)
        fichero.close()
        del (fichero)

    def mostrarContenidoFichero(self):
        print("Info fichero externo:\n")
        for per in self.personas:
            print(per)
            print()



persona1 = Persona("Erick", "Masculino", 25)
persona2 = Persona("Ian", "Masculino", 22)
persona3 = Persona("Daniela", "Femenino", 26)

mi_lista = ListaPersonas()
mi_lista.agregarPersonas(persona1)
mi_lista.agregarPersonas(persona2)
mi_lista.agregarPersonas(persona3)

#mi_lista = ListaPersonas()

mi_lista.mostrarContenidoFichero()
"""
