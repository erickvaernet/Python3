
"""
STRINGS:
Son Inmutables

my_string="Esta es una cadena"
result="Este es un {a}-y-esta como {b} ".format(a="STRING",b="OBJETO")
result=result.lower()

pos={result.find('o')}

print(result)
print(pos)
print(result.count('st'))
print(result.replace('st','xxx'))
print(result.split('-'))
"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
LISTAS:
Son Mutables

my_list=["pos0",1,2,3,True,False,"seis"]
print(my_list)
my_list.append("siete")
print(my_list)
my_list.insert(2,"insertado")
print(my_list)
my_list.remove(1)
print(my_list)
ultimo =my_list.pop()
print(my_list)
print(ultimo)
"""

"""
LISTAS-2
Son Mutables

lista=[2,3,1,9,2,16,67,2,1,75,894,25,96,24,12,653]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

lista_2=[34,23,63,82]
print(lista_2)
lista_2.extend(lista)
print(lista_2)
lista_2.sort()
print(lista_2)
"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
TUPLAS
similares a listas pero son Inmutables

# IMPORTANTE: poner , aunque haya un elemento por que sino no se toma como tupla// inclusive pueden ir sin parentesis pero si o si coma , auqnue tenga un elemento


tupla=(1,4,2,"string_1",'a',45,True,"si")
print(tupla)
print(tupla[3])
"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
DICCIONARIOS
no se rigen de indices, Las claves deben ser inmutables

diccionario={ 'primer_elemento': 1,
			  'segundo_elemento': "dos",
			  'tercer_elemento': True,
			}
print(diccionario)

# Obtener valor
print(diccionario["primer_elemento"])

# Puedo agregar elementos al diccionario entre [la nueva clave] y leugo del = el valor a asignar:
diccionario['cuarto_elemento']="Nuevo elemento"
print(diccionario)
# Se pueden modificar el contenido de cada llave pero no podemos modificar la llave en si. Si la llaver existe se actualiza el contenido

# Regrsa el contenido de llave 'z', si no existe regresa false   o cualquier elemento que pongamos en el segundo parametro
encuentra = diccionario.get('z',False)
print( encuentra)

# Eliminar un elemento con la llave usamos del
del diccionario["primer_elemento"]
print("valores del dicc:",diccionario,'\n')

# Obtenemos las llaves y las pasamos como listas
llave=list(diccionario.keys())
print(llave)

# Obtenemos las llaves y las pasamos como listas
contenido=list(diccionario.values())
print(contenido)

print("EL contenido de la llave","'"+llave[0]+"'","es:",contenido[0])

# para extender el diccionario:
diccionario_2={"dicc2_1":2,"dicc2_2":"segundovalor del segdicc"}
diccionario.update(diccionario_2)
print(diccionario)

# Para recorrer diccioanrio
 for key in diccionario:
>>> print("la clave es: ", key)
>>> print("su valor: ", diccionario[key])

# Metodo .items() devuelve lista de tuplas cada una con el par [(llave,contenido),(llave,contenido)]

"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
CONDICIONALES

condicion=True

if condicion:
	print(condicion)
elif condicion=='falso':
	print(condicion)
else:
	print(condicion)

# todas las variables son booleanas por ejemplo:

if []: #al estar vacia la lista actua como falsi
	print("Lista llena")
else:
	print("Lista vacia")
# para en num 1 es true y 0 es falso por ej // otros ejemplos de falsi diccionarios vacios{} listas vacias[]  tuplas vacias() o string vacio''
# None tambien actua como falsi
variable=None

# and or not
condicion_1=True
condicion_2=False

if condicion_1 and condicion_2:
	print("and")
elif condicion_1 or condicion_2:
	print("or")

"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Estructuras de control REPETITIVAS  /Bucles o iteraciones

"""
# WHILE

i=0
while True:
	print(i)
	if i==3:
		print("fin")
		break
	i+=1

contador=0
while contador <=10:
	print(contador)
	if contador==10:
		print("fin")
	contador += 1

"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# FOR

lista_for=["asd",1,4,72,64,True,False,"hola",8,9,10,11]

for elementos in lista_for:
	print(elementos)

# difernecia ente range() y xrange: https://www.youtube.com/watch?v=d_mxzMas2p8 //xrange ocupa menos memoria ram (bastante menos)

