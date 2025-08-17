mi_set = {
    42,                     # int
    3.14,                   # float
    "hola",                 # string
    True,                   # boolean
    (1, 2),                 # tupla (inmutable)
    b"bytes",               # bytes
    frozenset({1, 2, 3}),   # frozenset (conjunto inmutable)
    None                    # NoneType
}
# 1. add() - Agregar elemento
mi_set.add(4)
print("Después de add(4):", mi_set)

# 2. remove() - Eliminar elemento (error si no existe)
mi_set.remove(2)
print("Después de remove(2):", mi_set)

# 3. discard() - Eliminar elemento (sin error si no existe)
mi_set.discard(10)  # No pasa nada
print("Después de discard(10):", mi_set)

# 4. pop() - Eliminar y devolver un elemento arbitrario
elemento = mi_set.pop()
print("Elemento eliminado con pop():", elemento)
print("Set después de pop():", mi_set)

# 5. clear() - Vaciar el set
mi_set.clear()
print("Después de clear():", mi_set)
