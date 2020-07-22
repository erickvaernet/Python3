import tkinter

root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.pack()
# ------------------------------Variables--------------------------------
string_pantalla = tkinter.StringVar()

operacion = ""
resultado = 0
aux_operacion = ""
primera_operacion = 1

# ------------------------------Pantalla---------------------------------
pantalla = tkinter.Entry(frame, textvariable=string_pantalla)
# COLUMNSPAN permite decir cuantas columnas ocupa la pantalla
pantalla.grid(row=0, column=0, padx=5, pady=5, columnspan=4,)
pantalla.config(background="black", fg="green", width=20, font=40)

# -----------------------------Función_Pantalla--------------------------


def escribir_pantalla(numero):
    global operacion
    global aux_operacion
    if operacion != "":
        aux_operacion = operacion
        string_pantalla.set(numero)
        operacion = ""
    else:
        string_pantalla.set(string_pantalla.get() + numero)

# -----------------------------Función_operaciones--------------------------


def suma(num):
    global operacion
    global resultado
    resultado += int(num)
    operacion = "suma"
    string_pantalla.set(resultado)


def resta(num):
    global operacion
    global resultado
    global primera_operacion
    if primera_operacion != 1:
        resultado -= int(num)
    else:
        resultado = int(num)
        primera_operacion = 0
    operacion = "resta"
    string_pantalla.set(resultado)


def igual(num):
    global aux_operacion
    global resultado
    if aux_operacion == "suma":
        suma(num)
    elif aux_operacion == "resta":
        resta(num)
    else:
        string_pantalla.set("*ERROR*: REINICIE")


# ------------------------------Teclas---------------------------------
num_7 = tkinter.Button(frame, text="7", width=5, command=lambda: escribir_pantalla(
    "7")).grid(row=1, column=0, pady=2)

num_8 = tkinter.Button(frame, text="8", width=5, command=lambda: escribir_pantalla(
    "8")).grid(row=1, column=1, pady=2)

num_9 = tkinter.Button(frame, text="9", width=5, command=lambda: escribir_pantalla(
    "9")).grid(row=1, column=2, pady=2)


num_4 = tkinter.Button(frame, text="4", width=5, command=lambda: escribir_pantalla(
    "4")).grid(row=2, column=0, pady=2)

num_5 = tkinter.Button(frame, text="5", width=5, command=lambda: escribir_pantalla(
    "5")).grid(row=2, column=1, pady=2)

num_6 = tkinter.Button(frame, text="5", width=5, command=lambda: escribir_pantalla(
    "6")).grid(row=2, column=2, pady=2)


num_1 = tkinter.Button(frame, text="1", width=5, command=lambda: escribir_pantalla(
    "1")).grid(row=3, column=0, pady=2)

num_2 = tkinter.Button(frame, text="2", width=5, command=lambda: escribir_pantalla(
    "2")).grid(row=3, column=1, pady=2)

num_3 = tkinter.Button(frame, text="3", width=5, command=lambda: escribir_pantalla(
    "3")).grid(row=3, column=2, pady=2)


simb_igual = tkinter.Button(frame, text="=", width=5, command=lambda: igual(
    string_pantalla.get())).grid(row=4, column=0, pady=2)

num_0 = tkinter.Button(frame, text="0", width=5, command=lambda: escribir_pantalla(
    "0")).grid(row=4, column=1, pady=2)

coma = tkinter.Button(frame, text=",", width=5, command=lambda: escribir_pantalla(
    ",")).grid(row=4, column=2, pady=2)


simb_resto = tkinter.Button(
    frame, text="*", width=5, command=lambda: escribir_pantalla("*")).grid(row=1, column=3, pady=2)

simb_div = tkinter.Button(
    frame, text="/", width=5, command=lambda: escribir_pantalla("/")).grid(row=2, column=3, pady=2)

simb_suma = tkinter.Button(frame, text="+", width=5,
                           command=lambda: suma(string_pantalla.get())).grid(row=3, column=3, pady=2)

simb_resta = tkinter.Button(
    frame, text="-", width=5, command=lambda: resta(string_pantalla.get())).grid(row=4, column=3, pady=2)


# ---------------------------------loop-----------------------------------
root.mainloop()
