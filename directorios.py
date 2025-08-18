import os

# 1. Obtener el directorio actual
ruta_actual = os.getcwd() 
print("Directorio actual:", ruta_actual)

# 2. Cambiar de directorio
os.chdir('/home/yhonatan/python/icpc/prueba')
print("Directorio cambiado a:", os.getcwd())

# 3. Listar archivos y carpetas del directorio actual
contenido = os.listdir()  # lista todos los archivos y carpetas
print("Contenido del directorio:", contenido)

# 4. Crear un nuevo directorio
nuevo_directorio = "nueva_carpeta"
if not os.path.exists(nuevo_directorio):
    os.mkdir(nuevo_directorio)
    print(f"Directorio '{nuevo_directorio}' creado.")
else:
    print(f"Directorio '{nuevo_directorio}' ya existe.")

# 5. Crear directorios recursivos
ruta_completa = "carpeta1/carpeta2/carpeta3"
os.makedirs(ruta_completa, exist_ok=True)  # exist_ok=True evita error si ya existen
print(f"Directorios '{ruta_completa}' creados.")

# 6. Renombrar archivos o carpetas
archivo_viejo = "prueba.txt"
archivo_nuevo = "prueba_renombrada.txt"
if os.path.exists(archivo_viejo):
    os.rename(archivo_viejo, archivo_nuevo)
    print(f"{archivo_viejo} renombrado a {archivo_nuevo}")

# 7. Eliminar archivos
if os.path.exists(archivo_nuevo):
    os.remove(archivo_nuevo)
    print(f"{archivo_nuevo} eliminado.")

# 8. Eliminar directorios vacíos
if os.path.exists(nuevo_directorio):
    os.rmdir(nuevo_directorio)  # Solo elimina si está vacío
    print(f"Directorio '{nuevo_directorio}' eliminado.")

# 9. Eliminar directorios recursivamente
import shutil
if os.path.exists("carpeta1"):
    shutil.rmtree("carpeta1")  # Elimina carpeta1 y todo su contenido
    print("Directorios recursivos eliminados.")

# 10. Comprobar si es archivo o directorio
for item in os.listdir():
    if os.path.isdir(item):
        print(f"{item} es un directorio")
    elif os.path.isfile(item):
        print(f"{item} es un archivo")

os.system('clear')
os.system('ls -al')
os.system('echo "hola bebe"')