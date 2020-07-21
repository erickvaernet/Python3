import tkinter

root = tkinter.Tk()

frame_1 = tkinter.Frame(root, width="1280", height="700")

frame_1.pack()

label1 = tkinter.Label(frame_1, text="Primer texto: Hola",
                       fg="black", font=("Arial", 12),)

label1.place(x=10, y=20)

"""Se podria resumir asi si es que no usamos mas la etiqueta:
tkinter.Label(frame_1, text="Primer texto: Hola", fg="black", font=("Arial", 12),).place(x=10, y=20)
"""

# IMAGENES solo png y gif=? sino agregar otra libreria

miImagen = tkinter.PhotoImage(file="icono.png")

label2 = tkinter.Label(frame_1, image=miImagen, )

label2.place(x=50, y=50)


root.mainloop()
