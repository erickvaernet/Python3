import tkinter
from tkinter import filedialog

root = tkinter.Tk()


def abrir_fichero():
    fichero = filedialog.askopenfile(title="Abir Fichero", initialdir="C:", filetypes=(
        ("Tipo txt", "*.txt"), ("Tipo excel", "*.xlsx"), ("Todos los tipos", "*.*")))

    print(fichero)  # Nos devuelve la ruta de datos


tkinter.Button(root, text="Abrir Fichero", command=abrir_fichero).pack()

root.mainloop()
