"""
# podemos importar toda la biblioteca
import func_mat

resultado = func_mat.sumar(2, 3, 4, 8, 3, 1)
print(resultado)
"""

"""
# O simplemente una de las funciones asi no tengo que nombrar func_mat cada vez que quiera llamar a una funcion (esta y la anterior mejores que la 3ra)

from func_mat import sumar
resultado = sumar(2, 3, 4, 8, 3, 1)
print(resultado)
"""

"""
# O importar toda la biblioteca, no recomendado para programas grandes ya que se reserva espacio de memoria sin sentido

from func_mat import *
resultado = sumar(2, 3, 4, 8, 3, 1)
print(resultado)
"""
"""
# Para impportar clases y obj hacerlo de esta ultima manera??? investigar

# Para IMPORTAR PAQUETES: por ej hay una carpeta(paquete) llamada calculos y dentro esta el archivo cacl_redondear.py con la funcion redondear()
# RECORDAR: hay que crear un archivo vacio llamado __init__.py en la carpeta que se use como paquete

# tambien se puede hacer import *
from calculos.calc_redondear import redondear
redondear(5.6)
"""
