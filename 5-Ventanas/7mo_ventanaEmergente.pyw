import tkinter
from tkinter import messagebox


root = tkinter.Tk()

# ------------------------messagebox para ventana emergente------------------------

# Ventana de informacion


def ventana_emergente_inf():
    # Primer parmetro el titulo y segundo el contenido
    messagebox.showinfo("Creaste un nuevo archivo", "Felicidades")


# Ventana de Advertencia
def ventana_emergente_adv():
    messagebox.showwarning("Creaste un nuevo archivo", "Felicidades")


# de tipo ask de tipo Si / No
def salir_app():

    # ESTA funcion devuelve "yes" si apretan en boton de si y "no" si apretan en no
    respuesta = messagebox.askquestion("Salir", "¿Deseas salir?")

    if respuesta == "yes":
        root.destroy()


# de tipo ask pero de tipo Aceptar / Cancel
def salir_app2():

    # ESTA funcion devuelve True si apretan en boton de si y False si apretan en no
    respuesta = messagebox.askokcancel("Salir", "Estas por salir")

    if respuesta == True:
        root.destroy()


# de tipo ask pero de tipo Reintentar / Cancel
def salir_app3():

    # ESTA funcion devuelve True si apretan en boton de reintentar y False si apretan en no
    respuesta = messagebox.askretrycancel(
        "Salir", "aprienta en reintentar para salir")

    if respuesta == True:
        root.destroy()

# ---------------------------------------------------------------------------------


barra_menu = tkinter.Menu(root)  # Barra del menu va a estar en el root
root.config(menu=barra_menu)  # nos construye el menu

# Cascada de file
menu_file = tkinter.Menu(barra_menu, tearoff=0)
# agregamos la ventana emergente con command
menu_file.add_command(label="New", command=ventana_emergente_inf)
menu_file.add_command(label="Save", command=ventana_emergente_adv)
menu_file.add_command(label="load")
menu_file.add_command(label="Exit", command=salir_app)
menu_file.add_command(label="Exit-2", command=salir_app2)
menu_file.add_command(label="Exit-3", command=salir_app3)

# Cascada de view
menu_view = tkinter.Menu(barra_menu)
menu_view.add_command(label="Search")
menu_view.add_command(label="Replace")
menu_view.add_command(label="idk")


# Cascada de edit
menu_edit = tkinter.Menu(barra_menu)


# Cascada de Go
menu_go = tkinter.Menu(barra_menu)

# titulos de cascadas,se asigna su cascada respectiva
barra_menu.add_cascade(label="File", menu=menu_file)
barra_menu.add_cascade(label="View", menu=menu_view)
barra_menu.add_cascade(label="Edit", menu=menu_edit)
barra_menu.add_cascade(label="Go", menu=menu_go)


# __________________________________________________
frame = tkinter.Frame(root, width=820, height=640)

root.mainloop()
