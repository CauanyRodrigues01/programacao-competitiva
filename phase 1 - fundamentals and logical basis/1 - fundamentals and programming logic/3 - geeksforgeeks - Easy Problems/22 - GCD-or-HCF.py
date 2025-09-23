# https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1
import math
math.g
# Método 1: Usando recursão
# def gcd(a, b):
#     return a if b == 0 else gcd(b, a % b)

# Método 2: Usando while
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Método 3: Usando a função da biblioteca math
def gcd(a, b):
    return math.gcd(a, b)
