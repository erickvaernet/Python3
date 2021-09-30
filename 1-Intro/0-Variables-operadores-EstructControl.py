#Las variables  en python se declaran con el nombre (Ej:variable), el valor (Ej:1) y el operador de asignación (=) . 
variable = 1

# Para modificar el valor de una variable, basta con asignarle un nuevo valor después de definirla
variable = 45

# Tipado Dinámico: las variables pueden tomar diferentes valores de distintos tipos en diferentes momentos
'''Las variables en Python son declaradas por su contenido y no por su contenedor, lo que
nos va a permitir cambiar el valor y tipo de una variable durante la ejecución sin
necesidad de volver a declarar'''

#-Valor numérico en la variable:
numero= 231 

#-Valor de cadena en la variable
cadena= "hola" 

#Fuertemente Tipado: 
'''dado el valor de una variable de un tipo concreto, no se puede usar como 
si fuera de otro tipo distinto a menos que se haga una conversión'''

#numero
x = 10

#cadena
y = "10"

#Es necesario realizar la conversion de 'y' para poder sumarla a 'x' como número
resultado= x + int(y)

#Concatenar= unir cadenas
stri= "hola"+" "+"chau"
print(stri) #print permite mostrar los valores en consola

#Numeros y cadenas
frase= "hola "+str(2) # se caste a string el numero
print(frase)
print(frase,454) #para concatenar dentro del print se usa la ,

# *Operadores*:
#Suma,resta,multiplicación,división
a= 2-1
print("suma:",a)
b= 2+1
print("resta:",b)
c= 2*1
print("mult:",c)
d= 2/1
print("div:",d)

#Potencia
e=2**2
print("potencia:",e)

#modulo(o resto)
f=3%2
print("modulo:",f)

#Comparación
print(a==b)
print(c!=d)
print(d>e)
print(d<e)
print(d>=e)
print(d<=e)

#Logicos
True and False # En otros &&
True or False # En otros ||
True not False # En otros !


#Tipos: Ver imagen: "tipos-datos.jpg"
#tener en cuenta que los tipos tambien son objetos que heredan de otro ej: float hereda de number al igual que int
'''El tipo de un dato está definido por el conjunto de valores que puede tomar a lo
largo de un programa. Para ver los tipos de datos a continuación usaremos la función type(), 
que nos devuelve el tipo de objeto que enviamos como argumento'''
print("-----Tipos-----")
print(type(2))
print(type(2.2))
print(type("asd"))
print(type(True))

print(type((1,2)))
print(type([1,2,"21asd"]))
print(type({1,"sss",54,"asde"}))
print(type({"clave":"valor", 1:2, "clave3":3, 3:"asdad"}))

asd=None #falta de valor
print(type(asd))

#*Por otro lado, en Python se distingue entre objetos mutables y objetos inmutables:
#   1-Los objetos inmutables son objetos que no se pueden modificar. Por ejemplo, los números, las cadenas y las tuplas son objetos inmutables
#   2-Los objetos mutables son objetos que se pueden modificar. Por ejemplo, las listas y los diccionarios son objetos mutables.

#---Condicionales---
if True and False:
    print("uno")
elif False or False:
    print("dos")
else:
    print("tres")

#*----Estruct Repetitivas--:
#While
cont = 0
suma = 0
n = int(10)
while ​cont <= n:
    suma = suma + cont
    cont += 1
print('La suma total es: ', suma)

#for
print("Comienzo")
for i in range(3):
    print("Hola ", end="")
    if i==2 break
else:
    print("Final")

