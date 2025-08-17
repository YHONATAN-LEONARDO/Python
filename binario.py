# Números de ejemplo
a = 5   # binario: 0101
b = 3   # binario: 0011

# Operadores AND, OR, XOR, NOT
print("AND (a & b):", a & b)   # 0101 & 0011 = 0001 -> 1
print("OR  (a | b):", a | b)   # 0101 | 0011 = 0111 -> 7
print("XOR (a ^ b):", a ^ b)   # 0101 ^ 0011 = 0110 -> 6
print("NOT (~a):", ~a)         # ~0101 = 1010 (complemento a 2) -> -6

# Desplazamiento a la izquierda (<<)
print("a << 1:", a << 1)       # 0101 -> 1010 -> 10
print("a << 2:", a << 2)       # 0101 -> 010100 -> 20

# Desplazamiento a la derecha (>>)
print("a >> 1:", a >> 1)       # 0101 -> 0010 -> 2
print("a >> 2:", a >> 2)       # 0101 -> 0001 -> 1

# Ejemplo práctico: encender, apagar y verificar bits
bitmask = 0b0000  # todos apagados

# Encender el bit 2
bitmask |= (1 << 2)
print("Encender bit 2:", bin(bitmask))

# Apagar el bit 2
bitmask &= ~(1 << 2)
print("Apagar bit 2:", bin(bitmask))

# Verificar si el bit 2 está encendido
if bitmask & (1 << 2):
    print("Bit 2 está encendido")
else:
    print("Bit 2 está apagado")
