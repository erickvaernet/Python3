""" Este programa simula el juego de Ta-Te-Ti con lo aprendido en el curso "Estructuras de Datos en Python",
por ello se realizo tratando de limitarse a lo aprendido en el curso"""

import math
import random
import time

# --------------------------------Funciones Utilizadas--------------------------------------------


# Este procedimiento pinta un tablero de ta-te-ti segun las posiciones ocupadas (parametro tablero)
def pintar_tablero(tablero):

    print("""
    |{0}||{1}||{2}|
    |{3}||{4}||{5}|
    |{6}||{7}||{8}|
    """.format(tablero[0][0], tablero[0][1], tablero[0][2], tablero[1][0], tablero[1][1], tablero[1][2], tablero[2][0], tablero[2][1], tablero[2][2]))


# Esta funcion inserta una ficha (segun su simbolo "x" u "o") en una posicion seleccionada del tablero,
# y devuelve 1 en caso de que se haya insertado stisfactoriamente, si la posicion indicada esta ocupada, no se  inserta la ficha y devuelve 0
# Se toman como parametro el tablero de ta-te-ti, la posicion que se va ocupar en el tablero y el cimbolo o ficha que se va a insertar
def ocupar_posicion(tablero, posicion, simbolo):
    if posicion > 9 or posicion < 1:
        return 0
    # Se calculan las filas y columnas de la matriz segun la posicion indicada
    fila = (posicion-1)//3
    columna = posicion-((fila*3)+1)

    # Si la posicion esta ocupada retorna = 0 en caso contrario coloca la ficha y retorna 1
    if tablero[fila][columna] == "X" or tablero[fila][columna] == "O":
        return 0
    else:
        tablero[fila][columna] = simbolo
        return 1


# Esta funcion retorna 1 en caso de que alguien haya ganado, es decir que encuentre 3 simbolos iguales en linea
def arbitro(tablero):
    simbolos = ["X", "O"]

    for s in simbolos:
        for i in range(3):
            if s == tablero[i][0] and tablero[i][0] == tablero[i][1] and tablero[i][1] == tablero[i][2]:
                return 1
            elif s == tablero[0][i] and tablero[0][i] == tablero[1][i] and tablero[1][i] == tablero[2][i]:
                return 1
            elif s == tablero[0][0] and tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]:
                return 1
            elif s == tablero[0][2] and tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]:
                return 1
    else:
        return 0


def juega_maquina(tablero, simbolo):

    # Se genera una posicion aleatoria entre 1 y 9

    # Se inserta la ficha de la maquina en la posición al azar, en caso de que estee ocupada la posicion se entrara en el bucle while,
    # el cual reasignara una nueva posicion random hasta encontrar una libre donde inseratar la ficha
    while True:
        if ocupar_posicion(tablero, random.randint(1, 9), simbolo):
            break

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------Main-------------------------------------------------------------------------------------------------------

# Se inicializa la variable jugar_denuevo en "si" para entrar en el bucle principal del juego
jugar_denuevo = "si"

# Se inicializan en 0 los contadores para las victorias de la maquina y del usuario
victoras_usuario = 0
victoras_maquina = 0


