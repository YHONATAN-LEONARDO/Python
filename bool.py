# Variables booleanas
a = True
b = False

print("a:", a)   # True
print("b:", b)   # False

# Operadores lógicos
print("a and b:", a and b)   # False
print("a or b:", a or b)     # True
print("not a:", not a)       # False

# Comparaciones que devuelven booleanos
x = 10
y = 5

print("x == y:", x == y)     # False
print("x != y:", x != y)     # True
print("x > y:", x > y)       # True
print("x < y:", x < y)       # False

# Uso de in y not in (verifica pertenencia)
lista = [1, 2, 3, 4, 5]
print("3 in lista:", 3 in lista)         # True
print("10 not in lista:", 10 not in lista)  # True

# Conversión a booleano con bool()
print("bool(0):", bool(0))         # False
print("bool(''):", bool(''))       # False
print("bool('texto'):", bool('texto'))  # True
print("bool([]):", bool([]))       # False
print("bool([1,2]):", bool([1,2])) # True

# Uso en condicionales
edad = 20
if edad >= 18 and "a" in ["a", "b", "c"]:
    print("Mayor de edad y 'a' está en la lista")

if not b:
    print("b es False")
