# https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1

'''
Método 1: Usando a terceira variável

class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        c = a
        a = b
        b = c
        return a, b
'''

'''
Método 2: Usando o operador XOR Bitwise

class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b
'''

# Método 3: Usando desempacotamento de tuplas

class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        a, b = b, a
        return a, b