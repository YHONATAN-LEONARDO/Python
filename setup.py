from sympy import nextprime
from random import getrandbits

def get_primes(k):
    """
    Genera dos números primos de aproximadamente k bits
    """
    p = nextprime(getrandbits(k))
    q = nextprime(getrandbits(k))
    return p, q
