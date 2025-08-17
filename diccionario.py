diccionario = {
    "entero": 42,                                    # int
    "flotante": 3.1416,                              # float
    "cadena": "Hola, mundo",                         # str
    "booleano": False,                               # bool
    "nulo": None,                                    # NoneType
    "lista": [10, 20, 30, "cuarenta"],               # list
    "tupla": (1, 2, 3, "cuatro"),                    # tuple
    "conjunto": {1, 2, 3, 4},                        # set
    "bytes": b"abc",                                 # bytes
    "diccionario_simple": {"clave": "valor"},       # dict simple
    "diccionario_anidado": {                         # dict anidado
        "nivel1": {
            "nivel2": {
                "nivel3": "final"
            }
        }
    },
    "lista_diccionarios": [                          # lista con dicts
        {"id": 1, "nombre": "Ana"},
        {"id2": 2, "nombre": "Luis"},
    ],
    "tupla_listas": (                               # tupla con listas
        [1, 2], 
        [3, 4]
    ),
    "diccionario_con_tupla_y_lista": {
        "tupla": (5, 6, 7),
        "lista": ["x", "y", "z"]
    }
}
# 1. keys() - Mostrar claves
print("Claves:", diccionario.keys())

# 2. values() - Mostrar valores
print("Valores:", diccionario.values())

# 3. items() - Mostrar pares clave-valor
print("Items:")
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

# 4. get() - Obtener valor con clave, con valor por defecto
print("get clave4:", diccionario.get("clave4", "No encontrado"))

# 5. update() - Actualizar diccionario con nuevos pares
diccionario.update({"clave4": "valor4", "clave5": "valor5"})
print("Diccionario actualizado:", diccionario)

consulta = diccionario['lista_diccionarios'][0]['id']
print(consulta)