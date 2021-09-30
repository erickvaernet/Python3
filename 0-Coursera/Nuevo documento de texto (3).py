"""
Created on Saturday September  19/09/2020 2020

@author:    Fernando JesÃºs Aranda Polo
"""

import random

# Func 1 -> Mostrar la matriz por pantalla
def write_matrix():
    for fila in range(len(matriz)):
        print (matriz[fila])
    print("\n")
        
# Func 2 -> Asignar valor
def write_value(fila,col,symbol):
    matriz[int(fila)][int(col)] = symbol
    
# Func 3 -> Comprobar hueco
def comprobar(fila, col):
    comprobacion = False
    if (matriz[fila][col] == "_"):
        comprobacion = True
    return comprobacion

def comprobar_valores(fila, col):
    val_fila = False
    val_col = False
    if ((fila == "0") or (fila == "1") or (fila == "2")):
        val_fila = True
    if ((col == "0") or (col == "1") or (col == "2")):
        val_col = True     
    return val_fila and val_col

def comprobar_tres():
    
    ganador = "_"
    
    # Tres en raya horizontales
    for i in range(len(matriz)):
        if (matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2]):
            if (matriz[i][0] != "_"):
                ganador = matriz[i][0]
                break
        
    # Tres en raya verticales
    for i in range(len(matriz)):
        if (matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i]):
            if (matriz[0][i] != "_"):
                ganador = matriz[0][i]
                break
        
    # Tres en raya diagonales
    if (matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]):
        if (matriz[1][1] != "_"):
                ganador = matriz[1][1]
                
    if (matriz[2][0] == matriz[1][1] and matriz[1][1] == matriz[0][2]):
        if (matriz[1][1] != "_"):
                ganador = matriz[1][1]
                
            
    return ganador
            
        


""" AquÃ­ comienza el programa"""

print ("!! Bienvenido al juego del tres en raya !! \n   ")
print ("-------------------------------------------- \n ")

matriz = [
["_","_","_"],
["_","_","_"],
["_","_","_"]]

# ElecciÃ³n X/O

eleccion = False

while (not eleccion):
    
    pregunta = input("Â¿QuÃ© eliges? (X/O) \n")
    if pregunta == "X":
        eleccion = True
        print ("TÃº empiezas")
    elif pregunta == "O":
        eleccion = True
        print ("X empiezan")
    else:
        print ("CarÃ¡cter no vÃ¡lido")
    
turno = 0

while turno < 9:
    
    if pregunta == "X":
        if turno % 2 == 0:
            posible = False
            while (not posible):
                print("Escribe Ã­ndices donde colocar la ficha:")
                idx_fil = input("Ãndice de fila: ")
                idx_col = input("Ãndice de columna: ") 
                posible = comprobar_valores(idx_fil, idx_col)
                if (posible and comprobar(int(idx_fil), int(idx_col))):  
                    write_value(idx_fil, idx_col, pregunta)
                else:
                    print ("Esa posiciÃ³n ya estÃ¡ ocupada")
                    posible = False
        else:
            posible = False
            while (not posible):
                idx_fil = random.choice([0,1,2])
                idx_col = random.choice([0,1,2])
                posible = comprobar(idx_fil,idx_col)
            write_value(idx_fil, idx_col, "O")
    else:
        if turno % 2 == 0:
            posible = False
            while (not posible):
                idx_fil = random.choice([0,1,2])
                idx_col = random.choice([0,1,2])
                posible = comprobar(idx_fil,idx_col)
            write_value(idx_fil, idx_col, "X")
        else:
            posible = False
            while (not posible):
                print("Escribe Ã­ndices donde colocar la ficha:")
                idx_fil = input("Ãndice de fila: ")
                idx_col = input("Ãndice de columna: ")
                posible = comprobar_valores(idx_fil, idx_col)
                if (posible and comprobar(int(idx_fil), int(idx_col))):  
                    write_value(idx_fil, idx_col, pregunta)
                else:
                    print ("Esa posiciÃ³n ya estÃ¡ ocupada")
                    posible = False
           
            
            
        
        
            
      
    print("\n")
    print("Turno:  \n",turno)
    write_matrix()
   
    ganador = comprobar_tres()
    if ganador == "_":
        turno = turno + 1
    else:
        turno = 10
    
if ganador == "_":
    print("Se ha producido un empate")
else:
    print("El ganador es: ",ganador)