# bucle principal del juego, el cual nos permitira jugar las veces que querramos, siempre y cuando ingresemos "si" al finalizar el juego
while(jugar_denuevo == "si"):
    # Se crea una matriz 3x3 'vacia' ,para el tablero
    tablero = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

    # Se crea un contador que empezara en 0 y se sumara 1 tras cada turno, al llegar  9 si no se eligio un ganador significara que se llego a un empate
    contador_empate = 0

    # Presentacion de Juego
    print("***--- Bienvenido/a a Ta-Te-Ti ---***")

    # Se imprime las victorias tuyas y de la maquina cada vez que se juegue:
    print("*victorias del usuario: %d", victoras_usuario)

    # Se imprime las victorias tuyas y de la maquina cada vez que se juegue:
    print("*victorias de la maquina: %d", victoras_maquina)

    # Se informa y muestra las posiciones disponibles en el tablero
    print("Para jugar ten en cuenta la siguiente numeración de las casillas:")
    print("""
    |1||2||3|
    |4||5||6|
    |7||8||9|
    """)

    # Se entra en un bucle while que se repite hasta que el usuario ingrese un caracter valido
    while True:

        # Se pide introducir el simbolo con el que desea jugar al usuario
        simbolo_usuario = input(
            "Introduce el simbolo con el que desas jugar (X/O):").upper()

        print("")

        # En caso de que el simbolo introducido sea valido se sale del bucle while, caso contrario se emite un mensaje de error
        if simbolo_usuario == "X" or simbolo_usuario == "O":
            break
        else:
            print("Error, introducio un valor no contemplado, solo se admiten 'x' u 'o' como valores, reintroduzca uno de estos")

    # Se imprime el tablero vacio antes de que el jugador elija una posicion:
    print("Tablero vacio:")
    pintar_tablero(tablero)

    # Este if-else nos permite definir quien empieza, e independizarnos de esto para poder realizar un bucle principal donde se desarrolle el juego
    # Recordemos que X siempre empieza
    if simbolo_usuario == "X":

        # Si el usuario eligio "X" entonces se adigna "O" a la maquina, se emite un mensaje al usuario y se procede a un bucle while donde se desarrollan los turnos del juego
        simbolo_maquina = "O"

        print("Elegiste 'X', eres primero en poner:")
    else:

        # Si el usuario eligio "O" entonces se adigna "X" a la maquina, se emite un mensaje al usuario, la maquina realiza su jugada y posteriormente se procede al bucle while
        simbolo_maquina = "X"

        print("Elegiste 'O', eres segundo, empieza la maquina:")
        # Se pasa el tablero y el simbolo correspondiente a la maquina a una funcion que inserta la ficha en un lugar al azar y posteriormente se pinta el tablero
        juega_maquina(tablero, simbolo_maquina)
        pintar_tablero(tablero)

    # Bucle donde se desarrollan los turnos en el juego independientemente de quien comience
    while True:

        # Bucle de control,si el usuario ingresa una posicion fuera de rango o una posicion ocupada se emite un mensaje de error y se vuelve a pedir que elija la posición
        while True:
            error = 0
            try:
                posicion_elegida = (int)(input(
                    "Tu turno, elija la posición en la que desea poner la ficha (posiciones del 1 al 9):"))
            except:
                error = 1
                print("Error: valor")

            # Se usa la funcion para pintar el tablero. En caso de que la posicion elegida estee ocupada la funcion retorna 0 lo que lleva el flujo hacia "else:"
            if error == 0 and ocupar_posicion(tablero, posicion_elegida, simbolo_usuario):
                pintar_tablero(tablero)
                break
            else:
                print("Eligio una posición ocupada o fuera de rango, por favor ingrese una posición libre para poner su ficha, los valores permitidos van del 1 al 9 ")

        # Se aumenta el contador _empate cada vez que juega el usuario o la maquina
        contador_empate = contador_empate + 1

        # Se pasa el tabelro a una funcion arbitro(), si la funcion retorna 1 es decir que hay fichas iguales en linease se suma una victoria al contador de victorias
        #  del usuario y se emite un mensaje de que gano la maquina y se termina la partida
        if arbitro(tablero):
            victoras_usuario = +1
            print("***---¡¡¡Ganaste!!!---***")
            print("*El programa se cerrara automaticamente dentro de 5 segundos, vuelva a iniciarlo si quiere volver a jugar*")
            break

        # Se comprueba el contador de empate
        if contador_empate == 9:
            print("***---Se llego a un empate ---***")
            break

        # El turno de la maquina
        print("\n***-Turno de la maquina:")
        # Se hace una pausa de 0.5 segundos antes del turno
        time.sleep(0.5)
        # Se pasa el tablero y el simbolo correspondiente a la maquina a una funcion que inserta la ficha en un lugar al azar y posteriormente se pinta el tablero
        juega_maquina(tablero, simbolo_maquina)
        pintar_tablero(tablero)

        # Se aumenta el contador _empate cada vez que juega el usuario o la maquina
        contador_empate = contador_empate + 1

        # Se pasa el tabelro a una funcion arbitro(),si la funcion retorna 1 es decir que hay fichas iguales en linea se suma una victoria al contador de victorias
        # de la maquina y seemite un  mensaje de que gano la maquina y se termina la partida
        if arbitro(tablero):
            victoras_maquina = +1
            print("***Gano la maquina... vulve a intantar jugar denuvo***")
            print("*El programa se cerrara automaticamente dentro de 5 segundos, vuelva a iniciarlo si quiere volver a jugar*")
            break

        # Se comprueba el contador de empate
        if contador_empate == 9:
            print("***---Se llego a un empate ---***")
            break

    # Se le pregunta al usuario si desea repetir el juego
    jugar_denuevo = input(
        "¿Deseas jugar denuevo? en caso positivo escribe 'si', caso contrario solo presiona enter")
