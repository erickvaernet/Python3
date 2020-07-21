import tkinter

root = tkinter.Tk()

frame_1 = tkinter.Frame(root, width="1280", height="700")

frame_1.pack()

tkinter.Label(frame_1, text="Nombre:",
              fg="black", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=10, pady=10)

formulario_1 = tkinter.Entry(frame_1).grid(
    row=0, column=1, padx=10, pady=10)


tkinter.Label(frame_1, text="Apellido:",
              fg="black", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=10, pady=10)

formulario_2 = tkinter.Entry(frame_1).grid(row=1, column=1, padx=10, pady=10)


tkinter.Label(frame_1, text="Email:",
              fg="black", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=10, pady=10)

formulario_3 = tkinter.Entry(frame_1).grid(row=2, column=1, padx=10, pady=10)

tkinter.Label(frame_1, text="Contraseña:", fg="black", font=(
    "Arial", 12)).grid(row=3, column=0, sticky="e", padx=10, pady=10)

formulario_4 = tkinter.Entry(frame_1)
formulario_4.grid(row=3, column=1, padx=10, pady=10)
formulario_4.config(show="*")

tkinter.Label(frame_1, text="Comentarios:", fg="black", font=(
    "Arial", 12)).grid(row=4, column=0, sticky="n", padx=10, pady=10)


# Despues el texto
texto = tkinter.Text(frame_1, width=20, height=10).grid(
    row=4, column=1, pady=10)


root.mainloop()
