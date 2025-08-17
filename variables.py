import time

# Tipos de variables
nombre = 'Juan'       # str
edad = 12             # int
peso = 70.4           # float
es_mayor = True       # bool
conjunto = {1, 2, 3, 2, 1} # set 
# Colecciones
tupla = (1, 2, 3)     # tuple (inmutable)
lista = [4, 5, 6]     # list (mutable)

# Operadores
x = 6
y = 8
print(f'División entera: {x // y}')  # Resultado entero sin decimales
print(f'División exacta: {x / y}')    # Resultado decimal
print(f'Módulo (resto): {x % y}')     # Resto de la división

# Convertir string a lista de caracteres
nombre_lista = list(nombre)
print(f'Nombre como lista: {nombre_lista}')

# Convertir a booleano (True si cadena no está vacía)
booleano = bool("asdfsadf")
print(f'Booleano de cadena no vacía: {booleano}')

# División con redondeo a 2 decimales
resultado = 90 / 7
resultado_redondeado = round(resultado, 2)
print(f'La división es {resultado} y redondeada a 2 decimales es {resultado_redondeado}')
