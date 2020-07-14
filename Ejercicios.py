"""
# Ejercicio1
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no,
valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo @ .


def validar_mail(mail):
    if mail.find("@") == -1:
        return False
    else:
        return True


mail = input("Ingrese su dirección de mail:")

if validar_mail(mail):
    print("Mail Valido")
else:
    print("Mail Invalido")
"""

"""
#Ejercicio 13
Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo
y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.Precondición:
el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI. Ejemplo:
Nombre: Alba María Linares
DNI: 25834910
Alba7258


def comprobar_dni(numero):
    digitos = 0

    while numero:
        numero = numero//10
        digitos += 1

    if digitos == 7 or digitos == 8:
        return True
    else:
        return False


def first_3_digits(num):

    if num >= 100:

        while num > 999:
            num = num//10

        return num
    else:
        print("Error en first_3_digits, el numero indicado tiene menos de 3 digitos")

        return -1


def generar_id(names, dni):
    names = names.split(" ")
    last_name_digits = str(len(names[2]))
    first_3_dni = str(first_3_digits(dni))
    return names[0]+last_name_digits+first_3_dni


while True:
    print("")
    print("*Este sistema se cerrara utomaticamente una vez que aprete enter sin ingresar nombres ni apellidos*")

    nombres_apellido = input(
        "Ingrese el/los nombre/s y el apellido del socio nuevo:")

    if nombres_apellido == "":
        break

    while True:
        dni = int(input("Ingrese el DNI del nuevo socio:"))
        if comprobar_dni(dni):
            print("**DNI Valido**")
            break
        else:
            print("**DNI Invalido, el dni debe poseer 7 u 8 digitos**",
                  "\n", "**Reingrese el dni**")

    id_unico = generar_id(nombres_apellido, dni)

    print("Datos del socio nuevo:")
    print("Nombre:", nombres_apellido)
    print("DNI:", dni)
    print("ID Unico:", id_unico)
"""
