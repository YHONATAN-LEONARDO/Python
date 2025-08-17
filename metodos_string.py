mi_texto = "Este es un texto de prueba"

# 1. upper() - Poner todo en mayúsculas
print("Mayúsculas:", mi_texto.upper())

# 2. count() - Contar cuántas veces aparece una palabra o letra
print("Cantidad de 'e':", mi_texto.count('e'))

# 3. replace() - Reemplazar palabras
nuevo_texto = mi_texto.replace("texto", "mensaje")
print("Reemplazo:", nuevo_texto)

# 4. split() - Dividir el texto en palabras
palabras = mi_texto.split()
print("Lista de palabras:", palabras)

# 5. join() - Unir elementos de una lista con un separador
a = ['te', 'amo', 'mucho']
nuevo_a = '-'.join(a)
print("Lista unida con guiones:", nuevo_a)
