"""
class Persona:

    __nombre = "atr privado"

    def __metodPriv(self):
        print("met privado")


p1 = Persona
print(p1.nombre)  # no funciona ya que no puedo acceder al atr desde fuera
"""


class Producto:

    def __init__(self, precio, descripcion, stock):
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock

    def __str__(self):
        return f"Descripcion\t {self.descripcion}\n"\
               f"Precio\t      {self.precio}"


class Calzado(Producto):

    # SOBRESCRIBIENDO el metodo de clase padre
    def __init__(self, precio, descripcion, stock, talle, color):
        Producto.__init__(self, precio, descripcion, stock)
        # super().__init__( precio, descripcion, stock) #Funciona igual que la anterior debido a que super referencia a clase padre
        # pero no se pasa self en super()!!!!! OJO SOLO RECOMENDADO CUANDO EXISTE UNICA SUPERCLASE!!!
        self.talle = talle
        self.color = color

    def __str__(self):
        return f"{Producto.__str__(self)}\n"\
               f"Talles\t    {self.talle}\n"\
               f"Color\t    {self.color}"


producto1 = Producto(30000, "TV led 32' ", 20)
print(producto1.__str__(), "\n")

calzado1 = Calzado(2500, "Nike 24/7", 14,
                   [37, 38, 39, 40, 41, 42, 43], ["Azul", "Rojo", "Amarillo", "Verde"])

print(calzado1.__str__())

# POO polimofrismo

"""Se habla de sobrecarga y sobrescritura,  polimorfismo de sobreescritura es sobreescribir los metodos en clases hijas es decir cada una tiene su implementacion
y de sobrecarga cuando escribo el mismo metodo pero vario la cantidad de parametros me permite tener para un mismo metodo diferentes implementaciones"""

# SE puede usar MRO method resolution order con __mro__ o mro()
print(Calzado.mro())  # este devuelve lista
print(Calzado.__mro__)  # este devuelve tupla
