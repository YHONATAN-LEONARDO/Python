from Crypto.Util.number import long_to_bytes
import gmpy2

# --- Datos del reto ---
N = 17579151265991064773743067229253647427361470032064109043546795247258657422592183543341821745092623235708878211779688699759281729459036446601807836499705318
e = 65537
cyphertext = 6060082773316978585018792045277282070354838396919260533234269469932697709957788117096038723451576575399035249205219989578745861179097534880147707345132835

# --- Paso 1: Fermat factorization ---
def fermat_factor(n):
    a = gmpy2.isqrt(n)
    b2 = a*a - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = a*a - n
    b = gmpy2.isqrt(b2)
    return int(a-b), int(a+b)

p, q = fermat_factor(N)
print(f"p = {p}\nq = {q}")

# --- Paso 2: Calcular phi(N) ---
phi = (p-1)*(q-1)

# --- Paso 3: Calcular d ---
d = gmpy2.invert(e, phi)

# --- Paso 4: Descifrar cyphertext ---
m = pow(cyphertext, d, N)

# --- Paso 5: Convertir a texto la bandera ---
flag = long_to_bytes(m)
print("Flag:", flag.decode())
