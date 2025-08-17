import base64 as b6

flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convertir hexadecimal a bytes
binario = bytes.fromhex(flag)

print(binario)

# Codificar los bytes a Base64
encodebase64 = b6.b64encode(binario)
print(encodebase64)

# Mostrar como cadena
print(encodebase64.decode())