-If you want to write code that will run on both Python 2 and Python 3, use range() as the xrange funtion is deprecated in Python 3
-range() is faster if iterating over the same sequence multiple times.
-xrange() has to reconstruct the integer object every time, but range() will have real integer objects. (It will always perform worse in terms of memory however)

print("for uno")
for i in range(10): #Itera del 0 al 9(inclusive ) equivalente a mientras sea i<10
	print(lista_for[i])

print("for dos")
for i in range(1,10): #el for va desde el elemento 1 (recordemos que lista empieza en 0), hasta el elemento 10(no incluye el 10, es equivalente a mientras i<10)
	print(lista_for[i])

print("for tres")
for i in range(1,10,2):#EL tercer parametro es steps o pasos, cada cuantos pasos itero en este caso de a dos valores
	print(lista_for[i])

# Strings son iterables
for letra in "Esto es un string":
	print(letra)

# Los diccionarios tambien son iterables pero devuelven dos valores uno es la llave y el otro es esl contenido
diccionario_for={'key1':"AAA", 'key2':2, 'key3':True}

# recordar poner el diccionario.items() //RECORDAR el .items()
for llave, contenido in diccionario_for.items():
	print("La llave", llave, "tiene de contenido:",contenido,)
"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
COMPREHENSIONS
Realizar listas,tuplas,diccionarios y llenarlos

lista_e = [pares for pares in range(10) if pares%2==0]
print("lista_e",lista_e)

tupla_e = tuple(pares for pares in range(10) if pares%2==0)
print("tupla_e",tupla_e)

diccionario_e = { key:content for key,content in enumerate(lista_e) if key<6 }
print("diccionario_e",diccionario_e)
"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# EXTRAS INFORMATORIO

# LISTAS
lista_info = ['uno',1,'dos',"dois",'tres',False]
elem_lista = len( lista_info )
print(elem_lista)

# CONDICIONAL WHILE
podemos usar else despues de while para indicar que pasa cuando finaliza while (RECONOCe las variables locales de while)

"""
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Desafios INFO

from random import shuffle
x=["Tener","El","Azul","Bandera","Volar","Alto"]

shuffle(x)

print(x)
"""
""""
# El valor predeterminado de end es \n lo que significa que después de la instrucción print se imprimirá una nueva línea. Así que simplemente declaró end es lo que quiere ser impresas después de la declaración print se ha ejecutado

Por ejemplo: - print ("hello",end=" +") imprimirá hello +
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias[1] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]

print (materias[1])
"""

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
FUNCIONES

def factorial(numero):
	factorial=1
	while numero>0:
		factorial=factorial*numero
		numero -= 1
	return factorial

print(factorial(5))

# En pyton se pueden regresar muchos valores de una funcion, estos se regresan como una tupla (3,Tru,"stringsi",2,Fale)
def tipos_d():
	return "String",[1,"true"],123,14,"fin"

print(tipos_d())

tupla_de_func= tipos_d()
segundof=tupla_de_func[2]
print(segundof)

# tambiens e puede asignar asi: (pero tienen que estar el mismo num de variables que de valores retornados)
dat_cero,dat_uno,dat_dos,dat_tres,dat_tres= tipos_d()
print(dat_tres, dat_cero)

# diferentes formas
ultimo= tipos_d()[4]
doble=tipos_d()[0:3]
print(ultimo)
print(doble)


# se pueden pasar funciones como parametro
def multiplicar (num1,num2):
	return num1*num2

def efe (funcion):
	return funcion(2,3)

print (efe(multiplicar))

# IMPORTANTE se pude usar * para decir que se puede pasar n-argumentos a la funcion

#	* -----> n valores ----->tuplas
#	**-----> n valores ----->diccionario

def sumar(*args):
	result=0
	for i in args:
		result +=i
	return result

print(sumar(1,2,3,4,5,6,7,8,9,10))

# SIMILAR con ** pero es como diccionario

def sum(**kwargs):
	result= kwargs.get('numero',"No existe una key llamada numero")
	print(result)
	pass

sum(valor=1,numero=2,nem="soyletra")
"""

"""
# LAMBDAS o funciones anonimas
# sirven para escribir funciones cortas//simples?

