# ===============================
# Lista simple
# ===============================
lista = ['ana', 'luz', 'diana']
for nombre in lista:
    print(f'Lista simple: {nombre}')

# ===============================
# Diccionario
# ===============================
diccionario = {'ana': 25, 'luz': 30, 'diana': 22}
for clave, valor in diccionario.items():
    print(f'Diccionario: {clave} tiene {valor} años')

# ===============================
# Set (conjunto)
# ===============================
conjunto = {'manzana', 'banana', 'cereza'}
for fruta in conjunto:
    print(f'Set: {fruta}')

# ===============================
# Tupla
# ===============================
tupla = (10, 20, 30)
for numero in tupla:
    print(f'Tupla: {numero}')

# ===============================
# Lista de diccionarios
# ===============================
lista_diccionarios = [
    {'nombre': 'ana', 'edad': 25},
    {'nombre': 'luz', 'edad': 30},
    {'nombre': 'diana', 'edad': 22}
]
for persona in lista_diccionarios:
    print(f"Lista de diccionarios: {persona['nombre']} tiene {persona['edad']} años")

# ===============================
# Iterar con índice usando enumerate
# ===============================
nombres = ['ana', 'luz', 'diana']
for i, nombre in enumerate(nombres):
    print(f'Enumerate: Posición {i}, Nombre {nombre}')






# ===============================
# 1. range(stop)
# ===============================
print("=== range(stop) ===")
for i in range(5):  # 0,1,2,3,4
    print(i, end=' ')
print("\n")

# ===============================
# 2. range(start, stop)
# ===============================
print("=== range(start, stop) ===")
for i in range(2, 6):  # 2,3,4,5
    print(i, end=' ')
print("\n")

# ===============================
# 3. range(start, stop, step)
# ===============================
print("=== range(start, stop, step) ===")
# Incremento positivo
for i in range(1, 10, 2):  # 1,3,5,7,9
    print(i, end=' ')
print()

# Incremento negativo
for i in range(10, 0, -2):  # 10,8,6,4,2
    print(i, end=' ')
print("\n")

# ===============================
# 4. Usando range para iterar listas con índice
# ===============================
nombres = ['ana', 'luz', 'diana']
print("=== range con lista ===")
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")
print("\n")


while False:
    print('no entro')

items = ['a','b','c']

for item in enumerate(items):
    print(item)