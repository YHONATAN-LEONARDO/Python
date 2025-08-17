# Listas iniciales
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = ['f', 'g', 'h']

# append() → Agregar un elemento al final (Pila: push)
mi_lista.append(2)
print("Después de append:", mi_lista)

# extend() → Agregar otra lista completa
mi_lista.extend(mi_lista2)
print("Después de extend:", mi_lista)

# insert() → Insertar en una posición específica
mi_lista.insert(1, 'X')
print("Después de insert:", mi_lista)

# pop() → Eliminar y devolver el último elemento (Pila: pop)
ultimo = mi_lista.pop()
print("pop() quitó:", ultimo)
print("Lista después de pop:", mi_lista)

# pop(0) → Eliminar el primer elemento (Cola: dequeue)
primero = mi_lista.pop(0)
print("pop(0) quitó:", primero)
print("Lista después de pop(0):", mi_lista)

# remove() → Eliminar por valor (solo la primera coincidencia)
mi_lista.remove('b')
print("Después de remove('b'):", mi_lista)

# reverse() → Invertir la lista
mi_lista.reverse()
print("Después de reverse:", mi_lista)

# sort() → Ordenar (alfabéticamente o numéricamente)
mi_lista.sort()
print("Después de sort:", mi_lista)

# count() → Contar ocurrencias de un elemento
print("Cantidad de 'f' en mi_lista3:", mi_lista3.count('f'))

# index() → Encontrar posición de un elemento
print("Índice de 'g' en mi_lista3:", mi_lista3.index('g'))
