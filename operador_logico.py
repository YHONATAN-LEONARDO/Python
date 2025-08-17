# ===============================
# Operadores de comparación
# ===============================
igual = 5 == 5            # True
distinto = 5 != 3         # True
mayor = 7 > 4             # True
menor = 2 < 10            # True
mayor_igual = 5 >= 5      # True
menor_igual = 3 <= 4      # True

# ===============================
# Operadores lógicos
# ===============================
and_true_false = True and False   # False
or_true_false = True or False     # True
not_true = not True               # False

# ===============================
# Comparaciones encadenadas
# ===============================
encadenada1 = 3 < 5 < 8           # True
encadenada2 = 5 < 10 > 8          # True
encadenada3 = 3 == 3 != 5         # True

# ===============================
# Operadores 'in' y 'not in'
# ===============================
in_casa = 'a' in 'casa'           # True
not_in_casa = 'z' not in 'casa'   # True

# ===============================
# Operadores de identidad 'is' y 'is not'
# ===============================
x = [1, 2, 3]
y = x
z = [1, 2, 3]

is_xy = x is y                     # True
is_xz = x is z                     # False
isnot_xz = x is not z               # True
