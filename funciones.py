# 1. Función básica con return
def suma(a, b):
    return a + b

print(suma(5, 3))  # 8

# 2. Argumentos con valor por defecto
def saludar(nombre="Amigo"):
    print(f"Hola {nombre}")

saludar()          # Hola Amigo
saludar("Yhonatan") # Hola Yhonatan

# 3. Argumentos posicionales y por nombre
def info_persona(nombre, edad):
    print(f"{nombre} tiene {edad} años")

info_persona("Yhonatan", 21)          # Posicional
info_persona(edad=21, nombre="Yhonatan")  # Keyword arguments

# 4. *args -> varios argumentos posicionales
def suma_multiple(*args):
    return sum(args)

print(suma_multiple(1,2,3,4,5))  # 15

# 5. **kwargs -> varios argumentos por nombre
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Yhonatan", edad=21, ciudad="La Paz")

# 6. Combinar todo
def persona_completa(nombre, edad=20, *args, **kwargs):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print("Otros valores posicionales:", args)
    print("Otros valores por nombre:", kwargs)

persona_completa("Yhonatan", 21, "Estudiante", "Hacker ético", ciudad="La Paz", pais="Bolivia")

# 7. Función anidada
def exterior(x):
    def interior(y):
        return y * 2
    return interior(x) + 1

print(exterior(5))  # 11

# 8. Función lambda (función anónima)
multiplicar = lambda a, b: a * b
print(multiplicar(4,5))  # 20
