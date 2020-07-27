# .pyw como extension para que no se abra la consola de python por detras
import tkinter

raiz = tkinter.Tk()  # Se crea el objeto de ventana

raiz.title("Ventana Principal")  # titulo

# Impide que se redimencione tanto en ancho como en alto
raiz.resizable(False, False)

raiz.iconbitmap("icono.ico")  # Se le pone el icono deseado

raiz.geometry("800x600")  # Dimension de la ventana

# Color de fondo nose si funcionara con valores hexa
raiz.config(bg="black")


# --- PRINCIPAL esto permite que se mantenga abierta la ventana
raiz.mainloop()
