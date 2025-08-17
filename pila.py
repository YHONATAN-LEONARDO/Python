import time
import os

bien = "[]"
mal= "[]{)()}"
pila = []
inicio = time.perf_counter()
for character in bien: 
    if character in "{([":
        pila.append(character)
    elif character in "}])":
        if pila:
            pila.pop()
fin = time.perf_counter()
tiempo = (fin - inicio) * 1000


if not pila:
    print(f'La sentencia es correcta ;  y el tiempo es de ejecucion es  {round(tiempo, 3)}')
else:
    print(f'La sentencia esta mal ; y el tiempo de ejecucuion es {round(tiempo,3)}')

archivo = os.path.getsize('pila.py')

print(f'El tamano del archivo es {archivo}')
valor = 3.123415134

print(f'valro es {valor:.2f}')

