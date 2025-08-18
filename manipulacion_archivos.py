# 1. Abrir un archivo en modo lectura
mi_archivo = open('prueba.txt', 'r')  # 'r' = lectura
# Leer todo el contenido
contenido = mi_archivo.read()
print("Contenido completo del archivo:")
print(contenido)

# Volver al inicio del archivo si queremos leer otra vez
mi_archivo.seek(0)

# Leer solo una línea
una_linea = mi_archivo.readline()
print(f'Esta es la primera línea: {una_linea.strip()}')  # .strip() elimina saltos de línea

# Leer todas las líneas restantes en una lista
todas_las_lineas = mi_archivo.readlines()
print("Resto de las líneas:")
for linea in todas_las_lineas:
    print(linea.strip())

# Cerrar el archivo
mi_archivo.close()


# 2. Crear un archivo nuevo o sobrescribir si ya existe
archivo = open('prueba.txt', 'w')  # 'w' = escritura (sobrescribe)
archivo.write('Hola bebe 1\n')
archivo.write('Hola bebe 2\n')
print("Archivo creado y escrito con 2 líneas.")
archivo.close()


# 3. Añadir contenido a un archivo existente
archivo = open('prueba.txt', 'a')  # 'a' = append (añadir al final)
archivo.write('Hola bebe 3\n')
archivo.write('Hola bebe 4\n')
print("Se añadieron 2 líneas más al archivo.")
archivo.close()


# 4. Leer nuevamente para verificar cambios
archivo = open('prueba.txt', 'r')
print("Contenido final del archivo:")
for linea in archivo:
    print(linea.strip())
archivo.close()
