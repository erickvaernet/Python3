# .pyw como extension para que no se abra la consola de python por detras
import tkinter

'''{---------------------------VENTANA RAIZ--------------------------------------------'''
raiz = tkinter.Tk()  # Se crea el objeto de ventana

raiz.title("Ventana Principal")  # titulo

# Impide que se redimencione tanto en ancho como en alto
raiz.resizable(False, False)

raiz.iconbitmap("icono.ico")  # Se le pone el icono deseado

# raiz.geometry("800x600")  # Dimension de la ventana NO SE HACE YA QUE SE ADAPTA AL TAMAÑO DEL FRAME

raiz.config(bg="black")  # Color de fondo nose si funcionara con valores hexa
'''-------------------------------------------------------------------------------------}'''


'''{---------------------------FRAME DENTRO DE VENTANA RAIZ---------------------------------------'''

frame1 = tkinter.Frame()

# PARA QUE EL FRAME REDIMENSIONE EN ALTO Y ANCHO/ el expand permite redimension en vertical
frame1.pack(fill="both", expand=True)

frame1.config(bg="blue")

frame1.config(width="800", height="600")

frame1.config(bd=20)  # Tamaño del borde

# Estilo del borde https://www.tutorialspoint.com/python/tk_relief.htm
frame1.config(relief="groove")

frame1.config(cursor="hand2")

'''-----------------------------------------------------------------------------------}'''

'''{---------------------------VENTANA RAIZ BUCLE---------------------------------------'''
# --- PRINCIPAL esto permite que se mantenga abierta la ventana!!!!
raiz.mainloop()

'''----------------------------------------------------------------------------------}'''
