from Crypto.Util.number import long_to_bytes

# Número decimal dado
n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convertir a bytes
message_bytes = long_to_bytes(n)


# Convertir bytes a texto
message = message_bytes.decode()

print(message)