revertir = lambda cadena: cadena[::-1]
print(revertir("revertira?"))

sumar = lambda x,y: x+y
print(sumar(5,2))
"""
"""
# Funciones 2?


def generador(*args=, **kwargs):
    result1 = 0
    result2 = []
    for arg in args:
        result1 += arg
        if arg == None:
            print("no hay arg")

    for kwarg in kwargs:
        result2 += kwarg

    return result1, result2


print(generador(Hola=1, si=2))
"""
"""
# NamesSpace y llamadas de retorno
Crear una función que luego sea llamada desde otra función validando la
existencia de la función.

def mensaje(nombre):
 # Esta función retorna un mensaje de saludo
 return "Hola " + nombre

def llamada_de_retorno(nombre, funcion=""):
 # Llamada de retorno a nivel global
  if funcionin globals():
 return globals()[funcion](nombre)
 else:
return "La función no existe"

print(llamada_de_retorno("Maria", "mensaje"))
print(llamada_de_retorno("Maria", "saludo"))

"""
"""
diccio1 = {"aa": "asd", "diccio2": {"dica": "aaaa"}}

print(diccio1["diccio2"].get("dica"))
"""

"""
# Prog Orientada a Obejtos
# con __init__ creamos el constructor, podemos usar __ antes de una propiedad para que estee protegida y solo se pueda acceder a ella mediante la
# misma clase, es decir solo se pueden modificar estos atributos desde dentro de la clase// Sucede lo mismo con metodos que tienen__
# Siempre se pasa self como parametro a los metodos en python

class auto_protegido():

    def __init__(self):
        self.__ruedas = 4
        self.__arrancado = False
        self.__color = "Negro"

    def arrancar(self, estado):
        self.__arrancado = estado
        if estado:
            print("El auto esta arrancado")
        else:
            print("El auto esta apagado")

    def print_estado(self):
        print("El auto tiene:", self.__ruedas, "ruedas, es de color",
              self.__color, "y esta", self.__arrancado)


auto_1 = auto_protegido()

auto_1.print_estado()

"""
# POO HERENCIA

# el __ es para privado es decir solo  se accede desde la clase, luego est el "..buscar.." que es para protegido es decir solo la clase padre y
# las clases hijos pueden modificar ese atrib y ulltimo esta publico que es como normalmente se declara una variable sin __


class vehiculo():

    def __init__(self, marca, gasolina):
        self.__marca = marca
        self.gasolina = gasolina
        self.__arrancado = False
        self.velocidad = 0

    def arrancar(self, estado):
        self.__arrancado = estado
        if estado:
            print("El vehiculo esta arrancado")
        else:
            print("El vehiculo esta apagado")

    def acelerar(self):
        if self.__arrancado:
            self.velocidad += 10
        else:
            print("Encienda el vehiculo, para acelerar")
            return

    def estado(self):
        print("Velocidad:", self.velocidad, "\n",
              "Gasolina:", self.gasolina, "\n")

    def frenar(self):
        if self.__arrancado:
            self.velocidad -= 10
        else:
            print("Encienda el vehiculo, para frenar")
            return

# para acceder a atributos y metodos de la clase padre es necesario que no le pongamos en la clase padre los __ ya que no me permmitira modificar atributos
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Para extender constructor mirar aca:


class moto(vehiculo):
    def __init__(self, marca, gasolina):
        vehiculo.__init__(self, marca, gasolina)
        self.__ruedas = 2

    def estado(self):
        print("Velocidad:", self.velocidad, "\n",
              "Gasolina:", self.gasolina, "\n",
              "ruedas:", self.__ruedas, "\n")


moto1 = moto("marcaPapel", 1000)
moto1.arrancar(True)
moto1.acelerar()
moto1.estado()
moto1.acelerar()
moto1.acelerar()
moto1.acelerar()
moto1.estado()
moto1.frenar()
moto1.estado()
moto1.frenar()
moto1.estado()
moto1.arrancar(False)
moto1.estado()

# HERNCIA MULTIPLE

# Podemos poner:
# class moto_electrica(electrico, vehiculo): esta clase hereda las fiun cy atributo de ambas pero dando rpeferencia ala primero nombrado
# en este caso si ambos tienen _init_ se usa el de electricos pq esta primero
