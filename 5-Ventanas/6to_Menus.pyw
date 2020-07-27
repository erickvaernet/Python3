import tkinter


root = tkinter.Tk()

barra_menu = tkinter.Menu(root)  # Barra del menu va a estar en el root
root.config(menu=barra_menu)  # nos construye el menu

# PRIMERO: SE CREAN LAS CASCADAS CON SUS ETIQUETAS Y DESPUES SE LAS AGREGA AL MENU~
# ES DECIR QUE PRIMERO CREAMOS LAS ETIQUETAS QUE VAN A IR DENTRO DE CADA MENU Y DESPUES RECIEN CREAMOS EL NOMBRE DEL MENU EJ: "FILE", PRIMERO LOS ELEMENTOS:

# elementos del menu //el tearoff es para sacar la barra de defecto
menu_file = tkinter.Menu(barra_menu, tearoff=0)
menu_file.add_command(label="New")
menu_file.add_command(label="Save")
menu_file.add_command(label="load")


# ACA no usamos el tear off ver diferencia
menu_view = tkinter.Menu(barra_menu)
menu_view.add_command(label="Search")
menu_view.add_command(label="Replace")
menu_view.add_command(label="idk")

menu_edit = tkinter.Menu(barra_menu)
menu_go = tkinter.Menu(barra_menu)

# ACA RECIEN DECLARAMOS ELMENU FILE SIENDO QUE YA ESTA DECLARADO SUS ELEMENTOS
# Agregamos las cascadas uniendo un label con los elementos
barra_menu.add_cascade(label="File", menu=menu_file)
barra_menu.add_cascade(label="View", menu=menu_view)
barra_menu.add_cascade(label="Edit", menu=menu_edit)
barra_menu.add_cascade(label="Go", menu=menu_go)


# __________________________________________________
frame = tkinter.Frame(root, width=820, height=640)

root.mainloop()
